import shutil
import stat
import subprocess
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).with_name("apply-patch")


class ApplyPatchTest(unittest.TestCase):
    def setUp(self):
        self.tmpdir = Path(tempfile.mkdtemp(prefix="apply-patch-"))
        self.patch_dir = self.tmpdir / "patch"
        self.local_dir = self.tmpdir / "local"
        self.patch_dir.mkdir()
        self.local_dir.mkdir()

    def tearDown(self):
        shutil.rmtree(self.tmpdir)

    def run_cmd(self, *args, cwd=None, check=True):
        result = subprocess.run(
            args,
            cwd=cwd,
            text=True,
            capture_output=True,
        )
        if check and result.returncode != 0:
            raise AssertionError(
                f"command failed: {' '.join(args)}\nstdout:\n{result.stdout}\nstderr:\n{result.stderr}"
            )
        return result

    def init_git_repo(self, path: Path):
        self.run_cmd("git", "init", "-q", cwd=path)
        self.run_cmd("git", "config", "user.name", "Test User", cwd=path)
        self.run_cmd("git", "config", "user.email", "test@example.com", cwd=path)

    def write_text(self, root: Path, relpath: str, content: str):
        file_path = root / relpath
        file_path.parent.mkdir(parents=True, exist_ok=True)
        file_path.write_text(content)

    def test_only_check_reports_diff_and_new_without_modifying_local(self):
        self.write_text(self.patch_dir, "libsame.so", "same\n")
        self.write_text(self.patch_dir, "libdiff.so", "patch\n")
        self.write_text(self.patch_dir, "libnew.so", "new\n")

        self.write_text(self.local_dir, "libsame.so", "same\n")
        self.write_text(self.local_dir, "libdiff.so", "local\n")

        result = self.run_cmd(
            "python3",
            str(SCRIPT),
            "-s",
            str(self.patch_dir),
            "-d",
            str(self.local_dir),
            "--only-check",
        )

        self.assertEqual(result.returncode, 0)
        self.assertIn("DIFF", result.stdout)
        self.assertIn("NEW", result.stdout)
        self.assertEqual((self.local_dir / "libdiff.so").read_text(), "local\n")
        self.assertFalse((self.local_dir / "libnew.so").exists())

    def test_apply_with_skip_new_updates_existing_files_and_creates_commit(self):
        self.init_git_repo(self.local_dir)
        self.write_text(self.patch_dir, "dir/libsame.so", "same\n")
        self.write_text(self.patch_dir, "dir/libdiff.so", "patch\n")
        self.write_text(self.patch_dir, "dir/libnew.so", "new\n")

        self.write_text(self.local_dir, "dir/libsame.so", "same\n")
        self.write_text(self.local_dir, "dir/libdiff.so", "local\n")
        (self.local_dir / "dir/libdiff.so").chmod(0o755)
        self.run_cmd("git", "add", ".", cwd=self.local_dir)
        self.run_cmd("git", "commit", "-q", "-m", "initial", cwd=self.local_dir)

        result = self.run_cmd(
            "python3",
            str(SCRIPT),
            "-s",
            str(self.patch_dir),
            "-d",
            str(self.local_dir),
            "--skip-new",
            "-y",
        )

        self.assertEqual(result.returncode, 0)
        self.assertEqual((self.local_dir / "dir/libdiff.so").read_text(), "patch\n")
        self.assertEqual(stat.S_IMODE((self.local_dir / "dir/libdiff.so").stat().st_mode), 0o755)
        self.assertFalse((self.local_dir / "dir/libnew.so").exists())
        self.assertIn("SKIP", result.stdout)

        log = self.run_cmd("git", "log", "-1", "--pretty=%s", cwd=self.local_dir)
        self.assertEqual(log.stdout.strip(), "apply patch from patch")

        show = self.run_cmd("git", "show", "--summary", "--format=", "HEAD", cwd=self.local_dir)
        self.assertNotIn("mode change", show.stdout)


if __name__ == "__main__":
    unittest.main()

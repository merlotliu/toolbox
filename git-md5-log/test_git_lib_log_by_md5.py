import hashlib
import os
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).with_name("git-md5-log")


class GitMd5LogTest(unittest.TestCase):
    def setUp(self):
        self.tmpdir = Path(tempfile.mkdtemp(prefix="git-lib-log-by-md5-"))
        self.repo = self.tmpdir / "repo"
        self.repo.mkdir()
        self.run_cmd("git", "init", "-q", cwd=self.repo)
        self.run_cmd("git", "config", "user.name", "Test User", cwd=self.repo)
        self.run_cmd("git", "config", "user.email", "test@example.com", cwd=self.repo)

        self.lib_relpath = Path("vendor/lib/libGSLKernel.so")
        self.lib_path = self.repo / self.lib_relpath
        self.lib_path.parent.mkdir(parents=True)

        self.md5_a = self.write_commit(b"AAA", "commit-a", 1700000000)
        self.md5_b = self.write_commit(b"BBB", "commit-b", 1700000100)
        self.md5_a_again = self.write_commit(b"AAA", "commit-c", 1700000200)

    def tearDown(self):
        shutil.rmtree(self.tmpdir)

    def run_cmd(self, *args, cwd=None, env=None, check=True):
        result = subprocess.run(
            args,
            cwd=cwd,
            env=env,
            text=True,
            capture_output=True,
        )
        if check and result.returncode != 0:
            raise AssertionError(
                f"command failed: {' '.join(args)}\nstdout:\n{result.stdout}\nstderr:\n{result.stderr}"
            )
        return result

    def write_commit(self, data, message, timestamp):
        self.lib_path.write_bytes(data)
        self.run_cmd("git", "add", str(self.lib_relpath), cwd=self.repo)
        env = os.environ.copy()
        date = f"{timestamp} +0000"
        env["GIT_AUTHOR_DATE"] = date
        env["GIT_COMMITTER_DATE"] = date
        self.run_cmd("git", "commit", "-q", "-m", message, cwd=self.repo, env=env)
        return hashlib.md5(data).hexdigest()

    def test_returns_all_matching_commits_in_reverse_chronological_order(self):
        result = self.run_cmd(
            "python3",
            str(SCRIPT),
            "-p",
            str(self.lib_path),
            "-m",
            self.md5_a,
        )

        self.assertEqual(result.returncode, 0)
        self.assertIn("Matches found: 2", result.stdout)
        self.assertIn(self.md5_a, result.stdout)
        self.assertNotIn(self.md5_b, result.stdout)
        self.assertLess(result.stdout.index("commit-c"), result.stdout.index("commit-a"))

    def test_returns_non_zero_when_no_commit_matches(self):
        result = self.run_cmd(
            "python3",
            str(SCRIPT),
            "-p",
            str(self.lib_path),
            "-m",
            "ffffffffffffffffffffffffffffffff",
            check=False,
        )

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("No matching commits found", result.stderr)


if __name__ == "__main__":
    unittest.main()

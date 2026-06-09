# monky

Android monkey 压力测试工具，内置白名单 `blacklist.txt`。

## Usage

```
monky [-s <serial>] [-h]
```

## Options

| Option | Description |
|--------|-------------|
| `-s <serial>` | 指定设备序列号（默认: `33a415f2a1f`） |
| `-h` | 显示帮助信息 |

## Examples

```bash
# 使用默认设备序列号
monky

# 指定设备
monky -s 12345abcde
```

## 说明

- `blacklist.txt` 与脚本同目录，启动时自动 push 到 `/data/local/tmp/`
- 运行前执行 `adb root` + `adb remount`
- 无限循环，使用当天日期作为随机种子

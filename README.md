# VPDataset

[English](README_en.md) | [日本語](README_ja.md) | 中文

Voicepeak 语音数据集生成工具，用于自动化产出 WAV 语音文件。

## 环境要求

- Python 3.8+
- [VOICEPEAK](https://www.ah-soft.com/voice/index.html) 已安装

## 快速开始

### 查询角色与情感参数

```powershell
# 列出所有可用角色
python CLI.py --list-narrator

# 列出指定角色的情感参数
python CLI.py --list-emotion "Miyamai Moca"

# 切换界面语言（支持 zh / en / ja，默认 zh）
python CLI.py --locale en --help
```

### 批量生成

```powershell
python CLI.py \
  -i input.txt \
  -n "Miyamai Moca" \
  -e "honwaka=40,teary=10,bosoboso=5" \
  --speed 90
```

输入文件为纯文本，**一行一句**。

## CLI 参数

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `--voicepeak-path` | voicepeak 可执行文件路径 | `D:\Voicepeak\Voicepeak\voicepeak.exe` |
| `-i` / `--input` | 输入文本文件 | — |
| `-o` / `--output-dir` | WAV 输出目录 | `output` |
| `--list-file` | 标注文件路径 | — |
| `-n` / `--narrator` | 角色名称 | — |
| `-e` / `--emotion` | 情感表达式 | — |
| `--speed` | 语速（50–200） | — |
| `--pitch` | 音调（-300–300） | — |
| `--prefix` | 输出文件名前缀 | `voice` |
| `--speaker` | 标注中的说话人标签 | `narrator` |
| `--lang` | 标注中的语言标签 | `ja` |
| `--list-narrator` | 列出可用角色 | — |
| `--list-emotion` | 列出指定角色的情感参数 | — |
| `--locale` | 界面语言（`zh` / `en` / `ja`） | `zh` |

## 输出格式

### WAV 文件

按 `{prefix}_{序号}.wav` 命名，如 `voice_0000.wav`、`voice_0001.wav`。

### 标注文件（`.list`）

每行一条：

```
音频路径|说话人|语言|文本
output/voice_0000.wav|narrator|ja|こんにちは、世界！
```

## 致谢

CLI 设计参考了 [voicepeak-cli](https://github.com/petamorikei/voicepeak-cli)。

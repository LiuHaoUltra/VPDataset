# VPDataset

[English](README_en.md) | 日本語 | [中文](README.md)

Voicepeak 音声データセット生成ツール。WAV 音声ファイルの自動生成を行います。

## 動作環境

- Python 3.8+
- [VOICEPEAK](https://www.ah-soft.com/voice/index.html) インストール済み

## クイックスタート

### ナレーター・感情パラメータの確認

```powershell
# 利用可能なナレーター一覧
python CLI.py --list-narrator

# 指定ナレーターの感情パラメータ一覧
python CLI.py --list-emotion "Miyamai Moca"

# UI言語の切り替え（zh / en / ja、デフォルト: zh）
python CLI.py --locale ja --help
```

### 一括生成

```powershell
python CLI.py \
  -i input.txt \
  -n "Miyamai Moca" \
  -e "honwaka=40,teary=10,bosoboso=5" \
  --speed 90
```

入力ファイルはプレーンテキストで、**1行1文**。

## CLI オプション

| オプション | 説明 | デフォルト |
|------------|------|------------|
| `--voicepeak-path` | voicepeak 実行ファイルのパス | `D:\Voicepeak\Voicepeak\voicepeak.exe` |
| `-i` / `--input` | 入力テキストファイル | — |
| `-o` / `--output-dir` | WAV 出力ディレクトリ | `output` |
| `--list-file` | アノテーションファイルのパス（省略するとアノテーションを生成しない） | `slicer_opt.list` |
| `-n` / `--narrator` | ナレーター名 | — |
| `-e` / `--emotion` | 感情表現式 | — |
| `--speed` | 速度（50–200） | — |
| `--pitch` | ピッチ（-300–300） | — |
| `--prefix` | 出力ファイル名の接頭辞 | `voice` |
| `--speaker` | アノテーション内の話者ラベル | `narrator` |
| `--lang` | アノテーション内の言語ラベル | `JA` |
| `--list-narrator` | 利用可能なナレーター一覧 | — |
| `--list-emotion` | 指定ナレーターの感情一覧 | — |
| `--locale` | UI言語（`zh` / `en` / `ja`） | `zh` |

## 出力形式

### WAV ファイル

`{prefix}_{連番}.wav` の形式（例：`voice_0000.wav`、`voice_0001.wav`）。

### アノテーションファイル（`.list`）

1行1エントリ：

```
音声パス|話者|言語|テキスト
output/voice_0000.wav|narrator|ja|こんにちは、世界！
```

## 謝辞

CLI の設計は [voicepeak-cli](https://github.com/petamorikei/voicepeak-cli) を参考にしました。

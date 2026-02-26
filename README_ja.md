# VPDataset

[English](README_en.md) | 日本語 | [中文](README.md)

Voicepeak 音声データセット生成ツール。WAV 音声ファイルの自動生成を行います。

## 動作環境

- Python 3.8+
- [VOICEPEAK](https://www.ah-soft.com/voicepeak/) インストール済み

## クイックスタート

### ナレーター・感情パラメータの確認

```powershell
# 利用可能なナレーター一覧
python CLI.py --list-narrator

# 指定ナレーターの感情パラメータ一覧
python CLI.py --list-emotion 宮舞モカ

# UI言語の切り替え（zh / en / ja、デフォルト: zh）
python CLI.py --locale ja --help
```

### 一括生成

```powershell
python CLI.py \
  -i moca_script.txt \
  -o D:\Moca_Dataset\wavs \
  --list-file D:\Moca_Dataset\moca_training.list \
  -n 宮舞モカ \
  -e "mellow=40,teary=10,mumble=5" \
  --speed 90
```

入力ファイルはプレーンテキストで、**1行1文**（`moca_script.txt` を参照）。

## CLI オプション

| オプション | 説明 | デフォルト |
|------------|------|------------|
| `--voicepeak-path` | voicepeak 実行ファイルのパス | `D:\Voicepeak\Voicepeak\voicepeak.exe` |
| `-i` / `--input` | 入力テキストファイル | — |
| `-o` / `--output-dir` | WAV 出力ディレクトリ | — |
| `--list-file` | アノテーションファイルパス | — |
| `-n` / `--narrator` | ナレーター名 | — |
| `-e` / `--emotion` | 感情表現式 | — |
| `--speed` | 速度（50–200） | — |
| `--pitch` | ピッチ（-300–300） | — |
| `--prefix` | 出力ファイル名の接頭辞 | `moca` |
| `--speaker` | アノテーション内の話者ラベル | `moca_gentle` |
| `--lang` | アノテーション内の言語ラベル | `ja` |
| `--list-narrator` | 利用可能なナレーター一覧 | — |
| `--list-emotion` | 指定ナレーターの感情一覧 | — |
| `--locale` | UI言語（`zh` / `en` / `ja`） | `zh` |

## 出力形式

### WAV ファイル

`{prefix}_{連番}.wav` の形式（例：`moca_0000.wav`、`moca_0001.wav`）。

### アノテーションファイル（`.list`）

1行1エントリ：

```
音声パス|話者|言語|テキスト
D:\Moca_Dataset\wavs\moca_0000.wav|moca_gentle|ja|ある農場にたくさんの動物たちが住んでいました。
```

## 謝辞

CLI の設計は [voicepeak-cli](https://github.com/petamorikei/voicepeak-cli) を参考にしました。

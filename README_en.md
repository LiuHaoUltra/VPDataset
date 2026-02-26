# VPDataset

[English](README_en.md) | [日本語](README_ja.md) | [中文](README.md)

A voice dataset generation tool for Voicepeak, automating WAV audio file production.

## Requirements

- Python 3.8+
- [VOICEPEAK](https://www.ah-soft.com/voice/index.html) installed

## Quick Start

### Query Narrators & Emotions

```powershell
# List all available narrators
python CLI.py --list-narrator

# List emotion parameters for a specific narrator
python CLI.py --list-emotion 宮舞モカ

# Switch UI language (zh / en / ja, default: zh)
python CLI.py --locale en --help
```

### Batch Generation

```powershell
python CLI.py \
  -i input.txt \
  -n 宮舞モカ \
  -e "mellow=40,teary=10,mumble=5" \
  --speed 90
```

Input file is plain text, **one sentence per line**.

## CLI Options

| Option | Description | Default |
|--------|-------------|---------|
| `--voicepeak-path` | Path to voicepeak executable | `D:\Voicepeak\Voicepeak\voicepeak.exe` |
| `-i` / `--input` | Input text file | — |
| `-o` / `--output-dir` | WAV output directory | `output` |
| `--list-file` | Annotation file path | — |
| `-n` / `--narrator` | Narrator name | — |
| `-e` / `--emotion` | Emotion expression | — |
| `--speed` | Speed (50–200) | — |
| `--pitch` | Pitch (-300–300) | — |
| `--prefix` | Output filename prefix | `voice` |
| `--speaker` | Speaker label in annotation | `narrator` |
| `--lang` | Language label in annotation | `ja` |
| `--list-narrator` | List available narrators | — |
| `--list-emotion` | List emotions for a narrator | — |
| `--locale` | UI language (`zh` / `en` / `ja`) | `zh` |

## Output Format

### WAV Files

Named as `{prefix}_{index}.wav`, e.g. `voice_0000.wav`, `voice_0001.wav`.

### Annotation File (`.list`)

One entry per line:

```
audio_path|speaker|language|text
output/voice_0000.wav|narrator|ja|こんにちは、世界！
```

## Acknowledgements

CLI design inspired by [voicepeak-cli](https://github.com/petamorikei/voicepeak-cli).

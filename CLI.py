"""Voicepeak 批量语音数据集生成工具 / Voice Dataset Generator / 音声データセット生成ツール"""

import argparse
import os
import subprocess
import sys

# ─── 默认路径 ───
DEFAULT_EXE = r"D:\Voicepeak\Voicepeak\voicepeak.exe"

# ─── 三语文案 ───
MESSAGES = {
    "zh": {
        "desc": "Voicepeak 批量语音数据集生成工具",
        "voicepeak_path": "voicepeak 可执行文件路径",
        "input": "输入文本文件（一行一句）",
        "output_dir": "WAV 输出目录",
        "list_file": "标注文件输出路径",
        "narrator": '角色名称（如 "宮舞モカ"）',
        "emotion": '情感表达式（如 "mellow=40,teary=10,mumble=5"）',
        "speed": "语速（50-200）",
        "pitch": "音调（-300 到 300）",
        "prefix": "文件名前缀",
        "speaker": "标注文件中的说话人标签",
        "lang_label": "语言标签",
        "list_narrator": "列出可用角色",
        "list_emotion": "列出指定角色的情感参数",
        "locale": "界面语言：zh / en / ja",
        "err_input": "批量生成模式需要 --input / -i 参数",
        "err_output": "批量生成模式需要 --output-dir / -o 参数",
        "err_narrator": "批量生成模式需要 --narrator / -n 参数",
        "err_empty": "输入文件为空或无有效文本",
        "start": "共 {n} 条文本，开始批量生成...",
        "progress": "进度: {done}/{total}",
        "fail": "[失败] 第 {i} 条: {text} — {err}",
        "done": "\n处理完毕！成功: {s} / 失败: {f} / 总计: {t}",
    },
    "en": {
        "desc": "Voicepeak voice dataset batch generator",
        "voicepeak_path": "Path to voicepeak executable",
        "input": "Input text file (one sentence per line)",
        "output_dir": "WAV output directory",
        "list_file": "Annotation file output path",
        "narrator": 'Narrator name (e.g. "宮舞モカ")',
        "emotion": 'Emotion expression (e.g. "mellow=40,teary=10,mumble=5")',
        "speed": "Speed (50-200)",
        "pitch": "Pitch (-300 to 300)",
        "prefix": "Output filename prefix",
        "speaker": "Speaker label in annotation",
        "lang_label": "Language label",
        "list_narrator": "List available narrators",
        "list_emotion": "List emotion parameters for a narrator",
        "locale": "UI language: zh / en / ja",
        "err_input": "Batch mode requires --input / -i",
        "err_output": "Batch mode requires --output-dir / -o",
        "err_narrator": "Batch mode requires --narrator / -n",
        "err_empty": "Input file is empty or contains no valid text",
        "start": "{n} lines loaded, starting batch generation...",
        "progress": "Progress: {done}/{total}",
        "fail": "[FAIL] #{i}: {text} — {err}",
        "done": "\nDone! Success: {s} / Failed: {f} / Total: {t}",
    },
    "ja": {
        "desc": "Voicepeak 音声データセット一括生成ツール",
        "voicepeak_path": "voicepeak 実行ファイルのパス",
        "input": "入力テキストファイル（1行1文）",
        "output_dir": "WAV 出力ディレクトリ",
        "list_file": "アノテーションファイル出力パス",
        "narrator": 'ナレーター名（例: "宮舞モカ"）',
        "emotion": '感情表現式（例: "mellow=40,teary=10,mumble=5"）',
        "speed": "速度（50-200）",
        "pitch": "ピッチ（-300〜300）",
        "prefix": "出力ファイル名の接頭辞",
        "speaker": "アノテーション内の話者ラベル",
        "lang_label": "言語ラベル",
        "list_narrator": "利用可能なナレーター一覧を表示",
        "list_emotion": "指定ナレーターの感情パラメータ一覧を表示",
        "locale": "UI言語: zh / en / ja",
        "err_input": "一括生成モードには --input / -i が必要です",
        "err_output": "一括生成モードには --output-dir / -o が必要です",
        "err_narrator": "一括生成モードには --narrator / -n が必要です",
        "err_empty": "入力ファイルが空か有効なテキストがありません",
        "start": "{n} 行を読み込みました。一括生成を開始します...",
        "progress": "進捗: {done}/{total}",
        "fail": "[失敗] {i}番目: {text} — {err}",
        "done": "\n完了！成功: {s} / 失敗: {f} / 合計: {t}",
    },
}


def get_locale():
    """从 sys.argv 预扫描 --locale 参数"""
    for i, arg in enumerate(sys.argv):
        if arg == "--locale" and i + 1 < len(sys.argv):
            return sys.argv[i + 1]
        if arg.startswith("--locale="):
            return arg.split("=", 1)[1]
    return "zh"


def build_parser(msg):
    parser = argparse.ArgumentParser(description=msg["desc"])
    parser.add_argument("--voicepeak-path", default=DEFAULT_EXE, help=msg["voicepeak_path"])
    parser.add_argument("-i", "--input", help=msg["input"])
    parser.add_argument("-o", "--output-dir", default="output", help=msg["output_dir"])
    parser.add_argument("--list-file", help=msg["list_file"])
    parser.add_argument("-n", "--narrator", help=msg["narrator"])
    parser.add_argument("-e", "--emotion", help=msg["emotion"])
    parser.add_argument("--speed", type=int, help=msg["speed"])
    parser.add_argument("--pitch", type=int, help=msg["pitch"])
    parser.add_argument("--prefix", default="voice", help=msg["prefix"])
    parser.add_argument("--speaker", default="narrator", help=msg["speaker"])
    parser.add_argument("--lang", default="ja", help=msg["lang_label"])
    parser.add_argument("--list-narrator", action="store_true", help=msg["list_narrator"])
    parser.add_argument("--list-emotion", metavar="NARRATOR", help=msg["list_emotion"])
    parser.add_argument("--locale", default="zh", choices=["zh", "en", "ja"], help=msg["locale"])
    return parser


def list_narrator(exe):
    result = subprocess.run([exe, "--list-narrator"], capture_output=True, text=True)
    print(result.stdout, end="")


def list_emotion(exe, narrator):
    result = subprocess.run([exe, "--list-emotion", narrator], capture_output=True, text=True)
    print(result.stdout, end="")


def generate(exe, text, narrator, output, emotion=None, speed=None, pitch=None):
    cmd = [exe, "-s", text, "-n", narrator, "-o", output]
    if emotion:
        cmd += ["-e", emotion]
    if speed is not None:
        cmd += ["--speed", str(speed)]
    if pitch is not None:
        cmd += ["--pitch", str(pitch)]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def main():
    locale = get_locale()
    msg = MESSAGES.get(locale, MESSAGES["zh"])
    parser = build_parser(msg)
    args = parser.parse_args()

    if args.list_narrator:
        list_narrator(args.voicepeak_path)
        return

    if args.list_emotion:
        list_emotion(args.voicepeak_path, args.list_emotion)
        return

    # 校验必要参数
    if not args.input:
        parser.error(msg["err_input"])
    if not args.narrator:
        parser.error(msg["err_narrator"])

    os.makedirs(args.output_dir, exist_ok=True)

    with open(args.input, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]

    if not lines:
        print(msg["err_empty"], file=sys.stderr)
        sys.exit(1)

    list_writer = open(args.list_file, "w", encoding="utf-8") if args.list_file else None

    print(msg["start"].format(n=len(lines)))

    success, fail = 0, 0

    try:
        for index, text in enumerate(lines):
            wav_name = f"{args.prefix}_{index:04d}.wav"
            wav_path = os.path.join(args.output_dir, wav_name)

            try:
                generate(args.voicepeak_path, text, args.narrator, wav_path,
                         emotion=args.emotion, speed=args.speed, pitch=args.pitch)
                success += 1

                if list_writer:
                    list_writer.write(f"{wav_path}|{args.speaker}|{args.lang}|{text}\n")

                if (index + 1) % 50 == 0:
                    print(msg["progress"].format(done=index + 1, total=len(lines)))

            except subprocess.CalledProcessError as e:
                fail += 1
                print(msg["fail"].format(i=index, text=text, err=e), file=sys.stderr)
    finally:
        if list_writer:
            list_writer.close()

    print(msg["done"].format(s=success, f=fail, t=len(lines)))


if __name__ == "__main__":
    main()
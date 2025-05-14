# Gemini Audio Transcriber

Gemini APIを利用した日本語音声の文字起こしPythonスクリプトです。

## Requirements

- Python 3.11+
- Google Gemini API Key

## Setup

1. クローンする

    ```bash
    git clone https://github.com/k-2480/gemini-audio-transcriber.git
    cd gemini-audio-transcriber
    ```

2. Python仮想環境を有効化

    ```bash
    python -m venv env
    source env/Scripts/activate
    ```

3. 依存パッケージのインストール

    ```bash
    pip install -r requirements.txt
    ```

4. `.env`ファイルの作成

    ```bash
    cp .env.example .env
    ```

    この`.env`に自分のGemini APIキーを設定します。キーがなければ取得してください。

## Usage

```bash
python gemini_transcribe.py --input 入力音声ファイル.wav --output 出力ファイル.txt
```

- `--input`: 音声ファイル（例: example.wav）
- `--output`: 文字起こし結果保存先（例: example.txt）

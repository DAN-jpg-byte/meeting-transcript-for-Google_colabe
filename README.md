# 🎙️ 長時間会議 自動文字起こし・議事録作成システム

税理士・弁護士・コンサルタントなどとの長時間ミーティング音声を、Google Colab上で自動的に文字起こし・話者分離し、対話形式の議事録としてNotionに出力するシステムです。

---

## 📋 できること

- 🎙️ **音声の文字起こし**（WhisperX / large-v3モデル）
- 👥 **話者分離**（Gemini AIが誰が話しているか自動識別）
- 🤖 **AI整形**（誤字補正 → 話者分離の2段階処理で精度を担保）
- 📝 **Notionへ自動出力**（日付・参加者情報つきでページ作成）
- 📁 **処理済みファイルの自動整理**（Google Driveのフォルダ間を自動移動）
- 📊 **処理ログの記録**（Googleスプレッドシートに日時・ファイル名・参加者を記録）

---

## 🛠️ 必要なもの

### アカウント・サービス
- Google アカウント（Google Drive / Google Colab / Googleスプレッドシート）
- [Hugging Face](https://huggingface.co/) アカウント（無料）
- [Google AI Studio](https://aistudio.google.com/) アカウント（Gemini APIキー取得用・無料枠あり）
- [Notion](https://www.notion.so/) アカウント + インテグレーション作成済み

### Colabシークレット（3つ）

| シークレット名 | 取得場所 | 説明 |
|---|---|---|
| `GEMINI_API_KEY` | Google AI Studio → APIキーを作成 | 話者分離・テキスト整形に使用 |
| `NOTION_TOKEN` | Notion → 設定 → インテグレーション | Notionへの書き込みに必要 |
| `NOTION_DATABASE_ID` | NotionのデータベースURL内のID | 議事録の保存先DB |

> Colabシークレットの登録方法：左メニューの🔑アイコン → 「新しいシークレットを追加」

### Google Drive フォルダ構成
以下のフォルダをマイドライブに作成してください：

```
MyDrive/
└── MeetingTranscript/
    ├── 01_input/       ← 音声ファイルをここに入れる
    ├── 02_processed/   ← 処理済みファイルが自動移動される
    ├── 03_output/      ← 生テキスト・議事録MDが保存される
    └── 04_temp/        ← 一時ファイル用（自動作成）
```

### Googleスプレッドシート
`MeetingTranscript` という名前のスプレッドシートを作成し、以下のシートを用意してください：

**シート名：本日の参加者**

| 名前 | 役割 | プロフィール |
|---|---|---|
| 山田 太郎 | 税理士 | 〇〇税理士法人所属。法人税・相続税が専門。 |
| 田中 花子 | 社長 | 株式会社△△代表取締役。製造業。 |

---

## 🚀 使い方

### 初回セットアップ（最初の1回だけ）

1. 上記の「必要なもの」をすべて準備する
2. Colabでノートブックを開く
3. **ランタイムをGPUに変更する**
   - 「ランタイム」→「ランタイムのタイプを変更」→「T4 GPU」を選択
4. Step 1を実行してライブラリをインストールする（自動で再起動されます）

### 毎回の使い方

```
1. 音声・動画ファイルを「MeetingTranscript/01_input/」に入れる
   対応形式（音声）: mp3 / m4a / wav / aac / flac / ogg
   対応形式（動画）: mp4 / mov / avi / mkv / webm / wmv
   ※ 大文字拡張子（MP3・MP4等）も対応

2. スプレッドシートの「本日の参加者」を
   今日の参加者に更新する

3. Step 1のセルを実行
   → 完了音が鳴ったら自動で再起動される

4. Step 2のセルを実行
   → ポップアップが出たら「許可」を押す
   → 「🎉 準備完了！あとは待つだけです ☕」が出たらOK

5. 「▶ 現在のセルと以下のすべてのセルを実行」でまとめて実行
   → あとは待つだけ（PCのスリープはオフに！）

6. 完了したらNotionに議事録ページが作成されている
```

> **注意：** PCがスリープするとColabが切断されます。長時間処理中はスリープ設定をオフにしてください。

---

## ⚙️ 設定のカスタマイズ

`notebook.ipynb` の Step2 冒頭にある設定値を変更することで動作を調整できます。

| 変数名 | デフォルト | 説明 |
|---|---|---|
| `GEMINI_MODEL` | `gemini-3.1-flash-lite-preview` | 使用するGeminiモデル（下記参照） |
| `CHUNK_SIZE` | `10000` | Geminiへの分割単位（文字数） |

---

## 📦 使用技術

| ライブラリ | 用途 |
|---|---|
| [WhisperX](https://github.com/m-bain/whisperX) | 音声文字起こし（large-v3モデル） |
| [Google Generative AI](https://ai.google.dev/) | 誤字補正・話者分離（Gemini） |
| [gspread](https://github.com/burnash/gspread) | Googleスプレッドシート操作 |
| Notion API（requests直叩き） | Notionへの議事録出力 |

---

## 🤖 Gemini モデルの選び方

### 現在使用中のモデル
`gemini-3.1-flash-lite-preview`（RPM: 15 / RPD: 500）

### 利用可能なモデル一覧の取得方法

Colabで以下を実行すると、その時点で使えるモデルが確認できます：

```python
import google.generativeai as genai
genai.configure(api_key=GEMINI_API_KEY)

for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(m.name)
```

### テキスト出力モデルの無料枠比較（2026-04-19 時点）

| モデル（API ID） | RPM | RPD | 備考 |
|---|---|---|---|
| `gemini-3.1-flash-lite-preview` | 15 | **500** | ← 現在使用・おすすめ |
| `gemini-2.5-flash-lite` | 10 | 20 | 旧デフォルト |
| `gemini-2.5-flash` | 5 | 20 | |
| `gemini-3-flash-preview` | 5 | 20 | |

> RPM = 1分あたりのリクエスト数 / RPD = 1日あたりのリクエスト数
> レート制限の最新情報は [Google AI Studio](https://aistudio.google.com/rate-limit) で確認できます。

### モデルを変更したいとき

`notebook.ipynb` の Step2 の設定欄を変更するだけです：

```python
GEMINI_MODEL = 'gemini-3.1-flash-lite-preview'  # ← ここを変える
```

---

## ❓ よくあるエラー

| エラー | 原因 | 対処 |
|---|---|---|
| `CUDA driver version is insufficient` | GPUランタイムになっていない | ランタイムのタイプをT4 GPUに変更 |
| `❌ 以下のシークレットが未登録です` | Colabシークレットの登録漏れ | シークレットを確認・登録 |
| `❌ スプレッドシートに参加者情報がありません` | シートが空または名前が違う | シート名「本日の参加者」を確認 |
| `❌ 音声ファイルがありません` | ファイルをDriveに入れていない | `01_input/` に音声ファイルを配置 |
| pip依存関係のERROR（大量） | Colab内部パッケージとの競合 | 無視してOK（動作に影響なし） |

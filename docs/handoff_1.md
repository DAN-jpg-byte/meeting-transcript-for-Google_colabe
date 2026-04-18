# 引き継ぎドキュメント #1

作成日: 2026-04-18

---

## プロジェクト概要

**リポジトリ名:** `meeting-transcript-google-colab`

税理士等との長時間（3〜4時間）のミーティング音声を、Google Colab上で自動文字起こし・話者分離し、対話形式の全文記録としてNotionに出力するシステム。

---

## 現在の状態

### 完了していること
- [x] 要件定義・仕様の確定（`docs/spec.md`）
- [x] ロードマップの作成（`docs/roadmap.md`）
- [x] Colabノートブックの初期実装（`notebook.ipynb`）
  - Step 1: 環境セットアップ
  - Step 2: WhisperXで文字起こし＋話者分離
  - Step 3: スプレッドシートから参加者情報取得
  - Step 4: Geminiで話者特定 → Pythonで置換 → Geminiで整形
  - Step 5: Notionにページ作成
  - Step 6: 後片付け・ログ記録

### まだやっていること
- [ ] GitHubリポジトリの作成・push（ユーザーが自分でやる）
- [ ] 実際の音声ファイルでのテスト実行
- [ ] 事前準備（下記参照）

---

## 重要な仕様決定

### Google Drive 構成
```
MeetingTranscript/
├── 01_input       # 処理前の音声ファイル
├── 02_processed   # 完了した音声の移動先
├── 03_output      # 生成されたテキスト/Markdown
└── 04_management  # スプレッドシート（参加者名簿・処理ログ）
```

### スプレッドシートのレイアウト（シート名：本日の参加者）
| 名前 | 役割 | プロフィール |
|------|------|------------|
| 田中 太郎 | 税理士 | 主に説明する側。専門用語多め |
| 山田 花子 | 依頼者 | 説明を聞く側 |
→ 毎回のミーティング前に書き換えて使う

### 話者置換の方針
- 冒頭**3000文字** + 参加者プロフィール → Geminiで話者特定（JSON形式で返す）
- 全文 → **Pythonで機械的に一括置換**（精度担保のため）
- 置換後 → Geminiで専門用語補正・整形（**1万文字単位**に分割）

### Notionページのフォーマット
- タイトル: `議事録_YYYY-MM-DD`
- プロパティ: 日付、参加者
- 本文: 対話形式・全文（要約なし）
  ```
  田中: 今回の決算についてですが〜〜〜
  山田: それはつまりどういうことですか？
  ```

### APIキーの管理
- Colabのシークレット機能を使用（1回登録すればずっと使える）
- `HF_TOKEN`、`GEMINI_API_KEY`、`NOTION_TOKEN` の3つ

---

## ユーザーの事前準備チェックリスト

- [ ] **Google Drive:** `MeetingTranscript/` フォルダ構成の作成
- [ ] **Hugging Face:** アカウント作成・3つのモデルへの同意・Readトークンの発行
- [ ] **Google AI Studio:** Gemini APIキーの発行
- [ ] **スプレッドシート:** 参加者名簿シートの作成（`04_management` 内）
- [ ] **Notion:** インテグレーション作成・データベースIDの取得
- [ ] **Colab シークレット:** `HF_TOKEN`・`GEMINI_API_KEY`・`NOTION_TOKEN` を登録
- [ ] **notebook.ipynb の設定セル:** `NOTION_DATABASE_ID` を自分のIDに書き換える

---

## 次のタスク

1. GitHubにリポジトリ（`meeting-transcript-google-colab`）を作成してpush
2. 上記の事前準備を完了させる
3. 実際の音声ファイルでテスト実行
4. エラーが出たら修正

---

## ファイル構成

```
/workspace/
├── notebook.ipynb     # Colabノートブック（メイン）
└── docs/
    ├── spec.md        # 仕様書
    ├── roadmap.md     # 実装ロードマップ
    └── handoff_1.md   # このファイル
```

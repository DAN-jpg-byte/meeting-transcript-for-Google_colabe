# 引き継ぎドキュメント #2

作成日: 2026-04-18

---

## プロジェクト概要

**リポジトリ名:** `meeting-transcript-google-colab`（GitHub パブリック）

税理士等との長時間ミーティング音声を、Google Colab上で自動文字起こし・話者分離し、対話形式の全文記録としてNotionに出力するシステム。

---

## 現在の状態

### 完了していること
- [x] GitHubリポジトリ作成・push済み（パブリック）
- [x] Colabノートブックの実装（`notebook.ipynb`）
- [x] Colabシークレット登録（HF_TOKEN / GEMINI_API_KEY / NOTION_TOKEN）
- [x] Google Drive フォルダ構成作成（MeetingTranscript/01〜04）
- [x] Googleスプレッドシート作成（MeetingTranscript / シート名：本日の参加者）
- [x] Notion データベース作成・インテグレーション接続済み
- [x] NOTION_DATABASE_ID をノートブックに設定済み（43a5556c027349d18a35aafac5b54847）

### テスト実行中に解消したエラー
- whisperx の `DiarizationPipeline` → `from whisperx.diarize import DiarizationPipeline` に修正
- `use_auth_token` → `token` に修正
- Google Sheets 認証 → `google.colab.auth.authenticate_user()` に修正
- Notionプロパティ → 日付・参加者を本文冒頭に移動（プロパティはタイトルのみ）

### 未解決・次のタスク
- [ ] **Geminiモデル名の確定**
  - `gemini-2.0-flash` → 無料枠0で使えなかった
  - `gemini-2.5-flash` を設定済み（未テスト）
  - 動かなければ他のモデルIDを試す
  - Google AI Studioで正しいモデルIDを確認するのが確実

---

## 重要な仕様決定

- Notionページのプロパティはタイトルのみ（日付・参加者は本文冒頭に記載）
- Gemini モデルは無料枠があるものを使う
- Colabのシークレット機能でAPIキーを管理（コードに直書きしない）
- コードの更新があったときのみ「GitHubからノートブックを開き直す」運用

## レート制限メモ（2026-04-18時点）
無料枠があるモデル（表示名）：
- Gemini 2.5 Flash：RPD=20
- Gemini 2.5 Flash Lite：RPD=20
- Gemini 3 Flash：RPD=20
- Gemini 3.1 Flash Lite：RPD=500（最多）
※APIモデルIDは表示名と異なる可能性あり。要確認。

---

## ファイル構成

```
/workspace/
├── notebook.ipynb     # Colabノートブック（メイン）
└── docs/
    ├── spec.md
    ├── roadmap.md
    ├── handoff_1.md
    └── handoff_2.md   # このファイル
```

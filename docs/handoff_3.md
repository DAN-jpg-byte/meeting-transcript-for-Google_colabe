# 引き継ぎドキュメント #3

作成日: 2026-04-18
更新日: 2026-04-18

---

## プロジェクト概要

**リポジトリ名:** `meeting-transcript-google-colab`（GitHub パブリック）

税理士等との長時間ミーティング音声を、Google Colab上で自動文字起こし・話者分離し、対話形式の全文記録としてNotionに出力するシステム。

---

## 現在の状態

### 完了していること
- [x] GitHubリポジトリ作成・push済み（パブリック）
- [x] Colabノートブックの実装（`notebook.ipynb`）
- [x] Colabシークレット登録（HF_TOKEN / GEMINI_API_KEY / NOTION_TOKEN / NOTION_DATABASE_ID）
- [x] Google Drive フォルダ構成作成（MeetingTranscript/01〜04）
- [x] Googleスプレッドシート作成（MeetingTranscript / シート名：本日の参加者）
- [x] Notion データベース作成・インテグレーション接続済み
- [x] Geminiモデルを `gemini-2.5-flash-lite` に設定
- [x] Notion連携を `notion-client` → `requests` ライブラリに変更
- [x] NOTION_DATABASE_ID をColabシークレット経由に変更（ハードコードを廃止）
- [x] **Notion連携の動作確認完了**（ページ作成・ブロック追記129件 成功）
- [x] Gemini整形プロンプト改善（シンプル形式：太字・役職なし）
- [x] 全認証処理をStep2にまとめ（Fail Fast設計・あとは放置できる）
- [x] タイトルセルにバージョン番号を追加（version: 1.4 / 2026-04-18）
- [x] すべてGitにコミット済み・GitHubにpush済み

### 最新コミット履歴
```
83e9d05 docs: タイトルにバージョン番号を追加
5166f84 refactor: 全認証をStep2にまとめ、セル構成を整理
90e623b 不要なもの削除
b588e8e fix: Gemini整形プロンプトを改善（シンプル形式・太字禁止）
3ab56d9 docs: handoff_2を最新状態に更新
```

### 未解決・次のタスク
- [ ] 実際の音声ファイルで全ステップ通しテスト
- [ ] `gemini-2.5-flash-lite` の動作確認（APIモデルIDが正しいか）

---

## ノートブック構成（notebook.ipynb v1.4）

| セル | 内容 |
|------|------|
| cell-0 | タイトル・バージョン（マークダウン） |
| cell-1/2 | Step1: pip install（whisperx, google-generativeai, gspread 等） |
| cell-3/4 | **Step2: 全認証まとめ**（Drive・Sheets・Gemini・Notion・音声確認） |
| cell-6/8/9/10 | Step3: WhisperX 文字起こし・話者分離・名前置換 |
| cell-13/14/15/16 | Step4: Gemini で整形 |
| cell-17/18 | Step5: Notion出力 |
| cell-20/21 | Step6: 後片付け |

### Step2（全認証）の設計思想
- **Fail Fast**：最初に全認証・疎通確認 → 失敗したらここで止まる
- 完了後に `🎉 準備完了！あとは待つだけです ☕` を表示
- 認証対象：HF_TOKEN / GEMINI_API_KEY / NOTION_TOKEN / NOTION_DATABASE_ID / Drive / Sheets / Notion DB

---

## 重要な仕様決定

- Notionページのプロパティはタイトルのみ（日付・参加者は本文冒頭に記載）
- Notion DBのタイトルプロパティ名は **`名前`**（`タイトル`は誤り）
- Gemini モデルは無料枠があるものを使う（現在: `gemini-2.5-flash-lite`）
- Colabのシークレット機能でAPIキーを管理（コードに直書きしない）
  - 管理するシークレット：HF_TOKEN / GEMINI_API_KEY / NOTION_TOKEN / NOTION_DATABASE_ID
  - NOTION_DATABASE_ID の値：`43a5556c027349d18a35aafac5b54847`
- Notion API は `requests` ライブラリで直叩き
  - ページ作成：`POST /v1/pages`
  - ブロック追記：`PATCH /v1/blocks/{id}/children`（POSTではなくPATCH）
- Gemini整形プロンプト：`名前：発言内容` 形式、太字禁止、役職禁止、Markdown禁止
- コードの更新があったときのみ「GitHubからノートブックを開き直す」運用

## レート制限メモ（2026-04-18時点）
無料枠があるモデル（表示名）：
- Gemini 2.5 Flash：RPD=20
- Gemini 2.5 Flash Lite：RPD=20（← 現在使用中）
- Gemini 3 Flash：RPD=20
- Gemini 3.1 Flash Lite：RPD=500（最多）
※APIモデルIDは表示名と異なる可能性あり。要確認。

---

## 過去に解消したエラー（参考）

| エラー | 原因 | 対応 |
|--------|------|------|
| `notion-client` が動かない | ライブラリ非互換 | `requests` 直叩きに変更 |
| `invalid_request_url` (1回目) | エラー詳細不明 | HTTPErrorキャッチしてレスポンスボディ表示 |
| `invalid_request_url` (2回目) | プロパティ名 `タイトル`→`名前` | 診断セルでDB構造確認 |
| `invalid_request_url` (3回目) | ブロック追記にPOSTを使用 | PATCHに変更 → 129件成功 |
| Gemini出力に太字・役職が付く | プロンプト不足 | 明示ルールを追加 |
| WhisperX `DiarizationPipeline` import失敗 | パス変更 | `from whisperx.diarize import DiarizationPipeline` |
| `use_auth_token` エラー | 引数名変更 | `token` に修正 |
| Google Sheets 認証失敗 | 認証方法変更 | `google.colab.auth.authenticate_user()` に修正 |

---

## ファイル構成

```
/workspace/
├── notebook.ipynb        # Colabノートブック（メイン・v1.4）
├── sample/               # 過去のNotion連携実装サンプル（urllib直叩きの参考元）
│   ├── utils.py
│   ├── fetch_tasks.py
│   └── ...
└── docs/
    ├── spec.md
    ├── roadmap.md
    ├── handoff_1.md
    ├── handoff_2.md
    └── handoff_3.md      # このファイル
```

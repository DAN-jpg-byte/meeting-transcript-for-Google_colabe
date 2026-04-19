# 引き継ぎドキュメント #4

作成日: 2026-04-18
更新日: 2026-04-19

---

## プロジェクト概要

**リポジトリ名:** `meeting-transcript-for-Google_colabe`（GitHub パブリック）

税理士等との長時間ミーティング音声を、Google Colab上で自動文字起こし・話者分離し、対話形式の全文記録としてNotionに出力するシステム。

---

## 現在の状態（v2.0）

### 完了していること
- [x] GitHubリポジトリ作成・push済み（パブリック）
- [x] Colabノートブックの実装（`notebook.ipynb`）
- [x] Colabシークレット登録（GEMINI_API_KEY / NOTION_TOKEN / NOTION_DATABASE_ID）
- [x] Google Drive フォルダ構成作成（MeetingTranscript/01〜04）
- [x] Googleスプレッドシート作成（MeetingTranscript / シート名：本日の参加者）
- [x] Notion データベース作成・インテグレーション接続済み
- [x] Notion連携を `notion-client` → `requests` ライブラリに変更
- [x] NOTION_DATABASE_ID をColabシークレット経由に変更（ハードコードを廃止）
- [x] 全認証処理をStep2にまとめ（Fail Fast設計・あとは放置できる）
- [x] Step1インストールをuv化・完了音通知を追加
- [x] **実際の音声ファイルで全ステップ通しテスト完了**
- [x] README.md作成・v2.0に更新済み
- [x] **v1.0.0 タグ作成・push済み（2026-04-19）**
- [x] **v2.0 実装完了・push済み（2026-04-19）**

### v2.0 の主な変更点
- **WhisperX の話者分離（diarization）を廃止** → 精度が低かったため
- **Gemini の処理を2段階に分離**（精度向上のため）
  - Step 4a：誤字補正のみ（話者は気にしない）
  - Step 4b：話者分離のみ（きれいなテキストで精度アップ）
- **HF_TOKEN 不要になった**（話者分離を Gemini に移行したため）
- **音声・動画ファイル対応を拡張**（mp4/mov/avi/mkv/webm/wmv 等・大文字小文字両対応）
- **Gemini モデルを `gemini-3.1-flash-lite-preview` に変更**（RPD: 20 → 500）

### 追加で完了したこと（2026-04-19後半）
- [x] Gemini モデル候補をコメントアウトで列挙（切り替えやすく）
- [x] Step2 の認証ポップアップ時に通知音を追加
- [x] 音声・動画ファイル対応を拡張（mp4/mov/avi/mkv等・大文字小文字両対応）
- [x] スリープ注意をノートブック冒頭とマニュアルに追記
- [x] Notion 貼り付け用の運用マニュアル作成（`docs/notion_manual.md`）
- [x] **v2.0.0 タグ作成・push済み**

### 未解決・次のタスク
- [ ] 長時間音声（実際の税理士ミーティング）での通しテスト
- [ ] RPM制限（15回/分）に引っかかる場合はチャンク間に待ち時間を追加
- [ ] 定期的な運用で問題が出ないか様子見

---

## ノートブック構成（notebook.ipynb v2.0）

| セル | 内容 |
|------|------|
| cell-0 | タイトル・バージョン（マークダウン） |
| cell-1/2 | Step1: uv + pip install（whisperx, google-generativeai, gspread 等） |
| cell-3/4 | **Step2: 全認証まとめ**（Drive・Sheets・Gemini・Notion・ファイル確認） |
| cell-6/8/10 | Step3: WhisperX 文字起こしのみ（話者分離なし） |
| cell-13/14 | Step4a: Gemini で誤字補正（話者は気にしない） |
| cell-15 | Step4b: Gemini で話者分離（きれいなテキストで特定） |
| cell-17/18 | Step5: Notion出力 |
| cell-20/21 | Step6: 後片付け |

---

## 重要な仕様決定

- Notionページのプロパティはタイトルのみ（日付・参加者は本文冒頭に記載）
- Notion DBのタイトルプロパティ名は **`名前`**（`タイトル`は誤り）
- Gemini モデルは無料枠があるものを使う（現在: `gemini-3.1-flash-lite-preview`）
- Colabのシークレット機能でAPIキーを管理（コードに直書きしない）
  - 管理するシークレット：GEMINI_API_KEY / NOTION_TOKEN / NOTION_DATABASE_ID
  - NOTION_DATABASE_ID の値：`43a5556c027349d18a35aafac5b54847`
- Notion API は `requests` ライブラリで直叩き
  - ページ作成：`POST /v1/pages`
  - ブロック追記：`PATCH /v1/blocks/{id}/children`（POSTではなくPATCH）
- Gemini への入力は1万文字ずつ分割（CHUNK_SIZE=10000）
- コードの更新があったときのみ「GitHubからノートブックを開き直す」運用

## Gemini モデル情報（2026-04-19時点）

利用可能モデルの取得方法：
```python
import google.generativeai as genai
genai.configure(api_key=GEMINI_API_KEY)
for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(m.name)
```

テキスト出力モデルの無料枠：
| モデル（API ID） | RPM | RPD |
|---|---|---|
| `gemini-3.1-flash-lite-preview` | 15 | **500**（← 現在使用） |
| `gemini-2.5-flash-lite` | 10 | 20 |
| `gemini-2.5-flash` | 5 | 20 |

---

## 過去に解消したエラー（参考）

| エラー | 原因 | 対応 |
|--------|------|------|
| `notion-client` が動かない | ライブラリ非互換 | `requests` 直叩きに変更 |
| `invalid_request_url` (1回目) | エラー詳細不明 | HTTPErrorキャッチしてレスポンスボディ表示 |
| `invalid_request_url` (2回目) | プロパティ名 `タイトル`→`名前` | 診断セルでDB構造確認 |
| `invalid_request_url` (3回目) | ブロック追記にPOSTを使用 | PATCHに変更 → 129件成功 |
| Gemini出力に太字・役職が付く | プロンプト不足 | 明示ルールを追加 |
| `CUDA driver version is insufficient` | CPUランタイムで実行 | T4 GPUランタイムに変更 |
| `models/gemini-3.1-flash-lite is not found` | API IDが違った | `-preview` を付けて `gemini-3.1-flash-lite-preview` に修正 |

---

## ファイル構成

```
/workspace/
├── notebook.ipynb        # Colabノートブック（メイン・v2.0）
├── README.md             # プロジェクト説明
├── sample/               # 過去のNotion連携実装サンプル
└── docs/
    ├── spec_v2.md        # 要件定義 v2.0
    ├── roadmap_v2.md     # ロードマップ v2.0
    ├── handoff_1.md〜4.md
    └── handoff_4.md      # このファイル
```

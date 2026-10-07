# ロードマップ：話者分離（pyannote Community-1）の実験

要件: [spec_話者分離実験.md](spec_話者分離実験.md)
ブランチ: `experiment/diarization`（戻り先: タグ `v2.1.0`）

方針: **最初に動くことを優先する。** 小さく作って Colab で動かし、結果を見てから次を足す。
作るファイルは `experiment_diarization.ipynb` だけ。本体の `notebook.ipynb` は変更しない。

---

## Step 0: 準備（手元）

- [ ] spec と roadmap をコミットする
- [ ] Hugging Face で Community-1 の利用条件に同意済みか確認する（ユーザー作業）
  - 未同意なら: `pyannote/speaker-diarization-community-1` のページで同意 → Colab のシークレットに `HF_TOKEN`（Read 権限）を登録

## Step 1: 土台（インストール・認証・音声の用意）

変更ファイル: `experiment_diarization.ipynb`（新規）

- [ ] セル1: インストール（`pyannote.audio` 4.x）。本体と同じく、入れたらランタイムを再起動する
- [ ] セル2: 設定と認証
  - `HF_TOKEN` をシークレットから読む（なければ分かりやすいエラーで止まる）
  - Drive をマウント（Sheets・Notion・Gemini の認証は**しない**）
  - ffmpeg / ffprobe の確認
- [ ] セル3: `01_input` の音声を **コピー**して（移動しない）、16kHz・モノラルの wav に変換し、**音声の長さを表示**する
- ポイント: 入力音声は動かさない・消さない。Colab 側の `/content/work/` に作り、Drive の元は触らない

**完了の目安**: Colab で上から実行して、音声の長さ（分）が表示される。

## Step 2: 条件 A（人数のヒントなし）

- [ ] セル4: Community-1 を読み込み、話者分離を実行（`num_speakers` なし）
- [ ] 表示: 区間一覧（開始秒・終了秒・SPEAKER_xx）、検出人数、話者ごとの発話時間
- [ ] 保存: `04_temp/experiment_diarization/diarization_A.json`
- ポイント: GPU に載せる。処理時間も表示する（長時間音声に伸ばしたときの目安）

**完了の目安**: 人数と区間が表示され、JSON が Drive に残る。

> ここで一度ユーザーに結果を見てもらう。Community-1 が動いたか、人数が2人に近いかで次へ進むか決める。

## Step 3: 条件 B（人数を指定）と比較

- [ ] セル5: `num_speakers=2` で実行 → `diarization_B.json`
- [ ] セル6: A と B を並べて表示（検出人数、発話時間、区間の数、話者が変わる回数）

**完了の目安**: A と B の違いが1画面で見える。

## Step 4: 文字起こしと突き合わせ

- [ ] セル7: WhisperX で文字起こし（単語の時間つき）→ `whisper.json`
  - pyannote と WhisperX の依存関係がぶつかる場合は、別セル・別手順で逃がす（ここで確認する）
- [ ] セル8: 文字起こしの各発言に、時間が一番重なる話者を割り当てる（Python だけの処理）
- [ ] 出力: `SPEAKER_xx：発言` 形式のテキスト（A・B それぞれ）→ `result_A.txt` / `result_B.txt`

**完了の目安**: 会話の形のテキストが2種類できる。

## Step 5: 確認と記録

- [ ] ユーザーが音声と `result_A.txt` / `result_B.txt` を見比べる（spec の「合否の見方」）
- [ ] 結果を `docs/experiment_話者分離_結果.md` に記録（良かった点・悪かった点・A と B の差）
- [ ] 判断: 採用 / 条件を変えてもう一度 / 見送り
  - 採用なら、次の作業（チャンク分割・のりしろ・名前の対応づけ）の spec を別に作る
- [ ] handoff を更新する（`docs/handoff_6.md`）

---

## 気をつけること

- `pyannote.audio` 4.x の呼び出し方（モデル読み込みのトークン引数名など）は、実装時に公式の README で確認する
- WhisperX と pyannote の版がぶつかる可能性がある。Step 1 では pyannote だけ入れて、Step 4 で確認する
- 長さが長い音声（数時間）での確認は、この実験の次の段階（今回はやらない）

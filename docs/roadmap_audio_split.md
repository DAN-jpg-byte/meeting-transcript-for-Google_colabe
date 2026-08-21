# ロードマップ：長時間音声の無音分割機能

作成日: 2026-08-21

要件定義: [spec_audio_split.md](spec_audio_split.md)

---

## Step 1: pydubの追加とインストール確認

- **変更ファイル**: [notebook.ipynb](../notebook.ipynb) cell-2（Step1: ライブラリインストール）
- **実装イメージ**: `uv pip install` の対象に `pydub` を追加する
- **ポイント**: pydubは内部でffmpegを使うが、Colabには標準でffmpegが入っているため追加インストール不要

- [x] 実装
- [ ] Colabで動作確認（importエラーが出ないか）

---

## Step 2: 無音検出→カットポイント算出の関数を実装

- **変更ファイル**: [notebook.ipynb](../notebook.ipynb) Step3内に新規セルを追加（cell-6markdown の後、既存cell-8の前）
- **実装イメージ**:
  ```python
  from pydub import AudioSegment
  from pydub.silence import detect_silence

  def find_cut_point(audio, target_ms, search_windows_ms, min_silence_len=700, silence_thresh=None):
      """target_ms 付近の無音区間の中央をカット点として返す。見つからなければNone"""
      if silence_thresh is None:
          silence_thresh = audio.dBFS - 16
      for window in search_windows_ms:  # [60_000, 120_000, 240_000, ...]
          start = max(0, target_ms - window)
          end = min(len(audio), target_ms + window)
          silent_ranges = detect_silence(
              audio[start:end], min_silence_len=min_silence_len, silence_thresh=silence_thresh
          )
          if silent_ranges:
              # target_ms に一番近い無音区間を選ぶ
              best = min(silent_ranges, key=lambda r: abs((start + (r[0]+r[1])//2) - target_ms))
              return start + (best[0] + best[1]) // 2
      return None
  ```
- **ポイント**: 音量しきい値 `audio.dBFS - 16` は「その音声全体の平均音量より16dB静か」という相対基準。会議室のノイズレベルが違っても自動で追従する

- [x] 実装
- [ ] 短い音声（数分）でカットポイントが妥当な位置に出るかテスト

---

## Step 3: 音声をチャンクに分割して一時保存

- **変更ファイル**: 同上セル
- **実装イメージ**:
  ```python
  import os

  CHUNK_TARGET_MS = 10 * 60 * 1000  # 10分
  SEARCH_WINDOWS_MS = [60_000, 120_000, 240_000, 480_000]
  CHUNK_DIR = '/content/chunks'

  audio_seg = AudioSegment.from_file(audio_path)
  total_ms = len(audio_seg)

  cut_points = [0]
  cursor = CHUNK_TARGET_MS
  while cursor < total_ms:
      cut = find_cut_point(audio_seg, cursor, SEARCH_WINDOWS_MS)
      if cut is None:
          cut = cursor  # 無音が見つからなければ強制カット（採用済み方針）
      cut_points.append(cut)
      cursor = cut + CHUNK_TARGET_MS
  cut_points.append(total_ms)
  cut_points = sorted(set(cut_points))

  os.makedirs(CHUNK_DIR, exist_ok=True)
  chunk_paths = []
  for i in range(len(cut_points) - 1):
      chunk = audio_seg[cut_points[i]:cut_points[i+1]]
      chunk_path = f'{CHUNK_DIR}/chunk_{i:03d}.wav'
      chunk.export(chunk_path, format='wav')
      chunk_paths.append(chunk_path)

  print(f'✅ 音声を {len(chunk_paths)} チャンクに分割しました')
  ```
- **ポイント**: 元の `audio_seg` はチャンク書き出し後は使わないので、メモリ節約のため `del audio_seg` してもよい（長時間音声で気になる場合）

- [x] 実装
- [ ] 60分程度の音声で6個前後のチャンクになるか確認

---

## Step 4: 既存cell-8（WhisperX文字起こし）をチャンクループに変更

- **変更ファイル**: [notebook.ipynb](../notebook.ipynb) cell-8
- **実装イメージ**:
  ```python
  model = whisperx.load_model('large-v3', device, compute_type=compute_type)

  all_segments = []
  for i, chunk_path in enumerate(chunk_paths):
      print(f'🎙️ チャンク {i+1}/{len(chunk_paths)} を文字起こし中...')
      chunk_audio = whisperx.load_audio(chunk_path)
      chunk_result = model.transcribe(chunk_audio, batch_size=4, language='ja')
      all_segments.extend(chunk_result['segments'])
      os.remove(chunk_path)  # 使い終わったら削除

  result = {'segments': all_segments}
  print(f'✅ 文字起こし完了（{len(result["segments"])} セグメント）')
  ```
- **ポイント**: モデルのロードは1回だけ（ループの外）。`result['segments']` の形を維持することで、cell-10は無変更で動く

- [x] 実装
- [ ] cell-10がそのまま動くことを確認（テキスト連結・保存）

---

## Step 5: 通しテスト

- [ ] 実際の長時間音声（1時間以上）で最初から最後まで実行し、クラッシュしないか確認
- [ ] 分割された箇所で発言が不自然に途切れていないか、出力テキストを確認
- [ ] `/content/chunks/` が処理後に空になっている（削除できている）か確認

---

## Step 6: ドキュメント更新

- [ ] [handoff_4.md](handoff_4.md) に実装内容・仕様決定を記録
- [ ] spec_audio_split.md のチェック漏れがないか見直し

"""2つの会話テキスト（正解と出力）を比べて、文字ごとの話者の一致率を出す。
使い方: python -I -X utf8 score_dialogue.py <正解.txt> <出力.txt> [--until 0:05:15]
  --until: 出力のうち、この時刻より後に始まる発言を除く（正解が冒頭だけのとき、同じ範囲に揃えるため）。
           出力に [0:00:10] のような時刻がある場合だけ効く
"""
import re
import sys
from difflib import SequenceMatcher

IGNORE = re.compile(r'[\s。、，．,.?？!！「」『』\[\]()（）・…ー~〜]')  # 句読点・空白・記号は比べない
# 「[0:00:10] SPEAKER_01：」または「SPEAKER_01：」。時刻は無くてもよい
TURN_HEAD = re.compile(r'(?:\[(\d+:\d{2}(?::\d{2})?)\]\s*)?SPEAKER_(\d+)：')


def to_seconds(text):
    # 「0:05:15」「5:15」を秒にする
    seconds = 0
    for num in text.split(':'):
        seconds = seconds * 60 + int(num)
    return seconds


def parse_turns(path, until=None):
    # 「SPEAKER_xx：発言」の形を順番どおりに取り出す（行頭の ] などのごみは無視）
    text = open(path, encoding='utf-8').read()
    parts = TURN_HEAD.split(text)  # [前の文字, 時刻, 話者, 発言, 時刻, 話者, 発言, ...]
    turns = []
    for i in range(1, len(parts), 3):
        when, speaker, body = parts[i], parts[i + 1], parts[i + 2]
        if until is not None and when is not None and to_seconds(when) > until:
            continue
        body = re.sub(r'\s*\]?\s*$', '', body.split('\n')[0] if '\n' in body else body)
        turns.append((speaker, body))
    return turns


def per_char(turns):
    chars, speakers = [], []
    for speaker, body in turns:
        for ch in IGNORE.sub('', body):
            chars.append(ch)
            speakers.append(speaker)
    return ''.join(chars), speakers


def changes(speakers):
    return sum(1 for a, b in zip(speakers, speakers[1:]) if a != b)


until = None
if '--until' in sys.argv:
    until = to_seconds(sys.argv[sys.argv.index('--until') + 1])

truth_turns = parse_turns(sys.argv[1])
out_turns = parse_turns(sys.argv[2], until)
truth_text, truth_spk = per_char(truth_turns)
out_text, out_spk = per_char(out_turns)

matcher = SequenceMatcher(None, truth_text, out_text, autojunk=False)
matched = agree = 0
for block in matcher.get_matching_blocks():
    for k in range(block.size):
        matched += 1
        agree += truth_spk[block.a + k] == out_spk[block.b + k]

print(f'文字数: 正解 {len(truth_text)} ／ 出力 {len(out_text)}')
print(f'文章の一致: 正解の文字のうち {matched}（{matched / len(truth_text) * 100:.1f}%）が出力に見つかった')
print(f'話者の一致: 見つかった文字のうち {agree}（{agree / max(matched, 1) * 100:.1f}%）で話者が同じ')
print(f'   → 正解の全文字に対する「文字も話者も合っている」割合: {agree / len(truth_text) * 100:.1f}%')
print(f'話者が入れ替わる回数: 正解 {changes(truth_spk)} ／ 出力 {changes(out_spk)}')

empty = sum(1 for _, b in truth_turns if not IGNORE.sub('', b))
short = lambda turns: sum(1 for _, b in turns if 0 < len(IGNORE.sub('', b)) <= 5)
blank_out = sum(1 for _, b in out_turns if not IGNORE.sub('', b))
print(f'発言の数: 正解 {len(truth_turns)}（うち文字なし {empty}、5文字以下 {short(truth_turns)}）'
      f' ／ 出力 {len(out_turns)}（うち文字なし {blank_out}、5文字以下 {short(out_turns)}）')

# 話者ごとの文字数
for name, spk in (('正解', truth_spk), ('出力', out_spk)):
    counts = {s: spk.count(s) for s in sorted(set(spk))}
    print(f'{name}の話者別文字数: {counts}')

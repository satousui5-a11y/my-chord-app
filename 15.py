import streamlit as st

# タイトル
st.title("🎵 コード構成音計算機（ルート×タイプ対応）")
st.write("ルート音とコードの種類を選ぶと、構成音を自動で計算して表示します！")

# 12音の基本リスト
NOTES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

# コードタイプと「ルートから何半音上か」の度数インターバル（音程のルール）
CHORD_TYPES = {
    "Major (メジャー)": [0, 4, 7],               # Root, M3, P5
    "Minor (マイナー)": [0, 3, 7],               # Root, m3, P5
    "maj7 (メジャーセブンス)": [0, 4, 7, 11],     # Root, M3, P5, M7
    "m7 (マイナーセブンス)": [0, 3, 7, 10],       # Root, m3, P5, m7
    "7 (ドミナントセブンス)": [0, 4, 7, 10],      # Root, M3, P5, m7
    "m7b5 (ハーフディミニッシュ)": [0, 3, 6, 10]   # Root, m3, b5, m7
}

# 2列（カラム）に分けて選択ボックスを配置
col_root, col_type = st.columns(2)

with col_root:
    root = st.selectbox("ルート音（Root）", NOTES)

with col_type:
    chord_type = st.selectbox("コードタイプ", list(CHORD_TYPES.keys()))

# 構成音を計算する関数
def calculate_chord(root, chord_type):
    root_index = NOTES.index(root)
    intervals = CHORD_TYPES[chord_type]
    
    calculated_notes = []
    for interval in intervals:
        note_index = (root_index + interval) % len(NOTES)
        calculated_notes.append(NOTES[note_index])
    
    return calculated_notes

# 計算ボタン
if st.button("構成音を計算する"):
    result_notes = calculate_chord(root, chord_type)
    
    st.success(f"**{root} {chord_type}** の構成音:")
    
    cols = st.columns(len(result_notes))
    for i, note in enumerate(result_notes):
        cols[i].metric(label=f"{i+1}個目の音", value=note)

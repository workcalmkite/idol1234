import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(page_title="K-POP 아이돌 목록", page_icon="🎤")

st.title("🎤 K-POP 아이돌 목록")

# 프로젝트 폴더에 있는 csv 파일 불러오기
csv_path = Path(__file__).parent.parent / "kpop_idol.csv"

try:
    # UTF-8 먼저 시도
    try:
        df = pd.read_csv(csv_path, encoding="utf-8-sig")
    except:
        # 안되면 cp949 시도
        df = pd.read_csv(csv_path, encoding="cp949")

    st.success(f"총 {len(df)}명의 데이터를 불러왔습니다.")

    # 검색
    keyword = st.text_input("🔍 이름 또는 그룹 검색")

    if keyword:
        df = df[df.astype(str).apply(
            lambda x: x.str.contains(keyword, case=False, na=False)
        ).any(axis=1)]

    st.dataframe(df, use_container_width=True)

except FileNotFoundError:
    st.error("kpop_idol.csv 파일을 찾을 수 없습니다.")
    st.info("GitHub에 kpop_idol.csv를 함께 업로드하세요.")

except Exception as e:
    st.error(f"오류 발생 : {e}")

import streamlit as st
import pandas as pd

st.set_page_config(page_title="K-POP 아이돌 검색", page_icon="🎤", layout="wide")

st.title("🎤 K-POP 아이돌 검색 앱")

file_name = "Kpop_idol.csv"

try:
    df = pd.read_csv(file_name, encoding="utf-8-sig")
except:
    try:
        df = pd.read_csv(file_name, encoding="cp949")
    except:
        df = pd.read_csv(file_name, encoding="latin1")

st.success("데이터 불러오기 성공!")

st.subheader("📌 전체 아이돌 데이터")
st.dataframe(df, use_container_width=True)

st.divider()

st.subheader("👧👦 성별로 검색하기")

gender = st.selectbox("성별 선택", ["전체", "여자", "남자"])

if gender == "전체":
    gender_df = df
else:
    gender_df = df[
        df.astype(str).apply(
            lambda row: row.str.contains(gender, case=False, na=False).any(),
            axis=1
        )
    ]

st.dataframe(gender_df, use_container_width=True)

st.divider()

st.subheader("🔍 아이돌 이름 검색")

name = st.text_input("아이돌 이름을 입력하세요")

if name:
    result = df[
        df.astype(str).apply(
            lambda row: row.str.contains(name, case=False, na=False).any(),
            axis=1
        )
    ]
    st.dataframe(result, use_container_width=True)

st.divider()

st.subheader("🏢 소속사로 그룹 찾기")

agency = st.text_input("소속사를 입력하세요")

if agency:
    agency_result = df[
        df.astype(str).apply(
            lambda row: row.str.contains(agency, case=False, na=False).any(),
            axis=1
        )
    ]

    st.write(f"검색 결과: {len(agency_result)}개")
    st.dataframe(agency_result, use_container_width=True)

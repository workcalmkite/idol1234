import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="아이돌 검색 앱", page_icon="🎤", layout="wide")

st.title("🎤 아이돌 데이터 검색 앱")
st.write("여자/남자 아이돌을 검색하고, 소속사를 입력하면 그룹을 볼 수 있어요.")

# 파일 자동 찾기
files = os.listdir()
data_files = [f for f in files if f.endswith((".csv", ".xlsx"))]

if not data_files:
    st.error("데이터 파일이 없어요. csv 또는 xlsx 파일을 GitHub에 같이 올려주세요.")
    st.stop()

file_name = data_files[0]

if file_name.endswith(".csv"):
    df = pd.read_csv(file_name)
else:
    df = pd.read_excel(file_name)

st.success(f"데이터 파일 불러오기 성공: {file_name}")

st.subheader("📌 전체 데이터")
st.dataframe(df, use_container_width=True)

st.divider()

# 성별 검색
st.subheader("👧👦 여자 / 남자 아이돌 검색")

gender = st.selectbox(
    "성별을 선택하세요",
    ["전체", "여자", "남자"]
)

if gender != "전체":
    gender_df = df[
        df.astype(str).apply(
            lambda row: row.str.contains(gender, case=False, na=False).any(),
            axis=1
        )
    ]
else:
    gender_df = df

st.dataframe(gender_df, use_container_width=True)

st.divider()

# 아이돌 이름 검색
st.subheader("🔍 아이돌 이름 검색")

idol_name = st.text_input("아이돌 이름을 입력하세요")

if idol_name:
    result = df[
        df.astype(str).apply(
            lambda row: row.str.contains(idol_name, case=False, na=False).any(),
            axis=1
        )
    ]

    st.write(f"검색 결과: {len(result)}개")
    st.dataframe(result, use_container_width=True)

st.divider()

# 소속사 검색
st.subheader("🏢 소속사로 그룹 찾기")

agency = st.text_input("소속사를 입력하세요 예: HYBE, SM, JYP, YG")

if agency:
    agency_result = df[
        df.astype(str).apply(
            lambda row: row.str.contains(agency, case=False, na=False).any(),
            axis=1
        )
    ]

    if len(agency_result) > 0:
        st.write(f"'{agency}' 검색 결과: {len(agency_result)}개")
        st.dataframe(agency_result, use_container_width=True)
    else:
        st.warning("해당 소속사의 그룹을 찾을 수 없어요.")

st.divider()

# 간단 통계
st.subheader("📊 데이터 요약")
st.write(f"전체 데이터 개수: {len(df)}개")
st.write(f"컬럼 개수: {len(df.columns)}개")
st.write("컬럼 이름:", list(df.columns))

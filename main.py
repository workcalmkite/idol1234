import streamlit as st
import pandas as pd
import glob

st.set_page_config(page_title="K-POP 아이돌 검색", page_icon="🎤", layout="wide")

st.title("🎤 K-POP 아이돌 검색 앱")

# 현재 폴더의 csv 파일 자동 찾기
csv_files = glob.glob("*.csv")

if not csv_files:
    st.error("❌ CSV 파일을 찾을 수 없습니다.")
    st.stop()

file_name = csv_files[0]

# 여러 인코딩 자동 시도
loaded = False
for enc in ["utf-8", "utf-8-sig", "cp949", "euc-kr", "latin1"]:
    try:
        df = pd.read_csv(file_name, encoding=enc)
        loaded = True
        break
    except:
        pass

if not loaded:
    st.error("CSV 파일을 읽을 수 없습니다.")
    st.stop()

st.success(f"데이터 파일 : {file_name}")

# 컬럼 이름 출력
st.write("컬럼:", list(df.columns))

# 성별 검색
st.header("👦👧 성별 검색")

gender = st.selectbox("성별 선택", ["전체", "남자", "여자"])

if gender != "전체":
    result = df[df.astype(str).apply(
        lambda x: x.str.contains(gender, case=False).any(), axis=1)]
else:
    result = df

st.dataframe(result, use_container_width=True)

# 이름 검색
st.header("🔍 아이돌 이름 검색")

name = st.text_input("이름 입력")

if name:
    result = df[df.astype(str).apply(
        lambda x: x.str.contains(name, case=False).any(), axis=1)]
    st.dataframe(result, use_container_width=True)

# 소속사 검색
st.header("🏢 소속사 검색")

agency = st.text_input("소속사 입력")

if agency:
    result = df[df.astype(str).apply(
        lambda x: x.str.contains(agency, case=False).any(), axis=1)]

    st.dataframe(result, use_container_width=True)

    st.subheader("그룹 목록")
    if "Group" in df.columns:
        st.write(result["Group"].drop_duplicates().tolist())
    elif "group" in df.columns:
        st.write(result["group"].drop_duplicates().tolist())

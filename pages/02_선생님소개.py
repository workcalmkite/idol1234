import streamlit as st

st.title("👨‍🏫 선생님 소개")

teachers = {
    "교장선생님": "학교를 책임지고 운영하시는 분",
    "교감선생님": "학교 교육을 지원하시는 분",
    "담임선생님": "학생들과 가장 가까이에서 함께하는 선생님",
    "교과선생님": "국어, 영어, 수학 등 다양한 과목을 가르치는 선생님"
}

for name, intro in teachers.items():
    st.subheader(name)
    st.write(intro)

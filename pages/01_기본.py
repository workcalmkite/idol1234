import streamlit as st

st.set_page_config(page_title="학교 소개", page_icon="🏫")

st.title("🏫 방배중학교")

st.image("https://images.unsplash.com/photo-1509062522246-3755977927d7", use_container_width=True)

st.header("학교 소개")

st.write("""
방배중학교는 학생들의 꿈과 끼를 키우는 학교입니다.

✔️ 바른 인성
✔️ 창의적인 사고
✔️ 함께 성장하는 학교

학생들이 즐겁게 배우고 행복하게 생활할 수 있도록 다양한 교육활동을 운영하고 있습니다.
""")

st.info("우리 학교에 오신 것을 환영합니다!")

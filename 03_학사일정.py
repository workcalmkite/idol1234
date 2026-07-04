import streamlit as st
import pandas as pd

st.title("📅 학사일정")

schedule = pd.DataFrame({
    "월":["3월","4월","5월","7월","9월","12월"],
    "행사":[
        "입학식",
        "중간고사",
        "체육대회",
        "여름방학",
        "축제",
        "겨울방학"
    ]
})

st.dataframe(schedule, use_container_width=True)

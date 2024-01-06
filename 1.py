import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_extras.let_it_rain import rain
import requests
import json

st.set_page_config(page_title="NewYear",)

def load_lottie_json(file_path):
    with open(file_path, "r") as file:
        return json.load(file)

def main():
    # 로컬에 저장된 Lottie JSON 파일 경로
    lottie_file_path = "1.json"  # 여기에 다운로드한 파일 경로를 입력해주세요

    # Lottie 파일 로드
    lottie_json = load_lottie_json(lottie_file_path)

    # Streamlit에 Lottie 애니메이션 표시
    st_lottie(lottie_json, speed=1, width=600, height=600)

def snow():
    rain(
        emoji="❄️",
        font_size=36,
        falling_speed=10,
        animation_length="infinite",
    )

if __name__ == "__main__":
    main()

snow()
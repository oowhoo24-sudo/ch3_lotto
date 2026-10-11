import streamlit as st
import random

st.set_page_config(page_title="로또 번호 생성기", layout="centered")

# 번호 대역별 실제 로또 공 배경색 지정 함수
def get_ball_color(num):
    if num <= 10:
        return "#fbc400"  # 노란색 (1~10)
    elif num <= 20:
        return "#69c8f2"  # 파란색 (11~20)
    elif num <= 30:
        return "#ff7272"  # 빨간색 (21~30)
    elif num <= 40:
        return "#aaa"     # 회색 (31~40)
    else:
        return "#b0d840"  # 녹색 (41~45)

# 번호 세트 목록을 세션 상태에 저장 (최대 5개 유지)
if "lotto_history" not in st.session_state:
    st.session_state.lotto_history = []

st.title("🎲 로또 번호 생성기")

# 버튼 영역
col1, col2 = st.columns([1, 1])
with col1:
    if st.button("로또번호 생성", use_container_width=True):
        if len(st.session_state.lotto_history) < 5:
            new_numbers = sorted(random.sample(range(1, 46), 6))
            st.session_state.lotto_history.append(new_numbers)
        else:
            st.warning("최대 5세트까지만 생성할 수 있습니다.")

with col2:
    if st.button("초기화", use_container_width=True):
        st.session_state.lotto_history = []
        st.rerun()

st.write("---")

# 번호 출력 영역 (가로 정렬 + 공 디자인)
if st.session_state.lotto_history:
    for idx, nums in enumerate(st.session_state.lotto_history, 1):
        balls_html = "".join([
            f"""<div style="
                display: inline-flex;
                align-items: center;
                justify-content: center;
                width: 42px;
                height: 42px;
                border-radius: 50%;
                background-color: {get_ball_color(n)};
                color: #ffffff;
                font-weight: bold;
                font-size: 16px;
                margin: 0 4px;
                text-shadow: 0 1px 2px rgba(0,0,0,0.3);
            ">{n}</div>"""
            for n in nums
        ])

        st.markdown(
            f"""
            <div style="display: flex; align-items: center; margin-bottom: 14px;">
                <span style="font-weight: bold; font-size: 16px; width: 60px;">세트 {idx}</span>
                <div style="display: flex; flex-direction: row;">
                    {balls_html}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
else:
    st.info("버튼을 눌러 로또 번호를 생성해보세요. (최대 5세트)")
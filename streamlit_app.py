import streamlit as st
# [제목과 메뉴판] - print 대신 st.title, st.write 사용
st.title("🔋 시험 기간 카페인 반감기 계산기")

drinks = ["아메리카노", "몬스터 에너지", "핫식스", "캔커피"]
caffeine_amounts = [150, 100, 60, 40]
total_caffeine = 0

st.write("--- 카페인 음료 메뉴판 ---")
for i in range(len(drinks)):
    st.write(f"{i+1}. {drinks[i]} ({caffeine_amounts[i]}mg)")

# ------------------------------------------------------------------
# [핵심 변경 번역존] 
# 원래 코드: while True: choice = int(input())
# 변경 코드: 한 줄에 마신 번호를 다 받아와서(st.text_input) 공백으로 쪼개기(.split)
# ------------------------------------------------------------------
user_input = st.text_input("마신 음료 번호들을 공백으로 구분해서 입력하세요 (예: 1 2 1):", "")

if user_input:  # 사용자가 무언가 입력했을 때만 작동
    choices = user_input.split()  # 예: "1 2" 입력 시 ['1', '2']로 변환
    
    for c in choices:
        choice = int(c)  # 문자를 숫자로 변환
        
        # [2차시 조건문과 완벽히 동일]
        if 1 <= choice <= len(drinks):
            total_caffeine += caffeine_amounts[choice-1]
# ------------------------------------------------------------------

st.write(f"**오늘 총 섭취한 카페인:** {total_caffeine} mg")

# [시간 입력] - input 대신 st.number_input 사용
sleep_hours = st.number_input("몇 시간 후에 잠에 들 예정이신가요?:", min_value=1, max_value=24, value=5)

# [반감기 계산 반복문] - 2차시 코드와 100% 동일
remaining_caffeine = total_caffeine
for hour in range(1, sleep_hours + 1):
    remaining_caffeine = remaining_caffeine * 0.87

st.write(f"{sleep_hours}시간 후 몸에 남은 카페인: **{remaining_caffeine:.1f} mg**")

# [최종 조건문 판정] - print 대신 st.error, st.success로 색상만 입힘
if remaining_caffeine >= 50:
    st.error("🚨 [경고] 체내 카페인 수치가 높아 밤에 잠을 설칠 수 있습니다!")
else:
    st.success("✅ [안전] 카페인이 안전 수치로 떨어졌습니다. 편안하게 주무세요!")

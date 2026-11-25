
import streamlit as st
import random

# 웹사이트 화면 설정
st.set_page_config(
    page_title="맞춤형 문제집 추천",
    page_icon="📚",
    layout="wide"
)

# 수학 문제집 리스트
math_books = [
    ["마더텅", "블랙라벨"],
    ["쎈", "올림포스"],
    ["RPM", "기탄수학"],
    ["기초수학"]
]

# 과학 문제집 리스트
science_books = [
    ["하이탑", "메가스터디 N제"],
    ["완자 기출PICK", "자이스토리"],
    ["오투", "완자"],
    ["EBS 50일 통합과학"]
]

# 난이도 리스트
difficulty = ["최상", "상", "중", "하"]

# 수학 공부 꿀팁 리스트
math_tips = [
    "공식을 무작정 외우지 말고 원리를 이해하기",
    "개념을 공부한 뒤 기본 유형 반복하기",
    "틀린 문제는 틀린 이유를 기록하기",
    "어려운 문제보다 기본 문제의 정답률 높이기",
    "복습할 때 해설 없이 다시 풀어 보기"
]

# 과학 공부 꿀팁 리스트
science_tips = [
    "핵심 개념과 용어부터 정확히 이해하기",
    "그림과 그래프를 활용하여 개념 정리하기",
    "실험의 원인과 결과를 연결하여 이해하기",
    "틀린 선지가 왜 틀렸는지 분석하기",
    "공부한 개념을 자신의 말로 설명하기"
]


# 문제집 추천 함수
def recommend(grade, book_list):

    # 조건문을 이용한 수준 분류
    if grade == 1:
        level = "최상"
        selected = [0, 1]

    elif grade <= 3:
        level = "상"
        selected = [1, 2]

    else:
        level = "중·하"
        selected = [2, 3]

    books = []

    # for 반복문을 이용한 문제집 선정
    for i in selected:
        book = random.choice(book_list[i])
        books.append([book, difficulty[i]])

    return level, books


# 공부 꿀팁 출력 함수
def show_tips(tips):

    st.subheader("💡 공부 꿀팁")

    # for 반복문을 이용한 꿀팁 출력
    for i in range(len(tips)):
        st.write(str(i + 1) + ". " + tips[i])


# 분석 결과 출력 함수
def show_result(subject, age, grade, book_list, tips):

    level, books = recommend(grade, book_list)

    st.subheader(subject + " 분석 결과")

    st.write("나이:", age, "세")
    st.write("모의고사 등급:", grade, "등급")
    st.write("현재 학습 수준:", level)

    # 추천 문제집 표 만들기
    table = []

    for book in books:
        table.append({
            "문제집": book[0],
            "난이도": book[1]
        })

    st.markdown("**📚 추천 문제집**")
    st.table(table)

    # 나이와 등급에 따른 학습 방법 추천
    if age == 19 and grade <= 3:
        st.success("실모를 푸는걸 추천!!!")

    else:
        st.success("문제집 푸는걸 추천!!!")

    # 4~6등급 학생에게 공부 꿀팁 제공
    if grade >= 4:
        st.divider()
        show_tips(tips)


# 웹사이트 제목
st.title("📚 맞춤형 수학·과학 문제집 추천 시스템")

st.write(
    "자신의 나이와 수학, 과학 모의고사 "
    "등급을 입력하세요."
)

# 나이 선택
age = st.radio(
    "자신의 나이를 선택하세요.",
    [17, 18, 19],
    format_func=lambda x: str(x) + "세",
    horizontal=True
)

st.divider()

# 수학과 과학 화면 분리
col1, col2 = st.columns(2)

# 왼쪽 수학 영역
with col1:
    with st.container(border=True):

        st.markdown("## :blue[📐 수학]")

        math_grade = st.radio(
            "수학 모의고사 등급",
            [1, 2, 3, 4, 5, 6],
            format_func=lambda x: str(x) + "등급",
            key="math"
        )

# 오른쪽 과학 영역
with col2:
    with st.container(border=True):

        st.markdown("## :green[🔬 과학]")

        science_grade = st.radio(
            "과학 모의고사 등급",
            [1, 2, 3, 4, 5, 6],
            format_func=lambda x: str(x) + "등급",
            key="science"
        )

# 분석 버튼
if st.button(
    "분석",
    type="primary",
    use_container_width=True
):

    st.divider()
    st.header("📊 맞춤형 분석 결과")

    # 분석 결과 화면 분리
    result1, result2 = st.columns(2)

    # 수학 분석 결과
    with result1:
        with st.container(border=True):

            show_result(
                "📐 수학",
                age,
                math_grade,
                math_books,
                math_tips
            )

    # 과학 분석 결과
    with result2:
        with st.container(border=True):

            show_result(
                "🔬 과학",
                age,
                science_grade,
                science_books,
                science_tips
            )

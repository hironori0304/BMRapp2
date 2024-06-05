import streamlit as st

def calculate_bmr(sex, weight, height, age):
    if sex == "男性":
        bmr = 66.473 + (13.7516 * weight) + (5.0033 * height) - (6.7550 * age)
    else:
        bmr = 655.0955 + (9.5634 * weight) + (1.8496 * height) - (4.6756* age)
    return bmr

def main():
    st.title("エネルギー必要量計算アプリ")

    # ハリスベネディクトの式を表示
    st.write("### ハリスベネディクトの式")
    st.write("男性: BMR = 66.473 + (13.7516 × 体重[kg]) + (5.0033 × 身長[cm]) - (6.7550 × 年齢[歳])")
    st.write("女性: BMR = 655.0955+ (9.5634 × 体重[kg]) + (1.8496 × 身長[cm]) - (4.6756 × 年齢[歳])")

    # 入力フォーム
    sex = st.radio("性別", ("男性", "女性"))
    age = st.number_input("年齢（歳）", min_value=0, max_value=120, value=0, step=1, format='%d')
    height = st.number_input("身長（cm）", min_value=0.0, max_value=250.0, value=0.0, step=0.1, format='%.1f')
    weight = st.number_input("体重（kg）", min_value=0.0, max_value=300.0, value=0.0, step=0.1, format='%.1f')

    activity_factor = st.number_input("活動係数", min_value=1.0, max_value=2.0, value=1.0, step=0.1, format='%.1f')
    stress_factor = st.number_input("ストレス係数", min_value=1.0, max_value=2.0, value=1.0, step=0.1, format='%.1f')

    if st.button("エネルギー必要量を計算"):
        if age == 0 or height == 0 or weight == 0:
            st.error("すべてのフィールドに有効な値を入力してください。")
        else:
            bmr = calculate_bmr(sex, weight, height, age)
            tdee = bmr * activity_factor * stress_factor
            st.write(f"基礎代謝量 (BMR): {bmr:.2f} kcal/day")
            st.write(f"総エネルギー消費量 (TDEE): {tdee:.2f} kcal/day")

if __name__ == "__main__":
    main()


import streamlit as st

st.title("Calculate BMI")
st.markdown("---")
bg="""
<style>
.stApp {
    background-image: url("https://img.freepik.com/free-photo/smooth-gray-background-with-high-quality_53876-124606.jpg?semt=ais_hybrid&w=740");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}
</style>
"""
st.html(bg)




kg= st.number_input("น้ำหนัก (KG.)",value=60.5, min_value=10.0 ,max_value=200.0 ,step=0.5)
cm= st.number_input ("ส่วนสูง (CM.)",value=100, min_value=1 ,max_value=200 ,step=1)

sex = st.radio("เพศ",("ชาย","หญิง"),horizontal=True)
if st.button ("Calculate"):
    bmi=kg/(cm/100)**2
    st.subheader(f"ค่าดัชนีมวลกายของคุณคือ {bmi:.1f}")


    if sex=="หญิง":
        if (bmi) < 18.5:
            st.error("น้ำหนักต่ำกว่าเกณฑ์")
            st.error("เสี่ยงโรคขาดสารอาหาร")    
            st.image("underweight woman.png","นี้อาจเป็นสภาพของคุณ")

        elif (bmi) < 23:
            st.success("น้ำหนักสมส่วน")
            st.success("โอกาสมีโรคแทรกซ้อนน้อย")
            st.image("normal woman.png","นี้อาจเป็นสภาพของคุณ")

        elif (bmi) < 25:
            st.warning("น้ำหนักเกินมาตรฐาน")
            st.warning("ภาวะน้ำหนักเกิน ระยะเริ่มต้น")
            st.image("overweight.png","นี้อาจเป็นสภาพของคุณ")

        elif (bmi) < 30:
            st.warning("น้ำหนักเกิน")
            st.warning("ภาวะน้ำหนักเกินมาก ระยะอ้วนเริ่มต้น")
            st.image("obesity class 1.png","นี้อาจเป็นสภาพของคุณ")

        elif (bmi) > 30:
            st.error("น้ำหนักเกินมาก")
            st.error("ภาวะน้ำหนักเกินมาก โรคอ้วน")
            st.image("obesity class 2 or higher.png","นี้อาจเป็นสภาพของคุณ")



    elif sex=="ชาย":
        if (bmi) < 19:
            st.error("น้ำหนักต่ำกว่าเกณฑ์")
            st.error("เสี่ยงโรคขาดสารอาหาร")    
            st.image("underweight man.png","นี้อาจเป็นสภาพของคุณ")

        elif (bmi) < 24:
            st.success("น้ำหนักสมส่วน")
            st.success("โอกาสมีโรคแทรกซ้อนน้อย")
            st.image("normal weight man.png","นี้อาจเป็นสภาพของคุณ")

        elif (bmi) < 26:
            st.warning("น้ำหนักเกินมาตรฐาน")
            st.warning("ภาวะน้ำหนักเกิน ระยะเริ่มต้น")
            st.image("overweight man.png","นี้อาจเป็นสภาพของคุณ")

        elif (bmi) < 30:
            st.warning("น้ำหนักเกิน")
            st.warning("ภาวะน้ำหนักเกินมาก ระยะอ้วนเริ่มต้น")
            st.image("obesity class 1 man.png","นี้อาจเป็นสภาพของคุณ")

        elif (bmi) > 30:
            st.error("น้ำหนักเกินมาก")
            st.error("ภาวะน้ำหนักเกินมาก โรคอ้วน")
            st.image("obesity class 2 man.png","นี้อาจเป็นสภาพของคุณ")

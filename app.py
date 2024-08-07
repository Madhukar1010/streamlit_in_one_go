import streamlit as st

st.title("STREAMLIT PRACTICE : ")
st.header("STREAMLIT PRACTICE : ")
st.subheader("STREAMLIT PRACTICE : ")
st.text("STREAMLIT PRACTICE : ")

st.markdown("# Hello")
st.markdown("## Hello")
st.markdown("### Hello")
st.markdown("#### Hello")
st.markdown("##### Hello")

st.success("success!")
st.info("Information")
st.warning("Its a warning")
st.error("Its an error")
st.exception(ZeroDivisionError("Division not possible with zero"))

st.help(ZeroDivisionError)

st.subheader("WRITE : ")
st.write("range(1,10)")
st.write(range(1,10))
st.write(1+2+3)
x = 2
st.write("The number is : ",x)

st.subheader("CODE : ")
st.code("x = 10 \n"
        "for i in range(x): \n"
        "\tprint(i)")

st.subheader("CHECKBOX : ")
st.checkbox("Male")
if st.checkbox("Adult"):
    st.write("You are an Adult!")

st.subheader("RADIO : ")
RadioButton = st.radio("select : ", ["Male", "Female", "Other"])
if RadioButton == "Male":
    st.write("You are a Male")
elif RadioButton == "Female":
    st.write("You are a Female")
else:
    st.write("You are other gender")

st.subheader("SELECTBOX : ")
SelectedBox = st.selectbox("Courses available : ", ["Data Science", "Web Development",
                                      "Java", "AIML", "Python Developer"])
st.write("You selected : ", SelectedBox)

st.subheader("MULTI SELECTBOX : ")
Multi_Select_Box = st.multiselect("Courses available : ", ["Data Science", "Web Development",
                                      "Java", "AIML", "Python Developer"])
st.write("You selected : ", len(Multi_Select_Box), "Courses")
st.write("Your courses are : ", Multi_Select_Box)

st.subheader("Button : ")
st.button("Click me")
if st.button("press here"):
    st.write("You have pressed here!")

st.subheader("SLIDER : ")
st.slider("select the level : ", 1, 10, step = 1)
vol = st.slider("select the volume : ", 1, 100, step = 1)
st.write("The volume is : ", vol)

st.subheader("TEXT INPUT : ")
Username = st.text_input("Username :  ")
Password = st.text_input("password : ", type = "password")
st.write(Username, ":", Password)

st.subheader("TEXT AREA : ")
textArea = st.text_area("write something here in some words ?")
st.write(textArea)

st.subheader("NUMBER INPUT : ")
age = st.number_input("select your age")
st.write(age)
Age = st.number_input("select your age", 18, 25)
st.write(Age)

st.subheader("DATE INPUT : ")
st.date_input("Date : ")

st.subheader("TIME INPUT : ")
st.time_input("Time : ")

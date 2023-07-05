import requests
import streamlit as st
from streamlit_lottie import st_lottie


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# ---- LOAD ASSETS ----
lottie_coding1 = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_BROxHtztMy.json")


# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hi, I am Dishani :wave:")
    st.title("A Data Engineer From Belgium")
    st.write(
        "I am passionate about using data solutions to support smart business decisions and tackling complex high-stakes problems. ")
    st.write("[Learn More >](https://www.linkedin.com/in/dishanisen/)")

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            With a knack for career guidance and a passion for helping individuals achieve their goals, I help professionals like you:
            - With a second pair of eyes to your resume/CV via my resume reviewing services
            - Create compelling resume that stands out 
            - Review SOP with constructive feedback to enhance the impact
            - With tailored advice on how to break into the data science
            - Make informed decisions about your professional journey, especially when it involves relocating abroad"

            If this sounds interesting to you, consider directly reaching out to me via the contact form 👇 
            """
        )
        st.write("[Topmate >](https://topmate.io/dishani_sen)")
    with right_column:
        st_lottie(lottie_coding1, height=300, key="coding")


# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/dishani.sen@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)

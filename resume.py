import streamlit as st
import requests
from streamlit_lottie import st_lottie

st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")
def load_lottieurl1(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def load_lottieurl2(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
# ---- LOAD ASSETS ----
lottie_coding1 = load_lottieurl1("https://assets2.lottiefiles.com/packages/lf20_BROxHtztMy.json")
lottie_coding2 = load_lottieurl2("https://assets10.lottiefiles.com/packages/lf20_azmnf6vt.json")

st.title("Dishani's Resume Review Portal")

st.subheader("Hi, I am Dishani :wave:")
st.header("A Data Engineer From Belgium")
st.write(
        "I am passionate about using data solutions to support smart business decisions and tackling complex high-stakes problems. ")
st.write("[Learn More >](https://www.linkedin.com/in/dishanisen/)")


# Step 3: Reviewer Panel
st.header("What I do")
st.write("---")
left_column, right_column = st.columns(2)
with left_column:
        st.write("##")
        st.write(
            """
            With a knack for career guidance and a passion for helping individuals achieve their goals, I help professionals like you:
            - With a second pair of eyes to your resume/CV via my resume reviewing services
            - Create compelling resume that stands out 
            - Review SOP with constructive feedback to enhance the impact
            - With tailored advice on how to break into the data science
            - Make informed decisions about your professional journey, especially when it involves relocating abroad

            If this sounds interesting to you, you can connect with me via 👇 
            """
        )
        st.write("[Topmate >](https://topmate.io/dishani_sen)")
with right_column:
        st_lottie(lottie_coding1, height=300, key="coding1")


def main():
    

    # Step 1: User Interface
    st.header("Get a free resume review")
    resume_file = st.file_uploader("Upload your resume", type=["pdf", "docx"])
    additional_files = st.file_uploader("Upload any additional files", accept_multiple_files=True)

    if st.button("Submit"):
        # Step 2: File Handling
        if resume_file is not None:
            save_file(resume_file, "resume")
        if additional_files is not None:
            for file in additional_files:
                save_file(file, file.name)

        st.success("Your resume materials have been submitted successfully!")

def save_file(file, prefix):
    with open(f"{prefix}_{file.name}", "wb") as f:
        f.write(file.getbuffer())

if __name__ == "__main__":
    main()




# ---- Description ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("How does it work?")
        st.write("##")
        st.write(
            """
            Thanks for visiting my portal and trusting me with your resume. Here, on the other hand,a real human (that's correct,I) will analyse your resume and provide actionalble feedback.
            - If you have a message for me, please put them in the contact form.
            - Even if you do not have any special note for me, please do not forget to fill the contact form below, after submitting your resume for review.
            - This portal is still under development, so at this point, I can only get back to you with tailored advice on your resume when you leave your email through this form.
            - All the best for your career journey,🤝 happy to have helped you!
            
            """
        )
        
    with right_column:
        st_lottie(lottie_coding2, height=300, key="coding")

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



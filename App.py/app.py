from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st
import PyPDF2
from datetime import datetime
import speech_recognition as sr
 
 
# Initialize speech recognizer
recognizer = sr.Recognizer()
 
llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key="AIzaSyAZ80lI5yqgUVI1sMVWAiNgYDYnXB1FYSc")
 
 
 
def send_prompt(prompt):
    if prompt:
        if "pdf_content" in st.session_state:
            # If PDF content is available, concatenate it with the user prompt
            prompt += "\n\n" + st.session_state.pdf_content
       
        st.session_state.chat_session.append(("user", prompt))
        st.chat_message("user").markdown(prompt)
       
        # Send the combined prompt to the chatbot for processing
        response = llm.invoke(prompt)
       
        st.session_state.chat_session.append(("assistant", response.content))
        with st.chat_message("assistant"):
            st.markdown(response.content)
 
 
 
   # Function for speech recognition
def start_speech_recognition():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        st.write("Listening... (Speak your message)")
        audio_data = recognizer.listen(source)
    try:
        st.write("Processing...")
        text = recognizer.recognize_google(audio_data)
        st.write("You said:", text)
        send_prompt(text)
    except sr.UnknownValueError:
        st.error("Sorry, I could not understand what you said.")
    except sr.RequestError as e:
        st.error(f"Could not request results from Google Speech Recognition service; {e}")
         
 
def read_pdf(file):
    if file is not None:
        content = ""
        reader = PyPDF2.PdfReader(file)
        for page in range(len(reader.pages)):
            content += reader.pages[page].extract_text()
       
        # Store the extracted text content in the session state
        st.session_state.pdf_content = content
       
        # Set flag to indicate that PDF content has been sent
        st.session_state.pdf_sent = True
       
        # Send the extracted text content to the chatbot
        send_prompt(content)
 
st.set_page_config(
    page_title="AI chatbot powered with Gemini Pro",
    layout="centered",
)
 
# Function to save chat history in session state
def save_chat_history():
    current_date = datetime.now().date()
    if "chat_sessions" not in st.session_state:
        st.session_state.chat_sessions = {}
    chat_session = st.session_state.get("chat_session", [])
    st.session_state.chat_sessions[str(current_date)] = chat_session
 
# Function to display chat history in sidebar
def display_chat_history_sidebar():
    with st.sidebar:
        st.title("Chat History")
        chat_sessions = st.session_state.get("chat_sessions", {})
        for date, chat_session in chat_sessions.items():
            expander = st.sidebar.expander(f"{date}")
            with expander:
                if chat_session:
                    for sender, message in chat_session:
                        if sender == "user":
                            st.markdown(f"**User:** {message}")
                        elif sender == "assistant":
                            st.markdown(f"**Assistant:** {message}")
                else:
                    st.info("No chat history available.")
 
 
st.title("SaidGPT 🕵️‍♀️🧷 ")
 
if "chat_session" not in st.session_state:
    st.session_state.chat_session = []
 
# Send text chat
prompt = st.chat_input("Write a message...")
 
# Upload PDF file
file = st.file_uploader("Upload a PDF", type="pdf")
 
if "chat_session" in st.session_state:  # Display chat history if it exists
    for sender, message in st.session_state.chat_session:
        with st.chat_message(sender):
            st.markdown(message)
 
# Process input prompt or uploaded PDF
if prompt:
    send_prompt(prompt)
elif file:
    read_pdf(file)
 
 
 
 
 
    # Initialize session state
if 'usernames' not in st.session_state:
   st.session_state.usernames = ["user"]
if 'passwords' not in st.session_state:
   st.session_state.passwords = ["password"]
 
# Function for my theme with animation
def set_magical_theme_with_sparkles():
   
   # Set background color and text color
   st.markdown(
       """
<style>
       body {
           background-color: #000000;  /* Black background */
           color: #FFFFFF;  /* White text color */
           overflow: hidden; /* Prevent sparkles from overflowing */
       }
</style>
       """,
       unsafe_allow_html=True
   )
   
   st.markdown(
       """
<style>
       @keyframes sparkle {
           0% {transform: translateY(0) scale(0.8);}
           50% {transform: translateY(-15px) scale(1);}
           100% {transform: translateY(0) scale(0.8);}
       }
       .sparkle {
           position: fixed;
           width: 5px;  /* Smaller sparkles */
           height: 5px;  /* Smaller sparkles */
           background: #FFFFFF;  /* White sparkle color */
           border-radius: 50%;
           animation: sparkle 1s ease-in-out infinite;
           box-shadow: 0 0 5px #FFFFFF; /* Add glow effect */
       }
       .sparkle:nth-child(1) {
           top: 20%;
           left: 10%;
           animation-delay: 0.2s;
       }
       .sparkle:nth-child(2) {
           top: 30%;
           left: 30%;
           animation-delay: 0.5s;
       }
       .sparkle:nth-child(3) {
           top: 10%;
           left: 50%;
           animation-delay: 0.7s;
       }
       .sparkle:nth-child(4) {
           top: 40%;
           left: 70%;
           animation-delay: 0.4s;
       }
       .sparkle:nth-child(5) {
           top: 25%;
           left: 90%;
           animation-delay: 0.6s;
       }
       /* Additional sparkles */
       .sparkle:nth-child(6) {
           top: 15%;
           left: 20%;
           animation-delay: 0.8s;
       }
       .sparkle:nth-child(7) {
           top: 35%;
           left: 40%;
           animation-delay: 0.3s;
       }
       .sparkle:nth-child(8) {
           top: 5%;
           left: 60%;
           animation-delay: 0.9s;
       }
       .sparkle:nth-child(9) {
           top: 45%;
           left: 80%;
           animation-delay: 0.1s;
       }
       .sparkle:nth-child(10) {
           top: 30%;
           left: 70%;
           animation-delay: 0.7s;
       }
</style>
       """,
       unsafe_allow_html=True
   )
# Function to customize font and typography
   
def customize_typography():
   # Set custom fonts and styles
   st.markdown(
       """
<style>
       /* Set custom fonts */
       body {
           font-family: 'Comic Sans MS', cursive, sans-serif;  /* Use whimsical font */
       }
       /* Customize headings */
       h1, h2, h3 {
           color: #FFFFFF;  /* White heading color */
           font-weight: bold;
           text-align: center;
       }
       /* Customize button styles */
       .css-1aumxhk {
           background-color: #8A2BE2 !important;  /* Dark violet button color */
           color: #FFFFFF !important;  /* White button text color */
       }
</style>
       """,
       unsafe_allow_html=True
   )
# Main function to run the app
def main():
   
   
   # Set magical theme with sparkles animation
   set_magical_theme_with_sparkles()
   # Customize typography
   customize_typography()
   
   # Add sparkles animation
   st.markdown(
       """
<div class="sparkle"></div>
<div class="sparkle"></div>
<div class="sparkle"></div>
<div class="sparkle"></div>
<div class="sparkle"></div>
<div class="sparkle"></div>
<div class="sparkle"></div>
<div class="sparkle"></div>
<div class="sparkle"></div>
<div class="sparkle"></div>
       """,
       unsafe_allow_html=True
   )
 
 # Speech recognition buttons
col1, col2 = st.columns(2)
with col1:
        if st.button("Speak"):
            start_speech_recognition()
with col2:
        if st.button("Stop"):
            pass  # You can stop speech recognition if needed
 
   # Animated sidebar
# Function to display chat history in sidebar
def display_chat_history_sidebar():
    with st.sidebar:
        # Chat Using PDF title
        st.title('Chat Using PDF 🧾')
 
        # Login form
        st.subheader("Login")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        login_button = st.button("Login")
        if login_button:
            if username in st.session_state.usernames and \
                    password == st.session_state.passwords[st.session_state.usernames.index(username)]:
                st.success("Logged in as user!")
            else:
                st.error("Invalid username or password.")
 
        # Sign-up form
        st.subheader("Sign-up")
        new_username = st.text_input("New Username")
        new_password = st.text_input("New Password", type="password")
        confirm_password = st.text_input("Confirm Password", type="password")
        signup_button = st.button("Sign Up")
        if signup_button:
            if new_password == confirm_password:
                st.session_state.usernames.append(new_username)
                st.session_state.passwords.append(new_password)
                st.success("Sign-up successful! You can now log in.")
            else:
                st.error("Passwords do not match. Please try again.")
 
        # About section
        st.markdown('''
            ## About
            This app is an LLM-powered chatbot built using:
            - [Streamlit](https://streamlit.io/)
            - [LangChain](https://python.langchain.com/)
 
            ''')
 
        st.write("Made with ❤️ by Reem's Group")
 
       
 
save_chat_history()
display_chat_history_sidebar()              
 
# Run the app
if __name__ == "__main__":
   main()
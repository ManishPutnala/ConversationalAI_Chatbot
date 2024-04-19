import streamlit as st 
import google.generativeai as genai 

key = open("/gemini_key.txt")
genai.configure(api_key = key)
gemini_model = genai.GenerativeModel('gemini-pro')

st.set_page_config(
    page_title = "Data Jedi",
    page_icon = "🫧",
)

# Initialize conversation history if it doesn't exist
if "conversation" not in st.session_state:
    st.session_state.conversation = []

if not st.session_state.conversation:
    st.session_state.conversation.append({"role": "assistant", "content": "Hello, This is Data Jedi, Here to assist you with all your queries in data science"})
    st.title(":rainbow[Welcome to the Data Land]")

# Display conversation history
for message in st.session_state.conversation:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Get user input
user_input = st.chat_input()

# Add user input to conversation
if user_input is not None:
    st.session_state.conversation.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

# Generate AI response
if user_input and st.session_state.conversation[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Data Jedi is sharing its wisdom with you, just a moment..."):
            ai_response = gemini_model.generate_content(user_input)
            st.write(ai_response.text)
        new_ai_message = {"role": "assistant", "content": ai_response.text}
        st.session_state.conversation.append(new_ai_message)

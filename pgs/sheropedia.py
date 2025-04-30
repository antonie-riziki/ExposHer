

import streamlit as st 
import sys



sys.path.insert(1, './models')
print(sys.path.insert(1, '../models/'))

from func import sheropedia_topics

from dotenv import load_dotenv

load_dotenv()



st.markdown(
    """
    <div class=title>
        <div style=" justify-content: center;">
            <h1 style="text-align: center; padding: 5px; color: #F52887;">sHeropedia💃</h1>
            <p style="text-align: center;">Building Tomorrow's Women Leaders Today</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)


st.image('https://blog.ipleaders.in/wp-content/uploads/2021/01/img-20190306-5c7f72b3a4ca1.jpg', width=900)



topics = {
    "🩸 Menstrual Health": "Menstrual Health",
    "👭 Girl Talks": "Girl Talks",
    "🧠 Mental Health": "Mental Health",
    "🏫 Girls in Education": "Girls in Education",
    "👩‍⚕️ Women in Healthcare": "Women in Healthcare",
    "💼 Women in Leadership": "Women in Leadership",
    "🚺 Gender Equality": "Gender Equality",
    "💪 Self-Esteem & Confidence": "Self-Esteem & Confidence",
    "🛡️ Women Safety": "Women Safety",
    "💖 Relationships & Boundaries": "Relationships & Boundaries"
}

selected_topic = None

col11, col12 = st.columns(2)

with col11:
    col1, col2 = st.columns(2)
    for i, (emoji_label, topic_name) in enumerate(topics.items()):
        if i % 2 == 0:
            if col1.button(emoji_label, key=topic_name):
                selected_topic = topic_name
        else:
            if col2.button(emoji_label, key=topic_name):
                selected_topic = topic_name

# Initialize chat history if not already
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "How may I help you?"}]

# Inject topic introduction once on selection
if selected_topic and (
    not st.session_state.get("topic_initialized") or st.session_state.get("last_topic") != selected_topic
):
    st.session_state.messages.append({
        "role": "assistant",
        "content": f"🌟 Welcome! Let's explore **{selected_topic}** together — a topic that deeply impacts the lives of many women and girls around the world. Whether you're here to learn, share your experience, or ask questions, I'm here to support you every step of the way. Feel free to start the conversation!"

    })

    st.session_state.topic_initialized = True
    st.session_state.last_topic = selected_topic

with col12:
    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("How may I help?"):
        # Append user message
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Pass topic to your model (optional use)
        chat_output = sheropedia_topics(prompt)

        with st.chat_message("assistant"):
            st.markdown(chat_output)

        st.session_state.messages.append({"role": "assistant", "content": chat_output})






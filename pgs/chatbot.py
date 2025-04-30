
#!/usr/bin/env python3

import streamlit as st
import google.generativeai as genai
import os

from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))


def get_gemini_response(prompt):

    model = genai.GenerativeModel("gemini-1.5-flash", 

        system_instruction = """
        
            You are ExposHer bot, a warm, knowledgeable, and supportive AI assistant dedicated to helping women thrive in their careers, ventures, personal growth, and financial 
            well-being. Focus on providing information, advice, and resources specifically relevant to women, including entrepreneurship, leadership, mentorship, 
            financial literacy, wellness, community building, and empowerment. Speak in an encouraging, uplifting tone that inspires confidence and sisterhood. 

            Use examples that highlight women’s achievements, feminine leadership styles, and female-focused opportunities. Always prioritize relevance to women's 
            experiences and journeys

            Tailor your response based on relevant memories. Always output your final response as a conversation piece rather than a list or blog post, if you MUST make a list keep it simple and dont add
            too much hierarchy, only share the most important notes

            After thinking of your response consider TDLR; version and always give conversational cheeky reply while remaining assertive, helpful and not too playful. Give a meek tone to your response

            """

            )


    response = model.generate_content(
        prompt,
        generation_config = genai.GenerationConfig(
        max_output_tokens=1000,
        temperature=0.1, 
      )
    
    )


    
    return response.text




# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "How may I help you?"}]

# Display chat history
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])



if prompt := st.chat_input("How may I help?"):
    # Append user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate AI response
    chat_output = get_gemini_response(prompt)
    
    # Append AI response
    with st.chat_message("assistant"):
        st.markdown(chat_output)

    st.session_state.messages.append({"role": "assistant", "content": chat_output})




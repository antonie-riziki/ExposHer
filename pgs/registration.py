import streamlit as st
import pandas as pd
import africastalking
import os
import sys
import requests
import google.generativeai as genai


sys.path.insert(1, './modules')

from upload_file_rag import get_qa_chain, query_system
from func import welcome_message, send_sms

from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

africastalking.initialize(
    username='EMID',
    api_key = os.getenv("AT_API_KEY")
)

sms = africastalking.SMS
airtime = africastalking.Airtime


@st.dialog("🈴 ExposHer Digital Passport")
def digital_passport(first_name, surname, phone_number, email, face_id):
	personal_details, profile_pic = st.columns(2)

	with personal_details:
		st.write(f"<h5 style='text-align: left; margin-bottom: 1px;'>🚺 {str.upper(first_name) + ' ' + str.upper(surname)}</h5>", unsafe_allow_html=True)
		st.write(f"<h5 style='text-align: left; margin-bottom: 1px;'>📬 P.O. Box 00200 </h5>", unsafe_allow_html=True)
		# st.write(f"<h5 style='text-align: left; margin-bottom: 1px;'>📌 {address}, Kenya</h5>", unsafe_allow_html=True)
		st.write(f"<h5 style='text-align: left; margin-bottom: 1px;'>📞 Tel: +254 {phone_number}</h5>", unsafe_allow_html=True)
		# st.write(f"<h5 style='text-align: left; margin-bottom: 1px;'>#️⃣ Site ID: MJ#{site_id}</h5>", unsafe_allow_html=True)
		st.write(f"<h5 style='text-align: left; margin-bottom: 1px;'>📧 Email: {email}</h5>", unsafe_allow_html=True)

	with profile_pic:
		
		if face_id is not None:
			st.image(face_id, width=600)

		else:
	 		st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSdvltpjF8BWal0iwevlrM8ccNwRJDGFxVS6g&s')

	st.write(f"<h5 style='text-align: center; margin-bottom: 1px;'>With Our digital profile you tracks your skills, funding history, mentorships, leadership milestones \nits a dynamic résumé grows with your career and connects you to opportunities instantly.</h5>", unsafe_allow_html=True)
	st.write(f"<h5 style='text-align: center; margin-bottom: 1px;'>📑 Terms and Conditions apply</h5>", unsafe_allow_html=True)

	welcome_message(fname, phone_number)



col1, col2 = st.columns(2)




with col1:
	with st.form(key="user_registration"):
	    st.subheader("Registration")
	    fname, sname = st.columns(2)
	    with fname:
	    	first_name = st.text_input("First Name")
	    with sname:
	    	surname = st.text_input("Surname")
	    
	    username = st.text_input('Username:')
	    email = st.text_input("Email: ")
	    phone_number = st.number_input("Phone Number:", value=None, min_value=0, max_value=int(10e10))
	    password = st.text_input('Passowrd', type="password")
	    confirm_password = st.text_input('Confirm password', type='password')
	    face_id = st.file_uploader('Profile Photo')

	    checkbox_val = st.checkbox("Subscribe to our Newsletter")

	    submit_personal_details = st.form_submit_button("Submit")

	    
	    if password != confirm_password:
	    	st.error('Password mismatch', icon='⚠️')

	    else:
		    
		    if not (email and password):
		    	st.warning('Please enter your credentials!', icon='⚠️')
		    	# st.toast('You Must Register your Personal Details', icon='⚠️')
		    else:
		    	st.success('Proceed to engaging with the system!', icon='👉')

		    	

		    	if submit_personal_details:
		    		digital_passport(first_name, surname, phone_number, email, face_id)


			        

	

	# st.write("Outside the form")


# def load_lottieurl(url: str):
# 	r = requests.get(url)
# 	if r.status_code != 200:
# 		return None
# 	else:
# 		return r.json()


with col2:
	# reg_lottie = load_lottieurl("https://lottie.host/701a9d68-8f75-41a1-8c96-3e4b026a3d3f/zeKp8UyfVz.json")
	# st_lottie(reg_lottie)
	st.image('https://www.opscstudy.com/wp-content/uploads/2024/11/Women-Empowerment_11zon-1.jpg', width=700)
	st.image('https://www.potential.com/wp-content/uploads/2022/11/bigstock-Strong-Power-Women-Day-Femini-458970043-Converted.png', width=800)
	st.image('https://innereyefoundation.org/wp-content/uploads/2024/08/women_empowerment.jpg', width=900)
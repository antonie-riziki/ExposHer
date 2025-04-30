import streamlit as st 
import sys



sys.path.insert(1, './models')
print(sys.path.insert(1, '../models/'))

from func import women_in_business, similar_ventures, angel_investors

from dotenv import load_dotenv

load_dotenv()



st.markdown(
    """
    <div class=title>
        <div style=" justify-content: center;">
            <h1 style="text-align: center; padding: 5px; color: #F52887;">sHerk💃</h1>
            <p style="text-align: center;">United in Strength. Driven by Sisterhood</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.image('https://imageio.forbes.com/specials-images/imageserve/65aebac3ef04a10bbceaa553/Women-can-do-it--Four-female-characters-walk-up-together-and-hold-arms--Girls-support/0x0.jpg?format=jpg&crop=2499,1666,x0,y165,safe&width=960', width=700)

@st.dialog('...')
def process_info():
    st.spinner()


st.write('Connecting you to Female Venture Investors')

col1, col2 = st.columns(2, border=True)

with col1:
    with st.form(key='Business Details', border=False):

        col1_1, col1_2 = st.columns(2)

        with col1_1:
            category = st.selectbox('Category Stage', ['Ideation', 'Prototype', 'Innovation', 'Startup', 'Business'])

            patent = st.selectbox('Patent', ['Yes', 'No'])

        with col1_2:
            industry = st.selectbox('Industry', ['Beauty', 'Banking', 'Software', 'Education', 'Transport', 'Sales', 'Telecommunications', 'Food & Bev', 'Logistics', 'Hardware'])

            business_registered = st.selectbox('Is it registered', ['Yes', 'No'])


        name = st.text_input(f'Venture name')

        description = st.text_area('Descripion: ')

        eqty_percentage = ['less than 10%', '10% - 20%', '20% - 30%', '30% - 40%', '40% - 50%', 'above 50%']
        equity = st.pills('Equity', eqty_percentage)

        col1_3, col1_4 = st.columns(2)

        with col1_3:
            negotiable = st.selectbox('Is it Negotiable', ['Yes', 'No'])

        with col1_4:
            sales = st.selectbox('Do you have Sales', ['Yes', 'No'])

        more_info = st.text_area('additional information...', height=70)

        submit = st.form_submit_button("Submit", use_container_width=True)


# prompt = f"I have this {category} in the {industry} which I would like to pitch for investment"
prompt = f"{industry}"


with col2:
    with st.expander('#### 👩‍💼Women Business Moguls', expanded=True):
        wib_response = women_in_business(prompt)
        wib_response
        

col11, col12 = st.columns(2)

with col11:

    with st.expander(f'#### 💡Similar {category} Ventures', expanded=True):
        sv_response = similar_ventures(prompt)
        sv_response
        

with col12:

    with st.expander('#### 👑Local Angel Investors', expanded=True):
        lai_response = angel_investors(prompt)
        lai_response
        




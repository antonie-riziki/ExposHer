import streamlit as st 



reg_page = st.Page("./pgs/registration.py", title="register", icon=":material/person_add:")
signin_page = st.Page("./pgs/signin.py", title="sign in", icon=":material/login:")
home_page = st.Page("./pgs/main.py", title="home page", icon=":material/home:")
sherk_page = st.Page("./pgs/sherk.py", title="sHerk", icon=":material/crowdsource:")
sheroes_page = st.Page("./pgs/sheroes.py", title="sHeroes", icon=":material/group_search:")
sheropedia_page = st.Page("./pgs/sheropedia.py", title="sHeropedia", icon=":material/female:")
market_page = st.Page("./pgs/market.py", title="HerMarket", icon=":material/finance_mode:")
power_page = st.Page("./pgs/power-circle.py", title="powHer circles", icon=":material/flash_auto:")
# assets_page = st.Page("./pgs/assets_tracking.py", title="asset tracking", icon=":material/speed:")
# value_page = st.Page("./pgs/value.py", title="market value", icon=":material/finance_chip:")
# td_page = st.Page("./pgs/technical_drawing.py", title="techical drawing", icon=":material/architecture:")
# three_d_page = st.Page("./pgs/three-dee.py", title="three d's", icon=":material/deployed_code:")
# damage_page = st.Page("./pgs/damage.py", title="damage assessment", icon=":material/flood:")
chatbot_page = st.Page("./pgs/chatbot.py", title="chatbot", icon=":material/chat:")



pg = st.navigation([reg_page, signin_page, home_page, sherk_page, sheroes_page, sheropedia_page, market_page, power_page, chatbot_page])

st.set_page_config(
    page_title="ExposHer",
    page_icon="♀️",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.echominds.africa',
        'Report a bug': "https://www.echominds.africa",
        'About': "# We are a leading Women in Tech solution, Try *ExposHer* and experience reality!"
    }
)

pg.run()




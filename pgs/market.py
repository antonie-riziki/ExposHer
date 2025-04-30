




import streamlit as st 
import sys



sys.path.insert(1, './models')
print(sys.path.insert(1, '../models/'))


from dotenv import load_dotenv

load_dotenv()



st.markdown(
    """
    <div class=title>
        <div style=" justify-content: center;">
            <h1 style="text-align: center; padding: 5px; color: #F52887;">Her Market</h1>
            <p style="text-align: center;">The Future is Female, and It's Connected.</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)


st.image('https://images.ctfassets.net/3h69mkdgxn20/18iLxwlffGYCoChVODSMAV/907ec010421a3e61db72370d763a6b0c/WIB_1.svg', width=900)



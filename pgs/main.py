
from __future__ import annotations

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
            <h1 style="text-align: center; padding: 5px; color: #F52887;">ExposHer💃</h1>
            <p style="text-align: center;">From Dreams to Ventures — Powered by Women</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.image('https://www.resonanceglobal.com/hubfs/iStock-1371551897.jpg', width=900)







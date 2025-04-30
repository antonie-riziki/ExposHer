
import pandas as pd
import streamlit as st 
import sys



sys.path.insert(1, './models')
sys.path.insert(1, './src')

print(sys.path.insert(1, '../models/'))


from func import welcome_message


from dotenv import load_dotenv

load_dotenv()


df = pd.read_csv(r'./src/power-circles.csv', encoding='latin1')

st.markdown(
    """
    <div class=title>
        <div style=" justify-content: center;">
            <h1 style="text-align: center; padding: 5px; color: #F52887;">PowHer Circles</h1>
            <p style="text-align: center;">Where Women's Ideas Find Wings</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)


st.image('https://t3.ftcdn.net/jpg/05/76/49/04/360_F_576490467_QVWFh6kDzU2zr49TJ8SoQepkoxDcCIuD.jpg', width=900)


@st.dialog('ℹ️ Confirm')
def accept_dialog():

    st.write('are you sure you want to connect with so & so')
    col1, col2 = st.columns(2)

    with col1:
        cancel_btn = st.button('Cancel', use_container_width=True)

    with col2:
        confirm_btn = st.button('Accept', use_container_width=True)

        if confirm_btn:
            # welcome_message()
            pass



st.write('Looking for power circle besties')


interest_map = {
    '🙏Prayer WorriHer': 'Prayer WorriHer',
    '🌟Glow Getters': 'Glow Getters',
    '🧘‍♀️Zen Queens': 'Zen Queens',
    '🩸Cycle Sisters': 'Cycle Sisters',
    '👙Closet Confession': 'Closet Confession',
    '✈️Travel Companion': 'Travel Companion',
    '🤑Money Honeyz': 'Money Honeyz',
    '👩‍💼She Means Biz': 'She Means Biz',
    '🤰Mama Bear': 'Mama Bear',
    '🔐SisterHood Secrets': 'SisterHood Secrets',
    '🐇Pet Lovers': 'Pet Lovers',
    '🖍️Crafty Baddies': 'Crafty Baddies',
    '📹Reel Sisters': 'Reel Sisters',
    '👩‍💻Code Queens': 'Code Queens',
    '🍿Binge Besties': 'Binge Besties',
    '🎧Music Girlie': 'Music Girlie',
    '📝Scribble Sisters': 'Scribble Sisters',
    '🌍Green Goddess': 'Green Goddess',
    '💇‍♀️Skinfluenzers': 'Skinfluenzers',
    '🧋Candle & Tea Queens': 'Candle & Tea Queens'
}



all_circles = [
    ['🙏Prayer WorriHer', '🌟Glow Getters', '🧘‍♀️Zen Queens', '🩸Cycle Sisters', '👙Closet Confession'],
    ['✈️Travel Companion', '🤑Money Honeyz', '👩‍💼She Means Biz', '🤰Mama Bear', '🔐SisterHood Secrets'],
    ['🐇Pet Lovers', '🖍️Crafty Baddies', '📹Reel Sisters', '👩‍💻Code Queens', '🍿Binge Besties'],
    ['🎧Music Girlie', '📝Scribble Sisters', '🌍Green Goddess', '💇‍♀️Skinfluenzers', '🧋Candle & Tea Queens']
]

selected_interest = None

for group_index, circle in enumerate(all_circles):
    cols = st.columns(len(circle))
    for i, emoji_label in enumerate(circle):
        if cols[i].button(emoji_label, key=f'circle_{group_index}-{i}', use_container_width=True):
            selected_interest = interest_map[emoji_label]  # map to plain text


if selected_interest:
    
    interest_group = df.groupby('interests')
    
    try:
        get_group = interest_group.get_group(selected_interest)
        st.dataframe(get_group.head())
    
        st.write(selected_interest)


        top_records = get_group.head(2)


        col_left, col_right = st.columns(2, border=True)


        for i, row in top_records.iterrows():
            target_col = col_left if i % 2 == 0 else col_right

            with target_col:
                personal_details, profile_pic = st.columns(2)

                with personal_details:
                    st.write(f"<h6 style='text-align: left; margin-bottom: 1px;'>🚺 {row['name'].upper()}</h6>", unsafe_allow_html=True)
                    st.write(f"<h6 style='text-align: left; margin-bottom: 1px;'>📬 P.O. Box 00200, {row['location']}</h6>", unsafe_allow_html=True)
                    st.write(f"<h6 style='text-align: left; margin-bottom: 1px;'>📞 Tel: +254 {str(row['phone_number'])}</h6>", unsafe_allow_html=True)
                    st.write(f"<h6 style='text-align: left; margin-bottom: 1px;'>👩‍💼 {row['profession']}</h6>", unsafe_allow_html=True)
                    st.write(f"<h6 style='text-align: left; margin-bottom: 1px;'>🏢 {row['company']}</h6>", unsafe_allow_html=True)

                with profile_pic:
                    st.image(
                        row['profile_pic'] if pd.notna(row['profile_pic']) else 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSdvltpjF8BWal0iwevlrM8ccNwRJDGFxVS6g&s',
                        width=150
                    )

                st.write(f"🥷{row['bio']}\n")
                st.write(f"😂Fun Fact: {row['fun_fact']}")

                action_col1, action_col2 = st.columns(2)

                with action_col1:
                    decline_btn = st.button('Decline', key=f'decline_{i}', use_container_width=True, icon=':material/cancel:')

                with action_col2:
                    accept_btn = st.button('Connect', key=f'connect_{i}', use_container_width=True, icon=':material/check_circle:')
                    
                    if accept_btn:
                        print(row['interests'][i], row['phone_number'][i])
                        connection_message(row['interests'], row['phone_number'])

                        # st.success(f"You connected with {row['name']}!")


    except KeyError:
        st.warning("No data found for this interest.")





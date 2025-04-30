import streamlit as st 
import sys



sys.path.insert(1, './models')
print(sys.path.insert(1, '../models/'))

from func import sheroes_context
from dotenv import load_dotenv

load_dotenv()



st.markdown(
    """
    <div class=title>
        <div style=" justify-content: center;">
            <h1 style="text-align: center; padding: 5px; color: #F52887;">sHeroes💃</h1>
            <p style="text-align: center;">Where She Grows, the World Grows</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)


st.image('https://media.licdn.com/dms/image/v2/D4D12AQHNH_niJw_hYA/article-cover_image-shrink_720_1280/article-cover_image-shrink_720_1280/0/1709360744146?e=2147483647&v=beta&t=X5p6sRLwnr_YVcpxw0gBU9t-Y_h61u7gm5xuOgjIYu4', width=900)



female_impact_sectors = {
    "🧠 Science & Research": [
        "Physics ",
        "Chemistry ",
        "Biology & Genetics ",
        "Medicine & Physiology ",
        "Environmental Science "
    ],
    "👩‍⚖️ Politics & Governance": [
        "Presidents & Prime Ministers ",
        "Human Rights Advocates ",
        "Law Reformers"
    ],
    "💡 Innovation & Technology": [
        "Programming & Computer Science ",
        "Tech Startups ",
        "AI & Robotics Engineers"
    ],
    "💼 Business & Finance": [
        "Female CEOs ",
        "Social Entrepreneurs ",
        "Finance & Investment Leadership"
    ],
    "📚 Education & Literacy": [
        "Global Literacy Campaigns ",
        "Founders of Women's Schools ",
        "Academic Leaders"
    ],
    "🎭 Arts & Culture": [
        "Literature ",
        "Film & Theatre ",
        "Visual Arts "
    ],
    "📣 Media & Journalism": [
        "Investigative Journalism ",
        "Women-Led Media Houses",
        "Podcasting Influencers"
    ],
    "💪 Activism & Social Justice": [
        "Anti-Racism Advocates ",
        "Gender Equality Leaders ",
        "Disability & LGBTQ+ Rights"
    ],
    "🧕 Religion & Faith Leadership": [
        "Women Pastors & Imams",
        "Faith-Based Reformers"
    ],
    "🌱 Environment & Climate Action": [
        "Environmentalists ",
        "Sustainable Development Innovators"
    ],
    "⚖️ Law & Justice": [
        "Supreme Court Justices ",
        "Women's Rights Lawyers"
    ],
    "⚕️ Health & Wellness": [
        "Maternal Health Champions",
        "Mental Health Advocates",
        "Global Health Leaders"
    ],
    "🏃‍♀️ Sports & Athletics": [
        "Olympic Athletes ",
        "Equal Pay Advocates"
    ],
    "🚀 Space & Aviation": [
        "Astronauts ",
        "Aerospace Engineers"
    ],
    "🚧 Infrastructure & Construction": [
        "Female Architects",
        "Inclusive Urban Planners"
    ],
    "💬 Communication & Linguistics": [
        "Language Preservation",
        "Feminist Linguists"
    ]
}

# st.title("🌍 Female Impact Sectors Around the World")

if 'selected_subsector' not in st.session_state:
    st.session_state.selected_subsector = None

col1, col2 = st.columns(2)

with col1:
    for sector, subsectors in female_impact_sectors.items():
        with st.expander(sector):
            for sub in subsectors:
                btn_key = f"{sector}-{sub}"
                if st.button(f"{sub}", key=btn_key):
                    st.session_state.selected_subsector = sub.strip()

with col2:
    selected_sub = st.session_state.selected_subsector
    if selected_sub:
        with st.expander(f"💡 {selected_sub}", expanded=True):
            response = sheroes_context(selected_sub)
            st.markdown(response, unsafe_allow_html=True)
        
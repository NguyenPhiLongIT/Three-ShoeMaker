import streamlit as st
from src.models.database import init_db, seed_data
from src.viewmodels.wiki_viewmodel import WikiViewModel
from src.viewmodels.indicator_viewmodel import IndicatorViewModel
from src.views.wiki_view import render_wiki_view
from src.views.trade_view import render_trade_view
from src.views.deeplearn_view import render_deeplearn_view

# Page configuration
st.set_page_config(
    page_title="Three-Shoemaker",
    page_icon="👞",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize database
init_db()
seed_data()

# Initialize session state
if 'current_wiki_id' not in st.session_state:
    st.session_state['current_wiki_id'] = None

# Sidebar navigation
st.sidebar.title("🎯 Three-Shoemaker")
page = st.sidebar.radio(
    "Navigation",
    ["📚 Wiki", "📈 Trade Indicators", "🤖 Deep Learning"]
)

# Page routing
if page == "📚 Wiki":
    wiki_vm = WikiViewModel()
    render_wiki_view(wiki_vm)

elif page == "📈 Trade Indicators":
    indicator_vm = IndicatorViewModel()
    indicator_vm.load_data()
    render_trade_view(indicator_vm.get_formatted_indicators())

elif page == "🤖 Deep Learning":
    render_deeplearn_view()

st.sidebar.divider()
st.sidebar.caption("Built with Algorit Long")

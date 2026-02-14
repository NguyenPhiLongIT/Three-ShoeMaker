import streamlit as st
import os

def render_trade_view(indicator_list):
    """Display trade indicators with ratings."""
    st.header("📈 Trade Indicators")
    
    if not indicator_list:
        st.info("No indicators found.")
        return
    
    for indicator in indicator_list:
        with st.container():
            col1, col2 = st.columns([1, 3])
            
            with col1:
                if indicator['image_path'] and os.path.exists(indicator['image_path']):
                    st.image(indicator['image_path'], use_column_width=True)
                else:
                    st.info("📊 No image")
            
            with col2:
                st.subheader(indicator['name'])
                st.markdown(f"**Rating:** {'⭐' * indicator['rating']}")
                st.markdown(f"_{indicator['description']}_")
                
                with st.expander("View Code"):
                    st.code(indicator['code'], language='python')
            
            st.divider()

import streamlit as st
import os

# Custom CSS for fixed card height
st.markdown("""
    <style>
    [data-testid="stVerticalBlock"] > [style*="flex-direction: column"] > [data-testid="stVerticalBlock"] {
        height: auto !important;
    }
    .stContainer {
        height: auto !important;
    }
    </style>
""", unsafe_allow_html=True)

def render_list(wiki_summaries):
    """Display wiki knowledge cards in list view."""
    st.header("📚 Wiki Knowledge Base")
    
    if not wiki_summaries:
        st.info("No wiki entries found.")
        return
    
    cols = st.columns(3)
    for idx, wiki in enumerate(wiki_summaries):
        with cols[idx % 3]:
            # Wrapper container with fixed total height
            with st.container(border=True):
                # Create a fixed-height container (450px total)
                st.markdown(f"""
                    <div style="display: flex; flex-direction: column; height: 150px; gap: 8px;">
                        <div style="height: 200px; background: #f0f0f0; border-radius: 4px; display: flex; align-items: center; justify-content: center; overflow: hidden;">
                """, unsafe_allow_html=True)
                
                # Image
                if wiki['image_path'] and os.path.exists(wiki['image_path']):
                    st.image(wiki['image_path'], use_column_width=True)
                else:
                    st.markdown('<span style="font-size: 48px;">📷</span>', unsafe_allow_html=True)
                
                st.markdown("</div>", unsafe_allow_html=True)
                
                # Title (fixed height, clipped if too long)
                st.markdown(f"""
                    <div style="height: 60px; overflow: hidden; display: flex; align-items: center;">
                        <h3 style="margin: 0; word-wrap: break-word; line-height: 1.2;">{wiki['title']}</h3>
                    </div>
                """, unsafe_allow_html=True)
                
                # Tags section (flexible height)
                tags_html = ""
                if wiki['tags']:
                    tag_str = " ".join([f"🏷️ {tag.strip()}" for tag in wiki['tags']])
                    tags_html = f"<p style='margin: 4px 0; font-size: 12px; color: #666;'>{tag_str}</p>"
                
                st.markdown(f"""
                    <div style="flex: 1; display: flex; flex-direction: column; justify-content: flex-end;">
                        {tags_html}
                    </div>
                """, unsafe_allow_html=True)
                
                # Close main flex container
                st.markdown("</div>", unsafe_allow_html=True)
                
                # Button (outside the fixed container)
                if st.button("📖 Xem Chi Tiết", key=f"wiki_{wiki['id']}", use_container_width=True):
                    st.session_state['current_wiki_id'] = wiki['id']
                    st.rerun()

def render_detail(wiki_detail):
    """Display full article detail view."""
    # Back button
    col1, col2 = st.columns([0.1, 0.9])
    with col1:
        if st.button("⬅️ Quay Lại"):
            st.session_state['current_wiki_id'] = None
            st.rerun()
    
    st.divider()
    
    # Display full article
    st.title(wiki_detail['title'])
    
    # Display image
    if wiki_detail['image_path'] and os.path.exists(wiki_detail['image_path']):
        st.image(wiki_detail['image_path'], use_column_width=True)
    
    # Display tags
    if wiki_detail['tags']:
        tag_str = " ".join([f"🏷️ {tag.strip()}" for tag in wiki_detail['tags']])
        st.caption(tag_str)
    
    st.divider()
    
    # Display content
    st.markdown(wiki_detail['content'])

def render_wiki_view(wiki_vm):
    """Main wiki view handler - routes between list and detail."""
    current_wiki_id = st.session_state.get('current_wiki_id')
    
    if current_wiki_id is None:
        # List view
        summaries = wiki_vm.get_all_summaries()
        render_list(summaries)
    else:
        # Detail view
        detail = wiki_vm.get_article_detail(current_wiki_id)
        if detail:
            render_detail(detail)
        else:
            st.error("Article not found.")
            if st.button("⬅️ Quay Lại"):
                st.session_state['current_wiki_id'] = None
                st.rerun()

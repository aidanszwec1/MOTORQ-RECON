#!/usr/bin/env python3
import streamlit as st

st.set_page_config(
    page_title="Reconciliation Tools",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Invoice Reconciliation Tools")
st.markdown("Choose which reconciliation tool you want to use:")

# Create two columns for the different tools
col1, col2 = st.columns(2)

with col1:
    st.subheader("🚗 Motorq Reconciliation")
    st.markdown("""
    **Use this for:**
    - Motorq invoice reconciliation
    - Comparing ALL_MOTORQ CSV with Motorq invoice XLSX
    - VIN matching with days enrolled data
    """)
    if st.button("Launch Motorq Tool", type="primary", use_container_width=True):
        st.markdown("**To launch Motorq Reconciliation:**")
        st.code("streamlit run streamlit_apps/motorq_reconciliation.py", language="bash")

with col2:
    st.subheader("🚙 Mercedes-Benz Reconciliation")
    st.markdown("""
    **Use this for:**
    - Mercedes-Benz invoice reconciliation
    - Comparing ALL_MERCEDES CSV with Mercedes invoice CSV
    - Short VIN to full VIN matching
    """)
    if st.button("Launch Mercedes Tool", type="primary", use_container_width=True):
        st.markdown("**To launch Mercedes-Benz Reconciliation:**")
        st.code("streamlit run streamlit_apps/mercedes_reconciliation.py", language="bash")

st.markdown("---")

# Instructions section
with st.expander("🚀 Getting Started", expanded=True):
    st.markdown("""
    ### Setup Instructions:
    
    1. **Install dependencies** (one-time setup):
    ```bash
    pip install -r streamlit_apps/requirements.txt
    ```
    
    2. **Launch a specific tool**:
    ```bash
    # For Motorq reconciliation
    streamlit run streamlit_apps/motorq_reconciliation.py
    
    # For Mercedes-Benz reconciliation
    streamlit run streamlit_apps/mercedes_reconciliation.py
    ```
    
    ### What these tools do:
    - **Drag & drop interface** for uploading files
    - **Automated reconciliation** using existing Python scripts
    - **Download results** as Excel files
    - **No terminal or Python knowledge required** for end users
    
    ### File Requirements:
    - **Motorq**: ALL_MOTORQ CSV + Motorq invoice XLSX
    - **Mercedes**: ALL_MERCEDES CSV + Mercedes invoice CSV
    """)

st.markdown("---")
st.markdown("*Invoice Reconciliation Tools - Making reconciliation accessible to everyone*")

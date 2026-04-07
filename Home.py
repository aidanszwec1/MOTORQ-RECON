#!/usr/bin/env python3
import streamlit as st

st.set_page_config(
    page_title="Reconciliation Tools",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Invoice Reconciliation Tools")
st.markdown("Choose which reconciliation tool you want to use from the sidebar.")

# Instructions section
st.markdown("""
## 🚀 Welcome to the Invoice Reconciliation Suite

This application provides easy-to-use tools for reconciling invoice data with internal records. 
No Python knowledge required - just upload your files and download the results!

### Available Tools:
- **🚗 Motorq Reconciliation**: Compare Motorq invoice data with internal ALL_MOTORQ records
- **🚙 Mercedes-Benz Reconciliation**: Compare Mercedes invoice data with internal ALL_MERCEDES records

### How to Use:
1. Select a tool from the sidebar
2. Upload your data files using the drag-and-drop interface
3. Click "Run Reconciliation" 
4. Download your results as an Excel file

### Need Help?
Each tool includes detailed instructions and file format requirements. 
Check the expandable "Instructions" section on each page for specific guidance.
""")

st.markdown("---")

# Quick stats or info
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Tools Available", "2")

with col2:
    st.metric("File Formats", "CSV, XLSX")

with col3:
    st.metric("Output Format", "Excel")

st.markdown("---")
st.markdown("*Invoice Reconciliation Tools - Making reconciliation accessible to everyone*")

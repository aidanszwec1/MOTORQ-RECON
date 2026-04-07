#!/usr/bin/env python3
import streamlit as st
import pandas as pd
import tempfile
import os
import sys
from pathlib import Path

# Add the scripts directory to the path so we can import the motorq_recon module
script_dir = Path(__file__).parent.parent.parent / "scripts"
sys.path.append(str(script_dir))

try:
    from motorq_recon import run as motorq_run
except ImportError:
    st.error("Could not import motorq_recon module. Please ensure the scripts/motorq_recon.py file exists.")
    st.stop()

st.set_page_config(
    page_title="Motorq Reconciliation",
    page_icon="🚗",
    layout="wide"
)

st.title("🚗 Motorq Invoice Reconciliation")
st.markdown("Upload the internal Motorq CSV and the invoice XLSX, then run the reconciliation.")

# Create two columns for file uploads
col1, col2 = st.columns(2)

with col1:
    st.subheader("Internal Motorq Data (CSV)")
    internal_file = st.file_uploader(
        "Upload ALL_MOTORQ CSV file",
        type=['csv'],
        help="Expected format: CSV with VIN and DAYS_ENROLLED columns",
        key="internal"
    )
    if internal_file:
        st.success(f"✅ {internal_file.name} uploaded ({internal_file.size} bytes)")

with col2:
    st.subheader("Motorq Invoice (XLSX)")
    invoice_file = st.file_uploader(
        "Upload Motorq invoice XLSX file", 
        type=['xlsx'],
        help="Expected format: XLSX with 'Invoice_Detail' sheet containing VIN/fleetUnitId column",
        key="invoice"
    )
    if invoice_file:
        st.success(f"✅ {invoice_file.name} uploaded ({invoice_file.size} bytes)")

# Run reconciliation button
if st.button("🔄 Run Reconciliation", type="primary", use_container_width=True):
    if not internal_file or not invoice_file:
        st.error("❌ Please upload both files before running the reconciliation.")
    else:
        with st.spinner("Running reconciliation..."):
            try:
                # Create temporary files
                with tempfile.TemporaryDirectory() as temp_dir:
                    # Save uploaded files to temporary directory
                    internal_path = os.path.join(temp_dir, "internal_data.csv")
                    invoice_path = os.path.join(temp_dir, "invoice_data.xlsx")
                    output_path = os.path.join(temp_dir, "MOTORQ_RECON_OUTPUT.xlsx")
                    
                    # Write uploaded files
                    with open(internal_path, "wb") as f:
                        f.write(internal_file.getbuffer())
                    
                    with open(invoice_path, "wb") as f:
                        f.write(invoice_file.getbuffer())
                    
                    # Run the reconciliation
                    motorq_run(internal_path, invoice_path, output_path)
                    
                    # Read the output file for download
                    with open(output_path, "rb") as f:
                        output_data = f.read()
                    
                    # Display success message and download button
                    st.success("✅ Reconciliation completed successfully!")
                    
                    # Create download button
                    st.download_button(
                        label="📥 Download Reconciliation Results",
                        data=output_data,
                        file_name=f"MOTORQ_RECON_{pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')}.xlsx",
                        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                        use_container_width=True
                    )
                    
                    # Show preview of results
                    st.subheader("📊 Reconciliation Summary")
                    
                    # Read the summary sheet to show key metrics
                    try:
                        summary_df = pd.read_excel(output_path, sheet_name="Summary")
                        
                        # Display metrics in columns
                        metrics_col1, metrics_col2 = st.columns(2)
                        
                        for idx, row in summary_df.iterrows():
                            metric_name = row['Metric']
                            metric_value = row['Value']
                            
                            if idx % 2 == 0:
                                with metrics_col1:
                                    st.metric(metric_name, metric_value)
                            else:
                                with metrics_col2:
                                    st.metric(metric_name, metric_value)
                        
                        # Show the summary table
                        st.dataframe(summary_df, use_container_width=True)
                        
                    except Exception as e:
                        st.warning(f"Could not display summary preview: {e}")
                    
            except Exception as e:
                st.error(f"❌ Error during reconciliation: {str(e)}")
                st.error("Please check that your files are in the correct format and try again.")

# Instructions section
with st.expander("📋 Instructions", expanded=False):
    st.markdown("""
    ### How to use this tool:
    
    1. **Internal Motorq Data (CSV)**: Upload your ALL_MOTORQ CSV file containing VIN and DAYS_ENROLLED columns
    2. **Motorq Invoice (XLSX)**: Upload the Motorq invoice Excel file with an 'Invoice_Detail' sheet
    3. Click **Run Reconciliation** to process the files
    4. Download the results Excel file when processing is complete
    
    ### Output file contains:
    - **Summary**: Overall reconciliation metrics
    - **ByProduct**: VIN counts by Motorq product
    - **OnInvoice_NotInInternal**: VINs on invoice but missing in internal data
    - **InInternal_NotOnInvoice**: VINs in internal data but missing on invoice
    - **Matches**: VINs that match between both datasets
    
    ### File format requirements:
    - **CSV file**: Must contain 'VIN' and 'DAYS_ENROLLED' columns
    - **XLSX file**: Must contain 'Invoice_Detail' sheet with 'VIN/fleetUnitId' column
    """)

# Footer
st.markdown("---")
st.markdown("*Motorq Invoice Reconciliation Tool - Automated reconciliation between internal data and invoices*")

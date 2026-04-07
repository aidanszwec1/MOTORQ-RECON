# Motorq Invoice Reconciliation Tool

A Streamlit web application for reconciling Motorq invoice data with internal records.

## 🚀 Quick Start

### Local Development
```bash
pip install -r requirements.txt
streamlit run app.py
```

### Streamlit Cloud Deployment
1. Push this repository to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Deploy with:
   - Repository: `YOUR_USERNAME/MOTORQ-RECON`
   - Branch: `main`
   - Main file path: `app.py`

## 📊 Features

- **Drag & Drop Interface**: Easy file uploads
- **Automated Reconciliation**: Matches VINs between internal data and invoices
- **Excel Output**: Formatted results with multiple sheets
- **Real-time Summary**: Key metrics displayed immediately

## 📁 File Requirements

- **Internal Data**: CSV with VIN and DAYS_ENROLLED columns
- **Invoice Data**: XLSX with Invoice_Detail sheet containing VIN/fleetUnitId column

## 🔧 Output Sheets

- **Summary**: Overall reconciliation metrics
- **ByProduct**: VIN counts by Motorq product
- **OnInvoice_NotInInternal**: VINs on invoice but missing internally
- **InInternal_NotOnInvoice**: VINs in internal data but missing on invoice
- **Matches**: VINs that match between both datasets

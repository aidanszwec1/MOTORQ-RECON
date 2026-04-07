# Invoice Reconciliation Streamlit Dashboards

This folder contains user-friendly Streamlit dashboards that wrap the existing Python reconciliation scripts, making them accessible to coworkers without requiring Python or terminal knowledge.

## 🚀 Quick Start

### 1. Install Dependencies (One-time setup)
```bash
pip install -r streamlit_apps/requirements.txt
```

### 2. Launch a Dashboard
```bash
# For Motorq reconciliation
streamlit run streamlit_apps/motorq_reconciliation.py

# For Mercedes-Benz reconciliation  
streamlit run streamlit_apps/mercedes_reconciliation.py

# For the main launcher (shows both options)
streamlit run streamlit_apps/main_launcher.py
```

## 📊 Available Tools

### 🚗 Motorq Reconciliation (`motorq_reconciliation.py`)
- **Purpose**: Reconcile Motorq invoice data with internal ALL_MOTORQ data
- **Input Files**: 
  - ALL_MOTORQ CSV (with VIN and DAYS_ENROLLED columns)
  - Motorq invoice XLSX (with Invoice_Detail sheet containing VIN/fleetUnitId column)
- **Output**: Excel file with reconciliation results including matches, mismatches, and summary metrics

### 🚙 Mercedes-Benz Reconciliation (`mercedes_reconciliation.py`)
- **Purpose**: Reconcile Mercedes-Benz invoice data with internal ALL_MERCEDES data
- **Input Files**:
  - ALL_MERCEDES CSV (with VIN and STATUS columns)
  - Mercedes invoice CSV (with VINs in column C)
- **Output**: Excel file with reconciliation results using last-7-character VIN matching

## 📁 File Structure
```
streamlit_apps/
├── README.md                    # This file
├── requirements.txt             # Python dependencies
├── main_launcher.py            # Main launcher showing both tools
├── motorq_reconciliation.py    # Motorq reconciliation dashboard
└── mercedes_reconciliation.py  # Mercedes reconciliation dashboard
```

## 🎯 How to Use Each Dashboard

### General Workflow:
1. **Launch the dashboard** using the streamlit command
2. **Upload files** using the drag-and-drop interface:
   - Upload internal data file (CSV)
   - Upload invoice file (CSV/XLSX depending on tool)
3. **Click "Run Reconciliation"** to process the files
4. **Download the results** Excel file when processing completes
5. **Review the summary metrics** displayed on screen

### File Format Requirements:

#### Motorq Tool:
- **Internal CSV**: Must contain `VIN` and `DAYS_ENROLLED` columns
- **Invoice XLSX**: Must contain `Invoice_Detail` sheet with `VIN/fleetUnitId` column

#### Mercedes Tool:
- **Internal CSV**: Must contain `VIN` and `STATUS` columns  
- **Invoice CSV**: Must have VINs in column C (3rd column)

## 📈 Output Files

Both tools generate Excel files with multiple sheets:

### Motorq Output Sheets:
- **Summary**: Overall reconciliation metrics
- **ByProduct**: VIN counts by Motorq product
- **OnInvoice_NotInInternal**: VINs on invoice but missing in internal data
- **InInternal_NotOnInvoice**: VINs in internal data but missing on invoice
- **Matches**: VINs that match between both datasets

### Mercedes Output Sheets:
- **Summary**: Overall reconciliation metrics including match counts
- **Matches**: Short VINs from invoice matched to full VINs in internal data
- **OnInvoice_NotInInternal**: Short VINs on invoice but missing in internal data
- **InInternal_NotOnInvoice**: VINs in internal data but missing on invoice

## 🔧 Technical Details

### Dependencies:
- `streamlit>=1.28.0` - Web dashboard framework
- `pandas>=2.0.0` - Data processing
- `openpyxl>=3.1.0` - Excel file handling

### How It Works:
1. **File Upload**: Files are temporarily stored during processing
2. **Script Execution**: Calls the existing Python reconciliation scripts
3. **Result Generation**: Creates Excel output with formatted sheets
4. **Download**: Provides downloadable results with timestamp

### Security:
- All file processing happens locally
- Temporary files are automatically cleaned up
- No data is stored permanently by the dashboard

## 🐛 Troubleshooting

### Common Issues:

**"Could not import module" error:**
- Ensure you're running from the correct directory
- Check that the `scripts/` folder contains the reconciliation Python files

**File format errors:**
- Verify your CSV/XLSX files have the required columns
- Check that VIN columns contain valid data
- Ensure file encoding is UTF-8

**Memory issues with large files:**
- The tools can handle reasonably large files (tested up to 200MB)
- For very large files, consider splitting them or running the Python scripts directly

### Getting Help:
- Check the file format requirements in the dashboard instructions
- Review error messages displayed in the dashboard
- Ensure all required columns are present in your data files

## 📞 For Coworkers

These dashboards are designed to be simple and user-friendly:

1. **No Python knowledge required** - just drag, drop, and click
2. **Clear instructions** built into each dashboard
3. **Error messages** help identify file format issues
4. **Automatic file naming** with timestamps for downloaded results
5. **Summary metrics** displayed immediately after processing

Simply follow the on-screen instructions and you'll have your reconciliation results in minutes!

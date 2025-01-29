
import tabula
import pandas as pd

pdf_path = 'stock_market.pdf'

output_excel_path = 'extracted_tables.xlsx'

tables = tabula.read_pdf(
    pdf_path,
    pages='all',
    multiple_tables=True,
    pandas_options={'header': None},
    # Try using 'stream' mode if tables are without lines; switch to 'lattice' if needed
    stream=True
)

merged_tables = []
current_table = None

for df in tables:
    if df.empty:
        continue  
    
    if current_table is None:
        current_table = df
        continue
    
    if (df.shape[1] == current_table.shape[1]) and (df.iloc[0].tolist() == current_table.iloc[0].tolist()):
        current_table = pd.concat([current_table, df.iloc[1:]], ignore_index=True)
    else:
        merged_tables.append(current_table)
        current_table = df

if current_table is not None:
    merged_tables.append(current_table)

with pd.ExcelWriter(output_excel_path, engine='openpyxl') as writer:
    for i, df in enumerate(merged_tables):
        sheet_name = f'Table_{i+1}'
        df.to_excel(writer, sheet_name=sheet_name, index=False, header=False)

print(f"Extracted and merged tables saved to {output_excel_path}")

import pandas as pd

file_path = "extracted_tables.xlsx"  
xls = pd.ExcelFile(file_path)

cleaned_tables = {}

for sheet_name in xls.sheet_names:
    df = pd.read_excel(xls, sheet_name=sheet_name, header=0)  
    df = df.dropna(how='all')  
    df = df.astype(str).replace(",", "", regex=True) 
    for col in df.columns:
        try:
            df[col] = pd.to_numeric(df[col])  
        except ValueError:
            try:
                df[col] = pd.to_datetime(df[col]).dt.strftime('%Y-%m-%d')  
            except ValueError:
                pass  
    df = df.astype(str).replace("nan", "", regex=True) 
    cleaned_tables[sheet_name] = df

cleaned_file_path = "cleaned_extracted_tables.xlsx"
with pd.ExcelWriter(cleaned_file_path, engine="openpyxl") as writer:
    for sheet_name, df in cleaned_tables.items():
        df.to_excel(writer, sheet_name=sheet_name, index=False)

print(f"Cleaned tables saved to {cleaned_file_path}")

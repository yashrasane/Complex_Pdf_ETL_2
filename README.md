# PDF ETL (Extract, Transform, Load) Pipeline
## Overview
This project is a Python-based ETL pipeline designed to process complex, unstructured PDF documents. It extracts text and tabular data, validates and preprocesses the data, and exports it to an Excel file. The project also includes mechanisms to detect whether preprocessing is required and handle missing or invalid data.

## Dataset used
- <a href="https://github.com/yashrasane/Complex_Pdf_ETL_2/blob/8c8dbb220d799c08a36890ad30fb7f75d25cb0a5/stock_market_dataset.pdf">Dataset</a>

## Features
-Extracts text and tabular data from PDFs using pdfplumber.

-Parses structured information, such as company details, document type, and financial data.

-Validates data for missing values, non-numeric entries, invalid date formats, and duplicates.

-Preprocesses data (handles missing values, converts data types, standardizes date formats, removes duplicates).

-Exports clean, structured data to an Excel file for further use.

-(Optional) Stores processed data in a database for future analysis.

Excel Interaction <a href="https://github.com/yashrasane/Complex_Pdf_ETL_2/blob/8c8dbb220d799c08a36890ad30fb7f75d25cb0a5/cleaned_extracted_tables.xlsx">View Output</a>

## Dependencies
-tabula (for PDF parsing)

-pandas (for data handling and export)

-re (for regular expressions)


## Dashboard

![Screenshot (495)](https://github.com/yashrasane/Complex_Pdf_ETL_2/blob/70e88df111f973c7fde6a9162b17772a841f6aa9/cleaned_extracted_tables.jpg)

## Code Highlights
-Data Extraction: Utilizes tabula to extract tables from unstructured PDFs.

-Data Cleaning:Handles missing and invalid data in numeric and date fields.Removes duplicate rows.

-Flexible Pipeline:Skips preprocessing if the data is already clean.

-Outputs results directly to an Excel file.

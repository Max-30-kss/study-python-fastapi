import pandas as pd

# CSV в XLSX
def csv_to_xlsx(csv_file, xlsx_file):
    df = pd.read_csv(csv_file)
    df.to_excel(xlsx_file, index=False, engine='openpyxl')

# XLSX в CSV
def xlsx_to_csv(xlsx_file, csv_file):
    df = pd.read_excel(xlsx_file, engine='openpyxl')
    df.to_csv(csv_file, index=False)
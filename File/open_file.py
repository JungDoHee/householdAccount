import pandas as pd
import os

def openFile(filename, start_header):
    ext = filename.split('.')[-1].lower()
    try:
        if ext == 'xls':
            return pd.read_excel(filename, engine='xlrd', header=start_header)
        elif ext == 'xlsx' : 
            return pd.read_excel(filename, engine='openpyxl', header=start_header)
    except Exception as e :
        temp_file = pd.read_html(filename, encoding='utf8')
        df = temp_file[len(temp_file)-1]
        df.to_excel(filename+'x', index=False, engine='openpyxl')
        if os.path.exists(filename):
            os.remove(filename)
        return pd.read_excel(filename+'x', engine='openpyxl', header=start_header)
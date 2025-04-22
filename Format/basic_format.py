import re

def normalizeDateFomat(date_str) :
    if not isinstance(date_str, str) : 
        date_str = str(date_str)
    if '년' in date_str and '월' in date_str and '일' in date_str : 
        return re.sub(r'(\d{4})년\s*(\d{1,2})월\s*(\d{1,2})일', r'\1-\2-\3', date_str)
    elif '.' in date_str : 
        return date_str.replace('.', '-')
    elif '/' in date_str : 
        parts = date_str.split('/')
        if len(parts[2]) == 4 : 
            return f"{parts[2]}-{int(parts[0]):02}-{int(parts[1]):02}"
    return date_str

def numberFormat(number) : 
    return number.apply('{:,}'.format)
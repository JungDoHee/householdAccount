def getReplaceHeader(account_type) : 
    account_type = account_type.lower()
    if account_type == 'kb' : 
        replace_text = {'이용일자' : '결제일', '이용카드명' : '이용카드', '이용하신곳' : '사용처', '국내이용금\n액\n(원)' : '지출금액'}
    elif account_type == 'hyundaicard' :
        replace_text = {'이용일' : '결제일', '이용하신곳':'사용처', '이용금액' : '지출금액'}
    elif account_type == 'lt' : 
        replace_text = {'이용일자' : '결제일', '이용카드' : '이용카드', '이용가맹점' : '사용처', '이용금액' : '지출금액', '취소금액':'수입금액'}
    return replace_text

def getHeaderList(account_type) : 
    account_type = account_type.lower()
    headerList = []
    if account_type == 'kb' : 
        headerList = [0, 3, 4, 5, 11]
    elif account_type == 'hyundaicard' : 
        headerList = [0, 9, 4, 5, 10]
    elif account_type == 'lt' : 
        headerList = [0, 2, 3, 5, 11]
    return headerList

def getStartHeader(account_type) : 
    account_type = account_type.lower()
    header = 0
    if account_type == 'kb' : 
        header = 6
    elif account_type == 'hyundaicard' : 
        header = 2
    return header
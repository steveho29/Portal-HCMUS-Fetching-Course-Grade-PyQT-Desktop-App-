import requests
from bs4 import BeautifulSoup
from crypto import decrypt


def fetchPortal():
    credential = decrypt(open('credential.key', 'r').read()).split('%')
    username, password = credential[0], credential[1]

    data = {
        'dnn$ctr$Login$Login_DNN$txtUsername': username,
        'dnn$ctr$Login$Login_DNN$txtPassword': password,
        'dnn$ctr$Login$Login_DNN$cmdLogin': 'Login',
    }
    link = 'https://portal.ctdb.hcmus.edu.vn/Login?returnurl=/sinh-vien/ket-qua-hoc-phan'
    with requests.session() as session:
        response = session.get(url=link)

        soup = BeautifulSoup(response.text, features="html.parser")

        inputId = ['StylesheetManager_TSSM', 'ScriptManager_TSM',
                   '__VIEWSTATE', '__VIEWSTATEGENERATOR', '__VIEWSTATEENCRYPTED',
                   '__EVENTVALIDATION']
        for id in inputId:
            data[id] = soup.find('input', id=id).get('value')

        response = requests.post(url=link, data=data)
        print(response)

        soup = BeautifulSoup(response.text, features='html.parser')
        subjects = soup.select('tbody > tr')
        info = soup.select('#dnn_ctr479_ViewSVKQHocPhan_h4DiemTB > span')
        print(f'Number Subjects: {len(subjects)}')
        info = [x.text.strip() for x in info]

        data = {
            info[0]: ['', info[1]],
        }
        for s in subjects:
            subject = s.select('td')
            code = subject[1].text
            name = subject[2].text
            point = subject[-3].text.strip('\n')
            print(f'{code} {name} {point}')
            data[code] = [name, point]

        return data











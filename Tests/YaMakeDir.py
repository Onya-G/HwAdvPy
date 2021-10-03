import requests

YA_TOKEN = ''
DIRNAME = 'new folder'
URL = 'https://cloud-api.yandex.net/v1/disk/resources/'


def get_headers():
    return {
        'Content-Type': 'application/json',
        'Authorization': 'OAuth {}'.format(YA_TOKEN)
    }


def get_files_list():
    params = {'path': '/'}
    headers = get_headers()
    resp = requests.get(url=URL, headers=headers, params=params)
    return resp.text


def make_dir(dir_name):
    url = 'https://cloud-api.yandex.net/v1/disk/resources/'
    params = {'path': dir_name}
    headers = get_headers()
    requests.put(url=url, headers=headers, params=params)
    return requests.get(url=url, headers=headers, params=params)


if __name__ == '__main__':
    print(make_dir(DIRNAME))

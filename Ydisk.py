import requests


class ApiYDisk:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def create_directory(self, path):
        url = "https://cloud-api.yandex.net/v1/disk/resources"
        params = {"path": path}
        response = requests.put(url, headers=self.get_headers(), params=params)

    def upload_photo_max_size(self, photo):
        url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        response = requests.post(url, params={"url": photo['biggest_photo'], "path":  photo['file_path'], "overwrite": "true"}, headers=self.get_headers())
        response.raise_for_status()
        if response.status_code == 200:
            print("Success")

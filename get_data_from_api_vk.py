import requests


class ApiVK:
    def __init__(self, token: str):
        self.token = token

    def get_photo_from_profile(self, owner_id: str):
        url = 'https://api.vk.com/method/photos.get'
        params = {
            'owner_id': owner_id,
            'album_id': 'wall',
            'access_token': self.token,
            'extended': 1,
            'photo_sizes': 1,
            'v': '5.131'
        }
        return (requests.get(url, params=params)).json().get('response', dict).get('items', [])
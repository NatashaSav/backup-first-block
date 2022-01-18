from operator import itemgetter

from progress.bar import Bar

from get_data_from_api_vk import ApiVK
from Ydisk import ApiYDisk


class Backup:

    def __init__(self, vk_token: str, ya_disk_token: str):
        self.vk_client = ApiVK(vk_token)
        self.ya_client = ApiYDisk(ya_disk_token)

    def get_max_size_photo(self, photo: list):
        photo.sort(key=itemgetter('height'), reverse=True)
        return dict(
            biggest_photo=photo[0]['url'],
            size=photo[0]['type']
        )

    def backup(self, owner_id: str = '698870636'):
        all_values = list()
        backup_path = 'backup-' + owner_id
        self.ya_client.create_directory(backup_path)
        photos = self.vk_client.get_photo_from_profile(owner_id)
        bar = Bar('Processing', max=len(photos))
        for item in photos:
            photo = self.get_max_size_photo(item.get('sizes'))
            count_like = item['likes']['count']
            photo["count_like_for_photo"] = count_like
            photo["data_about_upload_photo"] = item['date']
            photo["file_name"] = str(count_like) + str('-') + str(item['date']) + '.jpg'
            photo["file_path"] = "{}/{}".format(backup_path, photo["file_name"])
            self.ya_client.upload_photo_max_size(photo)
            bar.next()
            all_values.append(dict(filename=photo['file_name'], size=photo["size"]))
        bar.finish()
        return all_values


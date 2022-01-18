import json

from backup import Backup

if __name__ == '__main__':
    with open('token.txt', 'r') as file_object:
        token = file_object.read().strip()
    with open('token_from_poligon.txt', 'r') as file_object:
        poligon_token = file_object.read().strip()
    saved_data = Backup(token, poligon_token)
    backup_data = saved_data.backup()
    with open('backup_data.json', 'w') as file:
        file.write(json.dumps(backup_data, indent="\t"))
    file.close()




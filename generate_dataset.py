import json
import os
import pandas as pd


def get_position_by_id(id):
    filter = dataframe['ID'] == id
    position = dataframe.loc[filter, 'Posição'].values
    if len(position) > 0:
        return position[0]
    else:
        return None


def get_rgb_by_id(id):
    filter = dataframe['ID'] == id
    rgb = dataframe.loc[filter, 'RGB'].values
    if len(rgb) > 0:
        return rgb[0]
    else:
        return None


def get_files_in_folder(folder_path):
    file_list = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_list.append(file_path)
    return file_list


def get_following(files, username):

    following = []

    for file in files:
        with open(file, 'r') as file_user:

            json_user = json.load(file_user)

            if username in set(json_user['followers']) and username != json_user['username']:
                following.append(json_user['username'])

    return following


if __name__ == "__main__":
    files = get_files_in_folder('./dataset')
    final_json = []

    dataframe = pd.read_csv('dataID.csv', delimiter=';')

    print(dataframe)

    for file in files:

        with open(file, 'r') as file_user:
            json_user = json.load(file_user)

            json_user['followers'].remove(json_user['username'])

            new_json = {
                'username': json_user['username'],
                'position': get_position_by_id(json_user['username']),
                'color': get_rgb_by_id(json_user['username']),
                'following': get_following(files, json_user['username']),
                'followers': json_user['followers']
            }

            if len(new_json['followers']) != 0 or len(new_json['following']) != 0:
                final_json.append(new_json)

    with open(f'dataset.json', "w") as arquivo:
        json.dump(final_json, arquivo, indent=4)

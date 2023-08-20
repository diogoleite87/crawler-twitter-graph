import json
import matplotlib.pyplot as plt
import numpy as np


def graphic_follow_position_pie(json_file, username, follow_type, title):

    direita = 0
    esquerda = 0
    centro = 0

    list_users = []

    for item in json_file:
        if item['username'] == username:
            if follow_type == 1:
                list_users = item['following']
            else:
                list_users = item['followers']

    for item in json_file:
        if item['username'] in list_users:
            if item['position'] == 'esquerda':
                esquerda += 1
            elif item['position'] == 'direita':
                direita += 1
            else:
                centro += 1

    labels = ['Esquerda', 'Direita', 'Centro']
    sizes = [esquerda, direita, centro]
    colors = ['#ff9999', '#66b3ff', '#99ff99']
    explode = (0.1, 0, 0)

    plt.figure(figsize=(8, 6))

    def func(pct, allvalues):
        absolute = int(np.round(pct/100.*np.sum(allvalues)))
        return "{:.1f}%\n({:d})".format(pct, absolute)

    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
            autopct=lambda pct: func(pct, sizes), shadow=True, startangle=140,
            pctdistance=0.85, wedgeprops={'edgecolor': 'black'})

    plt.title(username, fontsize=16)
    plt.axis('equal')
    plt.title(username)

    if follow_type == 1:
        plt.savefig(
            f'./followingGraphicsPie/seguintes_{username}_ideologia_grafico_pizza.png', transparent=True)
    else:
        plt.savefig(
            f'./followersGraphicsPie/seguidores_{username}_ideologia_grafico_pizza.png', transparent=True)


def graphic_follow_number_bar(json_file):

    user_list = []

    for item in json_file:

        data = {
            'username': item['username'],
            'following_len': len(item['following']),
            'followers_len': len(item['followers'])
        }

        user_list.append(data)

    top_10_following = sorted(
        user_list, key=lambda x: x['following_len'], reverse=True)[:10]
    top_10_followers = sorted(
        user_list, key=lambda x: x['followers_len'], reverse=True)[:10]

    bottom_10_following = sorted(
        user_list, key=lambda x: x['following_len'])[:10]
    bottom_10_followers = sorted(
        user_list, key=lambda x: x['followers_len'])[:10]

    top_usernames_following = [user['username'] for user in top_10_following]
    top_following_counts = [user['following_len'] for user in top_10_following]

    top_usernames_followers = [user['username'] for user in top_10_followers]
    top_followers_counts = [user['followers_len']
                            for user in top_10_followers]

    bottom_usernames_following = [user['username']
                                  for user in bottom_10_following]
    bottom_following_counts = [user['following_len']
                               for user in bottom_10_following]
    bottom_usernames_followers = [user['username']
                                  for user in bottom_10_followers]
    bottom_followers_counts = [user['followers_len']
                               for user in bottom_10_followers]

    plt.figure(figsize=(12, 6))
    plt.bar(top_usernames_following, top_following_counts,
            color='#FFDDBB', edgecolor='black', linewidth=1)
    plt.xlabel('Usuário')
    plt.ylabel('Quantidade de Seguintes')
    plt.title('Top 10 Usuários Políticos com Maior Quantidade de Seguintes')
    plt.xticks(rotation=45, ha='right')

    for i, count in enumerate(top_following_counts):
        plt.text(i, count + 0.5, str(count), ha='center', va='bottom')

    plt.tight_layout()
    plt.savefig('./followNumberGraphicsBar/top_10_seguintes.png',
                transparent=True)

    plt.figure(figsize=(12, 6))
    plt.bar(top_usernames_followers, top_followers_counts,
            color='#FFDDBB', edgecolor='black', linewidth=1)
    plt.xlabel('Usuário')
    plt.ylabel('Quantidade de Seguidores')
    plt.title('Top 10 Usuários Políticos com Maior Quantidade de Seguidores')
    plt.xticks(rotation=45, ha='right')

    for i, count in enumerate(top_followers_counts):
        plt.text(i, count + 0.5, str(count), ha='center', va='bottom')

    plt.tight_layout()
    plt.savefig('./followNumberGraphicsBar/top_10_seguidores.png',
                transparent=True)

    plt.figure(figsize=(12, 6))
    plt.bar(bottom_usernames_following, bottom_following_counts,
            color='#FFDDBB', edgecolor='black', linewidth=1)
    plt.xlabel('Usuário')
    plt.ylabel('Quantidade de Seguintes')
    plt.title('Top 10 Usuários Políticos com Menor Quantidade de Seguintes')
    plt.xticks(rotation=45, ha='right')

    for i, count in enumerate(bottom_following_counts):
        plt.text(i, count + 0.5, str(count), ha='center', va='bottom')

    plt.tight_layout()
    plt.savefig('./followNumberGraphicsBar/bottom_10_seguintes.png',
                transparent=True)

    plt.figure(figsize=(12, 6))
    plt.bar(bottom_usernames_followers, bottom_followers_counts,
            color='#FFDDBB', edgecolor='black', linewidth=1)
    plt.xlabel('Usuário')
    plt.ylabel('Quantidade de Seguidores')
    plt.title('Top 10 Usuários Políticos com Menor Quantidade de Seguidores')
    plt.xticks(rotation=45, ha='right')

    for i, count in enumerate(bottom_followers_counts):
        plt.text(i, count + 0.5, str(count), ha='center', va='bottom')

    plt.tight_layout()
    plt.savefig(
        './followNumberGraphicsBar/bottom_10_seguidores.png', transparent=True)


def graphic_info_pie(value1, value2, label1, label2, name_file):
    labels = [label1, label2]
    sizes = [value1, value2]
    colors = ['#ff9999', '#99ff99']
    explode = (0.1, 0)

    plt.figure(figsize=(8, 6))

    def func(pct, allvalues):
        absolute = int(np.round(pct/100.*np.sum(allvalues)))
        return "{:.1f}%\n({:d})".format(pct, absolute)

    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
            autopct=lambda pct: func(pct, sizes), shadow=True, startangle=140,
            pctdistance=0.85, wedgeprops={'edgecolor': 'black'})

    plt.axis('equal')

    plt.savefig(f'./infoGraphicsPie/{name_file}.png', transparent=True)


if __name__ == "__main__":

    with open('dataset.json', 'r') as file_user:

        json_file = json.load(file_user)

        graphic_follow_position_pie(json_file, 'LulaOficial',
                                    1, title='LulaOficial')
        graphic_follow_position_pie(
            json_file, 'jairbolsonaro', 1, title='jairbolsonaro')

        graphic_follow_position_pie(json_file, 'cirogomes',
                                    1, title='cirogomes')

        graphic_follow_position_pie(json_file, 'cirogomes',
                                    1, title='cirogomes')

        graphic_follow_position_pie(json_file, 'LulaOficial',
                                    2, title='LulaOficial')

        graphic_follow_position_pie(
            json_file, 'jairbolsonaro', 2, title='jairbolsonaro')

        graphic_follow_position_pie(json_file, 'cirogomes',
                                    2, title='cirogomes')

        graphic_follow_number_bar(json_file)

        graphic_info_pie(68, 353, 'Inválidos', 'Válidos',
                         'usuarios_invalidos_validos')

        graphic_info_pie(13, 340, 'Outliers', 'Válidos',
                         'usuarios_outliers_validos')

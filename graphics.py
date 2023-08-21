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


def return_posittion_username(json_file, username):
    for item in json_file:
        if item['username'] == username:
            return item['position']


def count_position_follow(json_file):

    user_list = []

    for item in json_file:
        following_direita = 0
        following_esquerda = 0
        following_centro = 0
        followers_direita = 0
        followers_esquerda = 0
        followers_centro = 0

        for user in item['following']:
            user_position = return_posittion_username(json_file, user)
            if user_position == 'esquerda':
                following_esquerda += 1
            elif user_position == 'centro':
                following_centro += 1
            else:
                following_direita += 1

        for user in item['followers']:
            user_position = return_posittion_username(json_file, user)
            if user_position == 'esquerda':
                followers_esquerda += 1
            elif user_position == 'centro':
                followers_centro += 1
            else:
                followers_direita += 1

        result_json = {
            'username': item['username'],
            'following_direita': following_direita,
            'following_esquerda': following_esquerda,
            'following_centro': following_centro,
            'followers_direita': followers_direita,
            'followers_esquerda': followers_esquerda,
            'followers_centro': followers_centro
        }

        user_list.append(result_json)

    top_10_following_esquerda = sorted(
        user_list, key=lambda x: x['following_esquerda'], reverse=True)[:10]

    top_usernames_following_esquerda = [
        user['username'] for user in top_10_following_esquerda]
    top_following_counts_esquerda = [user['following_esquerda']
                                     for user in top_10_following_esquerda]

    plt.figure(figsize=(12, 6))
    plt.bar(top_usernames_following_esquerda, top_following_counts_esquerda,
            color='#ff9999', edgecolor='black', linewidth=1)
    plt.xlabel('Usuário')
    plt.ylabel('Quantidade de Seguintes')
    plt.title(
        'Top 10 Usuários Políticos com Maior Quantidade de Seguintes de Esquerda')
    plt.xticks(rotation=45, ha='right')

    for i, count in enumerate(top_following_counts_esquerda):
        plt.text(i, count + 0.5, str(count), ha='center', va='bottom')

    plt.tight_layout()
    plt.savefig('./followingPositionGraphicsBar/top_10_seguintes_esquerda.png',
                transparent=True)

    top_10_following_direita = sorted(
        user_list, key=lambda x: x['following_direita'], reverse=True)[:10]

    top_usernames_following_direita = [
        user['username'] for user in top_10_following_direita]
    top_following_counts_direita = [user['following_direita']
                                    for user in top_10_following_direita]

    plt.figure(figsize=(12, 6))
    plt.bar(top_usernames_following_direita, top_following_counts_direita,
            color='#99ff99', edgecolor='black', linewidth=1)
    plt.xlabel('Usuário')
    plt.ylabel('Quantidade de Seguintes')
    plt.title(
        'Top 10 Usuários Políticos com Maior Quantidade de Seguintes de Direita')
    plt.xticks(rotation=45, ha='right')

    for i, count in enumerate(top_following_counts_direita):
        plt.text(i, count + 0.5, str(count), ha='center', va='bottom')

    plt.tight_layout()
    plt.savefig('./followingPositionGraphicsBar/top_10_seguintes_direita.png',
                transparent=True)

    top_10_following_centro = sorted(
        user_list, key=lambda x: x['following_centro'], reverse=True)[:10]

    top_usernames_following_centro = [
        user['username'] for user in top_10_following_centro]
    top_following_counts_centro = [user['following_centro']
                                   for user in top_10_following_centro]

    plt.figure(figsize=(12, 6))
    plt.bar(top_usernames_following_centro, top_following_counts_centro,
            color='#66b3ff', edgecolor='black', linewidth=1)
    plt.xlabel('Usuário')
    plt.ylabel('Quantidade de Seguintes')
    plt.title(
        'Top 10 Usuários Políticos com Maior Quantidade de Seguintes de Centro')
    plt.xticks(rotation=45, ha='right')

    for i, count in enumerate(top_following_counts_centro):
        plt.text(i, count + 0.5, str(count), ha='center', va='bottom')

    plt.tight_layout()
    plt.savefig('./followingPositionGraphicsBar/top_10_seguintes_centro.png',
                transparent=True)

    top_10_followers_esquerda = sorted(
        user_list, key=lambda x: x['followers_esquerda'], reverse=True)[:10]

    top_usernames_followers_esquerda = [
        user['username'] for user in top_10_followers_esquerda]
    top_followers_counts_esquerda = [user['followers_esquerda']
                                     for user in top_10_followers_esquerda]

    plt.figure(figsize=(12, 6))
    plt.bar(top_usernames_followers_esquerda, top_followers_counts_esquerda,
            color='#ff9999', edgecolor='black', linewidth=1)
    plt.xlabel('Usuário')
    plt.ylabel('Quantidade de Seguidores')
    plt.title(
        'Top 10 Usuários Políticos com Maior Quantidade de Seguidores de Esquerda')
    plt.xticks(rotation=45, ha='right')

    for i, count in enumerate(top_followers_counts_esquerda):
        plt.text(i, count + 0.5, str(count), ha='center', va='bottom')

    plt.tight_layout()
    plt.savefig('./followersPositionGraphicsBar/top_10_seguidores_esquerda.png',
                transparent=True)

    top_10_followers_centro = sorted(
        user_list, key=lambda x: x['followers_centro'], reverse=True)[:10]

    top_usernames_followers_centro = [
        user['username'] for user in top_10_followers_centro]
    top_followers_counts_centro = [user['followers_centro']
                                   for user in top_10_followers_centro]

    plt.figure(figsize=(12, 6))
    plt.bar(top_usernames_followers_centro, top_followers_counts_centro,
            color='#66b3ff', edgecolor='black', linewidth=1)
    plt.xlabel('Usuário')
    plt.ylabel('Quantidade de Seguidores')
    plt.title(
        'Top 10 Usuários Políticos com Maior Quantidade de Seguidores de Centro')
    plt.xticks(rotation=45, ha='right')

    for i, count in enumerate(top_followers_counts_centro):
        plt.text(i, count + 0.5, str(count), ha='center', va='bottom')

    plt.tight_layout()
    plt.savefig('./followersPositionGraphicsBar/top_10_seguidores_centro.png',
                transparent=True)

    top_10_followers_direita = sorted(
        user_list, key=lambda x: x['followers_direita'], reverse=True)[:10]

    top_usernames_followers_direita = [
        user['username'] for user in top_10_followers_direita]
    top_followers_counts_direita = [user['followers_direita']
                                    for user in top_10_followers_direita]

    plt.figure(figsize=(12, 6))
    plt.bar(top_usernames_followers_direita, top_followers_counts_direita,
            color='#99ff99', edgecolor='black', linewidth=1)
    plt.xlabel('Usuário')
    plt.ylabel('Quantidade de Seguidores')
    plt.title(
        'Top 10 Usuários Políticos com Maior Quantidade de Seguidores de Direita')
    plt.xticks(rotation=45, ha='right')

    for i, count in enumerate(top_followers_counts_direita):
        plt.text(i, count + 0.5, str(count), ha='center', va='bottom')

    plt.tight_layout()
    plt.savefig('./followersPositionGraphicsBar/top_10_seguidores_direita.png',
                transparent=True)


def count_position_username(json_file):

    direita = 0
    esquerda = 0
    centro = 0

    for item in json_file:

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

    plt.title('Ideologia dentre os 340 usuários', fontsize=16)
    plt.axis('equal')

    plt.tight_layout()
    plt.savefig('./infoGraphicsPie/usuarios_ideologia_total.png',
                transparent=True)


if __name__ == "__main__":

    with open('dataset.json', 'r') as file_user:

        json_file = json.load(file_user)

        # graphic_follow_position_pie(json_file, 'LulaOficial',
        #                             1, title='LulaOficial')
        # graphic_follow_position_pie(
        #     json_file, 'jairbolsonaro', 1, title='jairbolsonaro')

        # graphic_follow_position_pie(json_file, 'cirogomes',
        #                             1, title='cirogomes')

        # graphic_follow_position_pie(json_file, 'cirogomes',
        #                             1, title='cirogomes')

        # graphic_follow_position_pie(json_file, 'LulaOficial',
        #                             2, title='LulaOficial')

        # graphic_follow_position_pie(
        #     json_file, 'jairbolsonaro', 2, title='jairbolsonaro')

        # graphic_follow_position_pie(json_file, 'cirogomes',
        #                             2, title='cirogomes')

        # graphic_follow_number_bar(json_file)

        # graphic_info_pie(68, 353, 'Inválidos', 'Válidos',
        #                  'usuarios_invalidos_validos')

        # graphic_info_pie(13, 340, 'Outliers', 'Válidos',
        #                  'usuarios_outliers_validos')

        # count_position_follow(json_file)

        count_position_username(json_file)

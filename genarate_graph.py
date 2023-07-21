import json


def generate_large_graph():
    with open('dataset.json', 'r') as file_user:

        json_user = json.load(file_user)

        graphnode = []
        graphlink = []

        for item in json_user:

            node = {
                'id': item['username'],
                'name': item['username'],
                'label': item['position'],
                'color': 'blue' if item['position'] == 'direita' else ('white' if item['position'] == 'centro' else 'red')
            }

            graphnode.append(node)

            for following in item['following']:

                link = {
                    'source': item['username'],
                    'target': following,
                    'label': item['position'],
                    'color': 'white'
                }

                graphlink.append(link)

        final_json = {
            'nodes': graphnode,
            'links': graphlink
        }

        with open(f'graph.json', "w") as arquivo:
            json.dump(final_json, arquivo, indent=4)


def generate_selected_users_graph(username_list, json_name):
    with open('dataset.json', 'r') as file_user:

        json_user = json.load(file_user)

        graphnode = []
        graphlink = []
        username_list_added = []

        for item in json_user:

            if item['username'] in username_list:
                node = {
                    'id': item['username'],
                    'name': item['username'],
                    'label': item['position'],
                    'color': item['color']
                }

                graphnode.append(node)

        for item in json_user:
            for following in item['following']:

                if following in username_list:
                    node = {
                        'id': item['username'],
                        'name': item['username'],
                        'label': item['position'],
                        'color': item['color']
                    }

                    if item['username'] not in username_list_added:
                        graphnode.append(node)
                        username_list_added.append(item['username'])

                    link = {
                        'source': item['username'],
                        'target': following,
                        'label': item['position'],
                        'color': item['color']
                    }

                    graphlink.append(link)

        final_json = {
            'nodes': graphnode,
            'links': graphlink
        }

        with open(f'{json_name}.json', "w") as arquivo:
            json.dump(final_json, arquivo, indent=4)


if __name__ == "__main__":
    generate_large_graph()
    generate_selected_users_graph(
        ['LulaOficial', 'jairbolsonaro'], 'lula_bolsonaro')
    generate_selected_users_graph(
        ['LulaOficial', 'jairbolsonaro', 'cirogomes'], 'lula_bolsonaro_ciro')
    generate_selected_users_graph(
        ['jairbolsonaro', 'cirogomes'], 'bolsonaro_ciro')
    generate_selected_users_graph(
        ['LulaOficial', 'cirogomes'], 'lula_ciro')

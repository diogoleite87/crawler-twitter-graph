import json


def read_txt_file(file_path):
    data_list = []

    with open(file_path, 'r') as file:
        for line in file:
            if not line.startswith("#"):
                from_node, to_node = map(int, line.strip().split('\t'))
                data_list.append([from_node, to_node])

    return data_list


if __name__ == "__main__":

    file_path = "p2p-Gnutella08.txt"

    result_list = read_txt_file(file_path)

    graphnode = []
    graphlink = []

    for i in range(6301):
        node = {
            'id': str(i),
            'name': str(i),
            'label': "peer",
            'color': 'red'
        }

        graphnode.append(node)

    for item in result_list:
        link = {
            'source': str(item[0]),
            'target': str(item[1]),
            'label': 'to',
            'color': 'white'
        }

        graphlink.append(link)

    final_json = {
        'nodes': graphnode,
        'links': graphlink
    }

    with open(f'p2p_gnutella_08.json', "w") as arquivo:
        json.dump(final_json, arquivo, indent=4)

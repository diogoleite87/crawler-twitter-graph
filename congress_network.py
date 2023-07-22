import json


if __name__ == "__main__":

    graphnode = []
    graphlink = []

    with open('congress_network_data.json', 'r') as file:

        json_loaded = json.load(file)

        for i in range(475):

            node = {
                "id": str(i),
                "label": "person",
                "name": json_loaded[0]["usernameList"][i],
                "color": "blue"
            }

            graphnode.append(node)

        for i in range(475):

            print(json_loaded[0]["inList"][i])

            for inList in json_loaded[0]["inList"][i]:
                link = {
                    'source': str(inList),
                    'target': str(i),
                    'label': 'network',
                    'color': 'white'
                }

                graphlink.append(link)

        for i in range(475):
            print(json_loaded[0]["outList"][i])

            for outList in json_loaded[0]["outList"][i]:
                link = {
                    'source': str(i),
                    'target': str(outList),
                    'label': 'network',
                    'color': 'white'
                }

                graphlink.append(link)

    final_json = {
        'nodes': graphnode,
        'links': graphlink
    }

    with open(f'twitter_network_congress_us.json', "w") as arquivo:
        json.dump(final_json, arquivo, indent=4)

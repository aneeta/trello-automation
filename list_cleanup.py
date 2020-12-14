import datetime
import requests

def list_cleanup(key, token, board):

    TODAY = datetime.date.today()
    TOMORROW = TODAY + datetime.timedelta(days=1, hours=23, minutes=59)
    NW = TOMORROW + datetime.timedelta(days=7)

    # get list ids
    base_query = {
    'key': key,
    'token': token
    }
    response = requests.get(
        "https://api.trello.com/1/boards/{}/lists".format(board),
        params=base_query
    )

    lists = response.json()
    list_id = {}
    for item in lists:
        list_id[item['name']] = item['id']

    # move all cards from 'tomorrow' to 'today'
    query = {
        'key': key,
        'token': token,
        'idBoard': lists[0]['idBoard'],
        'idList': list_id['Today']
    }

    response = requests.post(
        "https://api.trello.com/1/lists/{}/moveAllCards".format(list_id['Tomorrow']),
        params=query
    )

    # modules
    response = requests.get(
        "https://api.trello.com/1/lists/{}/cards".format(list_id["Classes"]),
        params=base_query
    )
    modules = response.json()

    for i in modules:
        response = requests.get(
        "https://api.trello.com/1/lists/{}/cards".format(list_id[i["name"]]),
        params=base_query
        )

        for j in response.json():
            if j['due']:
                due = datetime.date.fromisoformat(j['due'][:10])
                # move cards with due date before today to 'backlog'
                if j['dueComplete'] == False and due < TODAY:
                    r = requests.put(
                        "https://api.trello.com/1/cards/{}".format(j['id']),
                        data={
                            'key': key,
                            'token': token,
                            'idList': list_id['Backlog']
                        }
                    )
                # move cards with due date today or tomorrow to 'today'
                if j['dueComplete'] == False and (TODAY < due and due <= TOMORROW):
                    r = requests.put(
                        "https://api.trello.com/1/cards/{}".format(j['id']),
                        data={
                            'key': key,
                            'token': token,
                            'idList': list_id['Today']
                        }
                    )

                # move cards with due date +2 - +8 days to 'this week'
                if j['dueComplete'] == False and (TOMORROW < due and due <= NW):
                    r = requests.put(
                        "https://api.trello.com/1/cards/{}".format(j['id']),
                        data={
                            'key': key,
                            'token': token,
                            'idList': list_id['This Week']
                        }
                    )


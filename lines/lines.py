def headers(data):
    headers = ""
    if data["data"]["linkedLists"]:
        linkedLists = data["data"]["linkedLists"]
        for lists in linkedLists:
            headers += lists["name"]+";"

    normalLists = data["data"]["normalLists"]
    for lists in normalLists:
        if normalLists.index(lists) == len(normalLists)-1:
            headers += lists["name"]
        else:
            headers += lists["name"]+";"
    return headers
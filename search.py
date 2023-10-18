import pymongo
from connect import client

db = client.get_database()
quotes_collection = db["quote"]
authors_collection = db["author"]


def search_quotes(query):
    if "name" in query:
        quotes = quotes_collection.find({"author": query["name"]})
    elif "tag" in query:
        quotes = quotes_collection.find({"tags": query["tag"]})
    elif "tags" in query:
        tags = query["tags"].split(",")
        quotes = quotes_collection.find({"tags": {"$in": tags}})
    else:
        return None
    return quotes


if __name__ == '__main__':

    while True:
        user_input = input(
            "Введите команду (например, name:Steve Martin, tag:life, tags:life,live, или exit для завершения): ").strip()

        if user_input.lower() == "exit":
            break

        parts = user_input.split(":")
        if len(parts) != 2:
            print("Incorrect command")
            continue

        command, value = parts[0], parts[1]
        query = {command: value}

        quotes = search_quotes(query)

        if quotes:
            for quote in quotes:
                print(quote['quote'])
        else:
            print("Нет результатов для данного запроса.")

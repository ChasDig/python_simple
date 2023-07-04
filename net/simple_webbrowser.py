import sys
import requests
import webbrowser


def search(title: str):
    search_url = "https://archive.org/advancedsearch.php"
    params = {
        "q": "title:({}) And mediatype:(movies)".format(title),
        "f1": "identifier,title,description",
        "output": "json",
        "rows": 10,
        "page": 1,
    }
    resp = requests.get(url=search_url, params=params)
    data = resp.json()
    docs = [(doc["identifier"], doc["title"], doc["description"]) for doc in data["response"]["docs"]]
    return docs


def choose(docs):
    last = len(docs) - 1
    for num, doc in enumerate(docs):
        print(f"{num}: {doc[1]} {doc[2][:30]}")
    input_index = input(f"Input your index ( 0 - {last}): ")
    try:
        return docs[int(input_index)][0]
    except:
        return None


def display(identifier_url):
    detail_url = f"https://archive.org/details/{identifier_url}"
    print(f"Loading: {detail_url}")
    webbrowser.open(detail_url)


def main(title):
    page = search(title)
    if page:
        page_index = choose(page)
        print(page_index)
        if page_index:
            display(page_index)
        else:
            print("Nothing selected.")
    else:
        print(f"Nothing found for {title}")


if __name__ == "__main__":
    main(sys.argv[1])

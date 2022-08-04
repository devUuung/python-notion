import requests


class Database:
    def __init__(self, url, api) -> None:
        headers = {
            "Accept": "application/json",
            "Notion-Version": "2022-06-28",
            "Authorization": f"Bearer {api}"
        }
        res = requests.get(
            "https://api.notion.com/v1/databases/" +
            url.split("/")[-1].split("?")[0],
            headers=headers).json()

        self.id = res["id"]
        self.title = res["title"]
        self.properties = res["properties"]
        self.api = api

    # 정상작동

    def insert(self, attributes, contents):
        url = "https://api.notion.com/v1/pages"
        properties = {}

        properties[attributes[0]] = {
            "title": [{"text": {"content": contents[0]}}]
        }

        for i in range(1, len(attributes)):
            properties[attributes[i]] = {"rich_text": [
                {"text": {"content": contents[i]}}]}

        payload = {
            "parent": {
                "type": "database_id",
                "database_id": f"{self.id}"
            },
            "properties": properties
        }
        headers = {
            "Accept": "application/json",
            "Notion-Version": "2022-06-28",
            "Content-Type": "application/json",
            "Authorization": f"{self.api}"
        }
        res = requests.post(url, json=payload, headers=headers)
        return res.json()

    # 정상작동

    def read(self):
        url = f"https://api.notion.com/v1/databases/{self.id}/query"
        payload = {"page_size": 100}
        headers = {
            "Accept": "application/json",
            "Notion-Version": "2021-08-16",
            "Content-Type": "application/json",
            "Authorization": f"{self.api}"
        }
        res = requests.post(url, json=payload, headers=headers).json()
        return res

    # 정상작동

    def update(self, primary, before_content, after_content):
        response = self.read()
        for result in response["results"]:
            if result["properties"][f"{primary}"]["title"][0]["plain_text"] == before_content:
                page_id = result["url"].split("/")[-1].split("-")[-1]
                url = f"https://api.notion.com/v1/pages/{page_id}"
                properties = {}
                properties[primary] = {
                    "title": [{"text": {"content": after_content}}]}
                payload = {
                    "parent": {
                        "type": "database_id",
                        "database_id": f"{self.id}"
                    },
                    "properties": properties
                }
                headers = {
                    "Accept": "application/json",
                    "Notion-Version": "2022-06-28",
                    "Content-Type": "application/json",
                    "Authorization": f"{self.api}"
                }
                res = requests.patch(
                    url, json=payload, headers=headers).json()
        return True if res else False

    # 정상작동
    # TODO primary뿐만 아니라 다른 속성으로도 삭제할 수 있게 만들기

    def delete(self, primary, content):
        response = self.read()
        # primary를 통해 삭제할 요소를 찾음
        for result in response["results"]:
            if result["properties"][f"{primary}"]["title"][0]["plain_text"] == content:
                page_id = result["url"].split("/")[-1].split("-")[-1]
                url = f"https://api.notion.com/v1/pages/{page_id}"
                payload = {"archived": True}
                headers = {
                    "Accept": "application/json",
                    "Notion-Version": "2022-06-28",
                    "Content-Type": "application/json",
                    "Authorization": f"{self.api}"
                }
                res = requests.patch(
                    url, json=payload, headers=headers).json()
        return True if res else False

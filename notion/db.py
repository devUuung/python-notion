import requests


class Page:
    def __init__(self, json, attrs: dict) -> None:
        self.id = json["id"]
        self.attr = {}
        for key, property in json["properties"].items():
            if property["type"] == "rich_text":
                self.attr[key] = {
                    "value": property["rich_text"][0]["plain_text"] if property["rich_text"] else None,
                    "type": attrs[key].type,
                    "primary": attrs[key].primary,
                    "notNone": attrs[key].notNone,
                    "title": False,
                    "rich_text": True
                }
            elif property["type"] == "title":
                self.attr[key] = {
                    "value": property["title"][0]["plain_text"] if property["title"] else None,
                    "type": attrs[key].type,
                    "primary": attrs[key].primary,
                    "notNone": attrs[key].notNone,
                    "title": True,
                    "rich_text": False
                }


class Attribute:
    """
        Attribute 클래스로 만들어진 인스턴스의 네이밍은 key의 이름이어야합니다.
    """

    def __init__(self, type, **kwargs) -> None:
        """
        type 종류
        1. str, string
        2. int, integer
        3. float
        """
        self.type = type
        try:
            if kwargs["primary"] == True:
                self.primary = True
                self.notNone = True
            else:
                self.primary = False
                self.notNone = False
        except KeyError:
            self.primary = False
            self.notNone = False
        try:
            if kwargs["notNone"] and kwargs["notNone"] == True:
                self.notNone = True
        except KeyError:
            ...


class Database:
    def __init__(self, url, api, attrs: dict) -> None:
        """
        url: 데이터베이스가 존재하는 http 주소입니다.
        api: notionAPI key 입니다.
        attrs: Attribute 클래스 인스턴스들의 딕셔너리 묶음입니다.
        """
        headers = {
            "Accept": "application/json",
            "Notion-Version": "2022-06-28",
            "Authorization": f"Bearer {api}"
        }
        res = requests.get(
            "https://api.notion.com/v1/databases/" +
            url.split("/")[-1].split("?")[0],
            headers=headers
        ).json()

        self.id = res["id"]
        self.title = res["title"]
        self.properties = res["properties"]
        self.api = api
        self.attrs = attrs

    # insert할때 타입이 일치하는지 확인하는 기능 추가해야함.
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

    def read(self) -> tuple[Page]:
        """
        Page 클래스 튜플을 반환합니다.
        1. id
        2. attr
        """
        url = f"https://api.notion.com/v1/databases/{self.id}/query"
        payload = {"page_size": 100}
        headers = {
            "Accept": "application/json",
            "Notion-Version": "2021-08-16",
            "Content-Type": "application/json",
            "Authorization": f"{self.api}"
        }
        res = requests.post(url, json=payload, headers=headers).json()
        arr = []
        for result in res["results"]:
            arr.append(Page(result, self.attrs))
        return tuple(arr)

    def update(self, key, before_content, after_content) -> bool:
        for result in self.read():
            if result.attr[key]["value"] == before_content:
                url = f"https://api.notion.com/v1/pages/{result.id}"
                properties = {}
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
                if result.attr[key]["title"]:
                    properties[key] = {
                        "title": [{"text": {"content": after_content}}]}
                elif result.attr[key]["rich_text"]:
                    properties[key] = {
                        "rich_text": [{"text": {"content": after_content}}]}
                res = requests.patch(url, json=payload, headers=headers).json()
        return True if res else False

    def delete(self, key, content) -> bool:
        """
        key의 값이 content인 요소를 삭제합니다.
        """
        for result in self.read():
            if result.attr[key]["value"] == content:
                url = f"https://api.notion.com/v1/pages/{result.id}"
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

import requests
from .page import Page


class Database:
    def __init__(self, url, api, attr) -> None:
        """
        url: 데이터베이스가 존재하는 http 주소입니다.
        api: notionAPI key 입니다.
        attr: Attribute 클래스 인스턴스들의 딕셔너리 묶음입니다.
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
        self.attr = attr

    def insert(self, attributes, contents):
        url = "https://api.notion.com/v1/pages"
        properties = {}
        is_primary = False
        for i, attribute in enumerate(attributes):
            if self.attr[attribute].primary:
                if is_primary:
                    return False
                is_primary = True
                if self.attr[attribute].type.is_valid(contents[i]):
                    properties[attribute] = {
                        "title": [{
                            "text": {
                                "content": str(contents[i])
                            }
                        }]
                    }
                else:
                    return False
            else:
                if self.attr[attribute].type.is_valid(contents[i]) is True:
                    properties[attribute] = {
                        "rich_text": [{
                            "text": {
                                "content": str(contents[i])
                            }
                        }]
                    }
                else:
                    return False

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
            arr.append(Page(result, self.attr))
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

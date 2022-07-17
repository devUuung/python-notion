from .client import Client
import requests


class Database(Client):
    def __init__(self, api_key: str, database_key: str) -> None:
        super().__init__(api_key)
        self.database_key = database_key

    def get_elements_text(self, attribute: str) -> list:
        url = f"https://api.notion.com/v1/databases/{self.database_key}/query"

        payload = {"page_size": 100}
        headers = {
            "Accept": "application/json",
            "Notion-Version": "2021-08-16",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }

        response = requests.post(url, json=payload, headers=headers)
        arr = []
        for result in response.json()["results"]:
            arr.append(result["properties"]
                       [f"{attribute}"]["title"][0]["plain_text"])
        return arr

    def remove_elements_text(self, attribute: str, text: str):
        url = f"https://api.notion.com/v1/databases/{self.database_key}/query"
        payload = {"page_size": 100}
        headers = {
            "Accept": "application/json",
            "Notion-Version": "2021-08-16",
            "Content-Type": "application/json",
            "Authorization": f"{self.api_key}"
        }
        response = requests.post(url, json=payload, headers=headers)

        for result in response.json()["results"]:
            if result["properties"][f"{attribute}"]["title"][0]["plain_text"] == text:
                page_id = result["url"].split("/")[-1].split("-")[-1]
                url = f"https://api.notion.com/v1/pages/{page_id}"
                payload = {"archived": True}
                headers = {
                    "Accept": "application/json",
                    "Notion-Version": "2022-06-28",
                    "Content-Type": "application/json",
                    "Authorization": f"{self.api_key}"
                }
                response = requests.patch(
                    url, json=payload, headers=headers)

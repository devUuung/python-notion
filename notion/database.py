from .client import Client
import requests


class Database(Client):
    def __init__(self, api_key: str, database_key: str) -> None:
        super().__init__(api_key)
        self.database_key = database_key

    def get_database(self):
        url = f"https://api.notion.com/v1/databases/{self.database_key}/query"

        payload = {"page_size": 100}
        headers = {
            "Accept": "application/json",
            "Notion-Version": "2021-08-16",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }

        response = requests.post(url, json=payload, headers=headers)

        return response.text

    def setDatabase(self):
        ...

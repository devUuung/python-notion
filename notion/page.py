from .client import Client
import requests


class Page(Client):
    def __init__(self, api_key: str, page_id: str) -> None:
        super().__init__(api_key)
        self.page_id = page_id

    def get_page(self) -> dict:
        url = f"https://api.notion.com/v1/pages/{self.page_id}"
        headers = {
            "Accept": "application/json",
            "Notion-Version": "2022-06-28",
            "Authorization": f"Bearer {self.api_key}"
        }
        response = requests.get(url, headers=headers)
        return response.json()

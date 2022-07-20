from .client import Client
import requests


class Block(Client):
    def __init__(self, api_key: str, block_id: str) -> None:
        super().__init__(api_key)
        self.block_id = block_id

    def get_block(self) -> dict:
        url = f"https://api.notion.com/v1/blocks/{self.block_id}"

        headers = {
            "Accept": "application/json",
            "Notion-Version": "2022-06-28",
            "Authorization": f"Bearer {self.api_key}"
        }

        response = requests.get(url, headers=headers)

        return response.json()

    def get_children_blocks(self) -> list:
        url = f"https://api.notion.com/v1/blocks/{self.block_id}/children?page_size=100"

        headers = {
            "Accept": "application/json",
            "Notion-Version": "2022-06-28",
            "Authorization": f"Bearer {self.api_key}"
        }

        response = requests.get(url, headers=headers)
        arr = []
        for result in response.json()["results"]:
            arr.append(result)
        return arr

    def get_children_blocks_text(self) -> list:
        url = f"https://api.notion.com/v1/blocks/{self.block_id}/children?page_size=100"

        headers = {
            "Accept": "application/json",
            "Notion-Version": "2022-06-28",
            "Authorization": f"Bearer {self.api_key}"
        }
        arr = []
        response = requests.get(url, headers=headers)
        for result in response.json()["results"]:
            arr.append(result["paragraph"]["rich_text"][0]["text"]
                       ["content"] if result["paragraph"]["rich_text"] else None)
        return arr

from .client import Client
import requests


class Block(Client):
    def __init__(self, api_key: str, block_id: str) -> None:
        super().__init__(api_key)
        self.block_id = block_id

    def get_block(self):
        url = f"https://api.notion.com/v1/blocks/{self.block_id}"

        headers = {
            "Accept": "application/json",
            "Notion-Version": "2022-06-28",
            "Authorization": f"Bearer {self.api_key}"
        }

        response = requests.get(url, headers=headers)

        return response.json()

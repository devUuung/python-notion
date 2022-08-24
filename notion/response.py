import requests
from notion.property import Property

class Response:
  def __init__(self, url, json, headers) -> None:
    self.results = requests.post(
      url,
      json=json,
      headers=headers
      ).json()["results"]

  def getResult(self):
    for result in self.results:
      yield result

  def getID(self, result):
    return result["id"]

  def getProperty(self, result) -> dict:
    dictionary = {}
    for key, value in result["properties"].items():
      dictionary[key] = (Property(key, value)())
    return dictionary

  def getProperties(self) -> tuple:
    arr = []
    for result in self.getResult():
      arr.append({
        "id": self.getID(result),
        "property": self.getProperty(result)
      })
    return tuple(arr)

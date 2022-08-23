import requests

class Property:
  def __init__(self, key, value) -> None:
    self.key = key
    self.type = value["type"]
    self.id = id
    match value["type"]:
      case "title":
        self.value = value["title"][0]["plain_text"]
      case "rich_text":
        self.value = value["rich_text"][0]["plain_text"]
      case _:
        raise Exception("Property 에러")

  def __call__(self) -> dict:
    return {
      "content": self.value,
      "type": self.type
    }

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

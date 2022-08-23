import requests

class Property:
  def __init__(self, key, value, id) -> None:
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

  def __call__(self) -> tuple:
    return (
      self.id,
      {
        self.key: self.value,
        "type": self.type
      }
    )

class Response:
  def __init__(self, url, json, headers) -> None:
    self.results = requests.post(
      url,
      json=json,
      headers=headers
      ).json()["results"]

  def getProperty(self):
    for result in self.results:
      yield [Property(key, value, result["id"])() for key, value in result["properties"].items()]

  def getProperties(self) -> tuple:
    return tuple([
        property for property in self.getProperty()
      ])

import requests

class Property:
  def __init__(self, key, value) -> None:
    self.key = key
    match value["type"]:
      case "title":
        self.value = value["title"][0]["plain_text"]
      case "rich_text":
        self.value = value["rich_text"][0]["plain_text"]
      case _:
        raise Exception("Property 에러")

  def __call__(self) -> tuple:
    return (self.key, self.value)

class Title:
  def __init__(self) -> None:
    pass

class RichText:
  def __init__(self) -> None:
    pass

class Response:
  def __init__(self, url, json, headers) -> None:
    self.results: array = requests.post(
      url,
      json=json,
      headers=headers
      ).json()["results"]

  def getProperty(self):
    for result in self.results:
      for key, value in result["properties"].items():
        yield Property(key, value)()

  def getProperties(self) -> tuple:
    return tuple([
        property for property in self.getProperty()
      ])

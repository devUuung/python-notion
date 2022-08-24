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
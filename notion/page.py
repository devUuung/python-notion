class Page:
    def __init__(self, json, attr: dict) -> None:
        self.id = json["id"]
        self.attr = {}
        for key, property in json["properties"].items():
            if property["type"] == "rich_text":
                self.attr[key] = {
                    "value": property["rich_text"][0]["plain_text"] if property["rich_text"] else None,
                    "type": attr[key].type,
                    "primary": attr[key].primary,
                    "null": attr[key].null,
                    "title": False,
                    "rich_text": True
                }
            elif property["type"] == "title":
                self.attr[key] = {
                    "value": property["title"][0]["plain_text"] if property["title"] else None,
                    "type": attr[key].type,
                    "primary": attr[key].primary,
                    "null": attr[key].null,
                    "title": True,
                    "rich_text": False
                }

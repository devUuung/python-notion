class Type:
    def __init__(self, type) -> None:
        self.type = type

    def __call__(self):
        return self.type

    def is_valid(self, content) -> bool:
        if self.type == "str" or self.type == "string" or self.type == "Str" or self.type == "String":
            return True
        elif self.type == "int" or self.type == "Int" or self.type == "Integer" or self.type == "integer":
            try:
                int(content)
            except ValueError:
                return False
            else:
                return True
        elif self.type == "float" or self.type == "Float":
            try:
                float(content)
            except ValueError:
                return False
            else:
                return True

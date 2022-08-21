class Field:
    def __init__(self, *, pk=False, null=True, foreign=None) -> None:
      self.pk = pk
      self.null = null
      self.type = None
      self.foreign = foreign
    def set_type(self, type):
      self.type = type
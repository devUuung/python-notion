from .field import Field

class FloatField(Field):
    def __init__(self, *, pk=False, null=True) -> None:
      super().__init__(pk=pk, null=null)

    def set_type(self, type):
      return super().set_type(type)
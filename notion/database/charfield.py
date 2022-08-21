from .field import Field

class CharField(Field):
    def __init__(self, *, pk=False, null=True, foreign=None) -> None:
      super().__init__(pk=pk, null=null, foreign=foreign)

    def set_type(self, type):
      return super().set_type(type)
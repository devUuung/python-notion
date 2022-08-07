from .type import Type


class Attribute:
    """
        Attribute 클래스로 만들어진 인스턴스의 네이밍은 key의 이름이어야합니다.
    """

    def __init__(self, type, primary=False, null=True, blank=True) -> None:
        """
        type 종류
        1. str, string
        2. int, integer
        3. float
        """
        self.type = Type(type)

        self.null = False if primary else null
        self.primary = primary
        self.blank = blank

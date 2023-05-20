class Product:
    def __init__(self, id: int, name: str, price: float):
        self.__id = id
        self.__name = name
        self.__price = price

    def get_id(self) -> int:
        return self.__id

    def get_name(self) -> str:
        return self.__name

    def get_price(self) -> float:
        return self.__price

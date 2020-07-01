class MyZeroExcept(Exception):
    def __init__(self, txt):
        self.txt = txt


class MyClass:
    def __init__(self):
        self._my_dividend = None
        self._my_divider = None

    def my_division(self):
        try:
            self._my_dividend = int(input("Введите делимое число: "))
            self._my_divider = int(input("Введите делитель: "))
        except ValueError:
            print("value error")

        try:
            if self._my_divider == 0:
                raise MyZeroExcept("нельзя делить на 0")
            my_result = self._my_dividend / self._my_divider
        except MyZeroExcept as err:
            print(err)
        else:
            print(f"Result = {my_result}")


m = MyClass()
m.my_division()
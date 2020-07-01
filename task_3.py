class MyListExcept(Exception):
    def __init__(self, txt):
        self.txt = txt


class MyClass:
    def __init__(self, my_list):
        self._my_list = my_list
        try:
            for i in self._my_list:
                if not isinstance(i, int):
                    raise MyListExcept("в массие не только числа!")
        except ValueError:
            print("value error")
        except MyListExcept as err:
            print(err)
        else:
            print("Correct list")


m = MyClass([1, 2, 3, 4, "a"])
import datetime


class MyDate:
    my_date_string = None
    my_number = None
    my_month = None
    my_year = None

    @classmethod
    def my_method(cls, my_date_string):
        my_date_string = my_date_string
        my_date_list = map(int, my_date_string.split('-'))

        for index, value in enumerate(my_date_list):
            if index == 0:
                MyDate.my_number = value
            elif index == 1:
                MyDate.my_month = value
            elif index == 2:
                MyDate.my_year = value

    @staticmethod
    def my_validate_method():
        if 1 <= MyDate.my_number <= 31:
            print(f"{MyDate.my_number} - corrected number")
        else:
            print(f"{MyDate.my_number} - uncorrected number")

        if 1 <= MyDate.my_month <= 12:
            print(f"{MyDate.my_month} - corrected month")
        else:
            print(f"{MyDate.my_month} - uncorrected month")

        if MyDate.my_year == datetime.datetime.now().year:
            print(f"{MyDate.my_year} - corrected year")
        else:
            print(f"{MyDate.my_year} - uncorrected year")


MyDate.my_method("3-02-2020")
MyDate.my_validate_method()

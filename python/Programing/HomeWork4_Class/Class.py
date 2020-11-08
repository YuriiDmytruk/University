import Validator
class Department:
    def __init__(self, id=None, title=None, director_name=None, phone_number=None, monthly_budget=None,
                 yearly_budget=None, website_url=None):
        self.id = id
        self.title = title
        self.director_name = director_name
        self.phone_number = phone_number
        self.monthly_budget = monthly_budget
        self.yearly_budget = yearly_budget
        self.website_url = website_url

    def print_elem(self):
        check = 0
        while check < Department.number_of_fields(self):
            print(Department.get_value(self, check), end='; ')
            check += 1

    def get_value(self, key):
        number = 0
        for attribute, value in self.__dict__.items():
            if number == key:
                return value
            else:
                number += 1

    def add_value(self, value, key):
        if value == "":
            value = "None"
        number = 0
        for attribute in self.__dict__.items():
            if number == key:
                name = str(attribute)
                name = get_name(name)
                self.__dict__[name] = value
            else:
                number += 1

    def create_new_elem(self, arr_add):
        validate_list_add(arr_add)
        check = 0
        while check < Department.number_of_fields(self):
            Department.add_value(self, arr_add[check], check)
            check += 1
        return self

    def number_of_fields(self):
        fields = 0
        for attribute, value in self.__dict__.items():
            fields += 1
        return fields

def validate_list_add(arr_add):
    check = 0
    while check < len(arr_add):
        element = Validator.Validate(arr_add[check])
        add_value = Validator.Validate.check_invalid_symbols(element)
        arr_add[check] = add_value
        check += 1
    return arr_add


def get_name(name):
    ret_name = ""
    check = 0
    x = 0
    while check < len(name):
        if name[check] == "'":
            x += 1
            check += 1
        if x == 1:
            ret_name += name[check]
            check += 1
        elif x == 2:
            break
        else:
            check += 1
    return ret_name


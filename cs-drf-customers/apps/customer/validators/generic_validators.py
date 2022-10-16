from ctypes import Array

def validate_min_length(field_name, field_value, min_length):
    """checks if the field has the minimum number of characters

    Args:
        field_name: `str`: field name in serializer
        field_value `str`: field to be validated
        min_length `int`: minimum amount that the field must have
    """
    print('Antes do if')
    if len(field_value) < min_length:
        print('entrou')
        return (
            f"{field_name}: O {field_name} deve ter {min_length} dígitos."
        )


def list_in_one_dict(list: Array) -> dict:
    """takes a list of strings in key:value format and transforms it into a dictionary.

    Args:
        list `Array`: list of strings with (key:value). \n
        eg. ['name: is name', ..., 'value:is value']

    -------
    Returns:
        `dict`: all values in dict
    ----
    eg. { 'name' : 'is name', ..., 'value' : 'is value' }
    """
    dict = {}
    for item in list:
        if item:
            tuple = item.split(': ')
            dict[tuple[0]] = tuple[1]

    return dict

import tkinter as tk
from typing import Iterable
from random import randint
import pyperclip


check_button_type = Iterable[tk.IntVar]


def generate_code(length: int) -> str:
    """
    function to generate code of specific length
    :param length: just code length
    :return: code of specific length as a **string**
    """

    max_number: int = 10 ** length - 1
    code: str = str(randint(0, max_number))
    fill_length: int = length - len(code)

    return code.zfill(fill_length)


def generate_and_put(tk_int_var: check_button_type, result_label: tk.Label) -> None:
    """
    function to generate and put psc codes into label
    :param tk_int_var: iterable of **tk.IntVar** objects
    :param result_label: label you want to put results
    :return: **None**
    """

    active_check_buttons: int = 0
    for i in tk_int_var:
        if i.get() == 1:
            active_check_buttons += 1

    codes_list: list = []
    for i in range(active_check_buttons):
        codes_list.append(generate_code(16))

    codes_as_string: str = "\n".join(codes_list)
    result_label.configure(text=codes_as_string)


def add_check_button(tk_int_var: check_button_type) -> bool:
    """
    function to add checkbox
    :param tk_int_var: iterable of **tk.IntVar** objects
    :return: return **True** if any checkbox changed, else **False**
    """

    result: bool = False
    for i in tk_int_var:
        if i.get() == 0:
            i.set(1)
            result = True
            break

    return result


def copy_code(result_label: tk.Label):
    pyperclip.copy(result_label.cget("text"))

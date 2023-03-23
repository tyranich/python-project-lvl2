from .json import json_formater
from .stylish import stylish
from .plain import plain


def choising_formater(formater):

    if formater == "stylish":
        return stylish
    elif formater == "plain":
        return plain
    elif formater == "json":
        return json_formater

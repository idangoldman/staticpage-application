from inspect import getmembers
from pprint import pprint

def view_obj(value):
    pprint(getmembers(value))

def comment_view_obj(value):
    pprint('################')
    pprint('################')
    pprint('################')
    pprint(getmembers(value))
    pprint('################')
    pprint('################')
    pprint('################')
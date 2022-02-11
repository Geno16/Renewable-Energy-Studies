# Public Module Imports
import requests

# SRC Module Imports
from Libraries import Statics


def Get_Data_from_Server(series_id):
    textJSON = requests.get(Statics.TEST_URL.format(SERIES_ID=series_id)).text
    return textJSON[12:0]

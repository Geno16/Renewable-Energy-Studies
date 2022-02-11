# Public Module Imports
import requests
import json

# Publci Class Imports
from abc import ABC

# Public Method Imports
from abc import abstractclassmethod as abstract

# SRC Module Imports
from Libraries.Statics import Vars


class Abstract_Data_Requestor(ABC):

    @abstract
    def __init__(self, retrival_url):
        self.__http = requests.get(
            retrival_url)
        self.__textJSON = self.__http.text
        self.__url = retrival_url

    def Get_HTTP(self):
        return self.__http

    def Get_Dict(self):
        return json.loads(self.__textJSON)

    def Get_Text(self):
        return self.__textJSON

    def Get_URL(self):
        return self.__url


class Series_Data_Requestor(Abstract_Data_Requestor):
    def __init__(self, series_id):
        super().__init__(Vars.URL + Vars.SERIES_TOKEN.format(series_id))


class Catagory_Data_Requestor(Abstract_Data_Requestor):
    def __init__(self, catagory_id):
        super().__init__(Vars.URL + Vars.CATAGORY_TOKEN.format(catagory_id))

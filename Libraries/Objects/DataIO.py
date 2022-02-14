# Public Module Imports
from ast import Return
import requests
import json
import pandas as pd

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

    @abstract
    def Get_DF(self, name='Data'):
        pass

    def Get_HTTP(self):
        return self.__http

    @abstract
    def Get_Dict(self):
        return json.loads(self.__textJSON)

    def Get_Text(self):
        return self.__textJSON

    def Get_URL(self):
        return self.__url


class Series_Data_Requestor(Abstract_Data_Requestor):
    def __init__(self, series_id):
        self.__series_id = series_id
        super().__init__(Vars.SERIES_URL + Vars.SERIES_TOKEN.format(series_id))

    def Get_Dict(self):
        return super().Get_Dict()['series']

    def Get_DF(self, name=None):

        if pd.isnull(name):
            name = 'Data'

        # Create the Initial Dataframe
        df = pd.DataFrame(data=self.Get_Dict()[0]['data'], columns=[
            'Month', name])

        # split the ID, and
        # add values for indexing
        idList = self.__series_id.split(".")
        df['Category'] = idList[0]
        df['Sub-Category'] = idList[1]
        df['State'] = idList[2].split('-')[1]

        # Return the re-indexed dataframe as a series.
        return df.set_index(keys=['Category', 'Sub-Category', 'State', 'Month']).squeeze()


class Catagory_Data_Requestor(Abstract_Data_Requestor):
    def __init__(self, catagory_id):
        super().__init__(Vars.CATAGORY_URL + Vars.CATAGORY_TOKEN.format(catagory_id))

    def Get_Dict(self):
        return super().Get_Dict()['category']

    def Get_DF(self, name=None):
        dict = self.Get_Dict()
        dfList = []
        for series in dict['childseries']:
            if pd.isnull(name):
                name = ' - '.join(series['name'].split(' : ')[0:2])

            if ".M" in series['series_id']:
                dfList.append(Series_Data_Requestor(
                    series['series_id']).Get_DF(name=name))

        return pd.concat(dfList)

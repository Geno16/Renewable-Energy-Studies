# Public module Imports
import pandas as pd
import numpy as np

from Libraries.Objects.DataIO import Catagory_Data_Requestor, Series_Data_Requestor


def main():
    NetGen = Series_Data_Requestor('ELEC.GEN.ALL-AL-99.A')

    print(NetGen.Get_Dict())

    NetGen = Catagory_Data_Requestor('1')

    print(NetGen.Get_Dict())


if __name__ == "__main__":
    main()

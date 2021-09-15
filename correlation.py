import numpy as np
import pandas as pd
import plotly_express as px
import csv


def getDataSource1(data_path):
    coffee=[]
    sleep=[]
    with open(data_path) as csv_file:
        csv_reader=pd.read_csv(csv_file)
        for row in csv_reader:
            coffee.append(float(row["coffee in ml"]))
            sleep.append(float(row["sleep in hours"]))

    return {"x":coffee,"y":sleep}

def getDataSource2(data_path):
    marks=[]
    days=[]
    with open(data_path) as csv_file:
        csv_reader=pd.read_csv(csv_file)
        for row in csv_reader:
            marks.append(float(row["marks"])),
            days.append(float(row["days present"]))

    return {"x":marks,"y":days}

def findCorrelation(dataSource):
    correlation=np.corrcoef(dataSource["x"],dataSource["y"])
    print("Correlation: ",correlation[0,1])

def plotFigure1(data_path):
    with open(data_path) as csv_file:
        df=pd.read_csv(csv_file)
        fig=px.scatter(df,x="coffee in ml", y="sleep in hours", size="coffee in ml", size_max=100)
        fig.show()

def plotFigure2(data_path):
    with open(data_path) as csv_file:
        df=pd.read_csv(csv_file)
        fig=px.scatter(df,x="days present", y="marks", color="marks")
        fig.show()

def setup1():
    data_path="coffee.csv"
    dataSource=getDataSource1(data_path)
    findCorrelation(dataSource)
    plotFigure1(data_path)
    
def setup2():
    data_path="grades.csv"
    dataSource=getDataSource2(data_path)
    findCorrelation(dataSource)
    plotFigure2(data_path)

setup1()
setup2()
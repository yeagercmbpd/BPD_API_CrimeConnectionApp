import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import qgrid
import os
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
import datetime
import numpy
import geopandas as gpd
from h3 import h3
from shapely.geometry import Polygon
from shapely.geometry import Point

Neighborhoods=gpd.read_file('https://opendata.arcgis.com/datasets/fc5d183b20a145009eae8f8b171eeb0d_0.geojson')

Slice=pd.read_pickle("./df.pkl")

basket = (Slice
          .groupby(['CrimeDate', 'Neighborhood'])['Description']
          .count().unstack().reset_index().fillna(0)
          .set_index('CrimeDate'))

def encode_units(x):
    if x <=0:
        return 0
    if x >= .1:
        return 1

basket_sets = basket.applymap(encode_units)

frequent_itemsets = apriori(basket_sets, min_support=0.6, use_colnames=True)

rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)


rules_sup1_conf75=rules[ (rules['lift'] >= 1.00) & (rules['confidence'] >= 0.75) ].sort_values('confidence',ascending=False)

MapFrame = rules_sup1_conf75
MapFrame['antecedentsList'] = [list(x) for x in MapFrame['antecedents']]
MapFrame['consequentsList'] = [list(x) for x in MapFrame['consequents']]

MapFrame=MapFrame.reset_index()
X=MapFrame.antecedentsList.apply(pd.Series) \
    .merge(MapFrame, left_index = True, right_index = True)

FirstFinished = X.melt(id_vars = ['index','consequentsList'],value_vars = [0], value_name = "antecedentsEach").dropna().drop("variable", axis = 1)

X2=FirstFinished.consequentsList.apply(pd.Series) \
    .merge(FirstFinished, left_index = True, right_index = True)

FinalFinished = X2.melt(id_vars = ['index','antecedentsEach'],value_vars = [0], value_name = "consequentsEach").dropna().drop("variable", axis = 1)

FinalFinished['antecedentsEach']=FinalFinished['antecedentsEach'].astype(str)
FinalFinished['consequentsEach']=FinalFinished['consequentsEach'].astype(str)

Neighborhoods.filter(['NBRDESC','LABEL','geometry'])

FinalShapeConnect = pd.merge(FinalFinished, Neighborhoods, left_on=["antecedentsEach"], right_on=["NBRDESC"])

FinalShapeConnect.rename(columns={'geometry':'Start'}, inplace=True)

FinalShapeConnect = pd.merge(FinalShapeConnect, Neighborhoods, left_on=["consequentsEach"], right_on=["NBRDESC"])

FinalShapeConnect.rename(columns={'geometry':'Finish'}, inplace=True)

FinalShapeConnect=gpd.GeoDataFrame(FinalShapeConnect, geometry=FinalShapeConnect.Start)

FinalShapeConnect['LatitudeStart']=FinalShapeConnect.representative_point().geometry.y
FinalShapeConnect['LongitudeStart']=FinalShapeConnect.representative_point().geometry.x

FinalShapeConnect=gpd.GeoDataFrame(FinalShapeConnect, geometry=FinalShapeConnect.Finish)

FinalShapeConnect['LatitudeFinish']=FinalShapeConnect.representative_point().geometry.y
FinalShapeConnect['LongitudeFinish']=FinalShapeConnect.representative_point().geometry.x

FinalShapeConnect = pd.merge(FinalShapeConnect, X.filter(['index','support','confidence','lift']), left_on=["index"], right_on=["index"])

df2=FinalShapeConnect.filter(['antecedentsEach','consequentsEach','LatitudeStart','LongitudeStart','LatitudeFinish','LongitudeFinish','Start','Finish','support','confidence','lift'])
df2.to_csv('connectionstest.csv')
df2.to_pickle("./Connections.pkl")

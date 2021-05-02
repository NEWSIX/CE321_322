import pandas as pd
from firebaseClass import firebaseClass as fireClass
from Analysis import Analysis as anls
from Analysis import plotGraph as plt

class mainClass:  
    def callfunction():  
        df = fireClass.Retrieving('WEB')                                            # Firebase Retrieving
        data = filterData.MergeData(df)
        viewRank = anls.viewRank(data)                                              # View Ranking
        #userRank = anls.userRank(data)                                             # User Ranking
        #fireClass.RankCommit('userRank',userRank)
        #fireClass.RankCommit('viewRank',viewRank)                                  # Update view rank Score
        
class filterData: 

    def cleanData(df):
        data = filterData.MergeData(df)                                             # Merge USER ID
        return data
    def MergeData(df):
        col = df.columns.drop(['ID'])                                               # Select All Attribute except ID
        df = df.groupby('ID')[col].first().reset_index()                            # Group Same Value in Attribute 'ID'
        return df


df = fireClass.Retrieving('viewRank')   
print(df)
#mainClass.callfunction()
#data = [ {'Page':"Page1_1",'views':5}                                              #TEST insert DATA
#             ,{'Page':"Page1_2",'views':20}
#             ,{'Page':"Page2_1",'views':11}
#             ,{'Page':"Page2_2",'views':31}
#             ,{'Page':"Page3_1",'views':3}
#             ,{'Page':"Page3_2",'views':6}]       
#fireClass.insert('https://javaproject-86658-default-rtdb.firebaseio.com/','',data)                  #TEST insert DATA
#fireClass.delete('https://javaproject-86658-default-rtdb.firebaseio.com/','WEB',None)               #TEST insert DATA
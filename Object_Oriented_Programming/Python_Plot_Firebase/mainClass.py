import pandas as pd                                                                       # Library  for using Datafram
from firebaseClass import firebaseClass as fireClass                                      # for using method firebaseClass in firebase class
from Analysis import Analysis as anls                                                     # for using method Analysis in Analysis class
from Analysis import plotGraph as plt                                                     # for using method firebase in Analysis class

class mainClass:  
    def callfunction():  
        df = fireClass.Retrieving('historyWEB')                                            # Firebase Retrieving
        print(df)
        data = anls.Ranking(df)
        fireClass.RankCommit('',data)
        
        #data = filterData.MergeData(df)
        #viewRank = anls.viewRank(data)                                                    # View Ranking
        #userRank = anls.userRank(data)                                                    # User Ranking
        #fireClass.RankCommit('userRank',userRank)
        #fireClass.RankCommit('viewRank',viewRank)                                         # Update view rank Score
        #df = df.groupby('username').groups

        
        
class filterData: 

    def cleanData(df):
        data = filterData.MergeData(df)                                                   # Merge USER ID
        return data
    def MergeData(df):
        col = df.columns.drop(['username'])                                               # Select All Attribute except ID
        df = df.groupby('username')[col].first().reset_index()                            # Group Same Value in Attribute 'ID'
        return df


mainClass.callfunction()                                                                  # Method Call
#data = [ {'Page':"Page1_1",'views':5}                                                    #TEST insert DATA
#             ,{'Page':"Page1_2",'views':20}
#             ,{'Page':"Page2_1",'views':11}
#             ,{'Page':"Page2_2",'views':31}
#             ,{'Page':"Page3_1",'views':3}
#             ,{'Page':"Page3_2",'views':6}]       
#fireClass.insert('https://javaproject-86658-default-rtdb.firebaseio.com/','',data)                  #TEST insert DATA
#fireClass.delete('https://javaproject-86658-default-rtdb.firebaseio.com/','WEB',None)               #TEST insert DATA

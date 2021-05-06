import pandas as pd                                                                 # Library  for using Datafram
import numpy as np                                                                  # Library  for using numpy
import matplotlib.pyplot as plt                                                     # Library  for using matplot
from statistics import mode                                                         # Library  for using statistics

class Analysis:
 #  def viewRank(df):                                                               # Ranking
 #      data = df.drop(['username'],axis=1)                                         # Select Attribute to Build Rank Score
 #      sum = np.sum(data)                                                          # sum value in data
 #      sum = sum.rank(ascending=False)                                             # Ranking by Pandas module
 #      sum = round(sum)                                                            # Round Num
 #      #sum = sum.astype(np.int64)                                                 # Set Float 64 to Integer 64
 #      sum = sum.sort_values()                                                     # Sort for Number of Rank
 #      sum = pd.DataFrame(sum,columns = ['Rank'])                                  # SET ROW(s) AND Column(s)
 #      sum = sum.transpose()                                                       # Martix Transpose
 #      colum = sum.columns                                                         # GET ATTRIBUTE NAME
 #      row = df.values.tolist()
 #      row = sum.values.tolist()                                                   # RANK Result                                        
 #      row = list(np.concatenate(row).flat)                                        # CONVERT ARRAY 2D TO 1D
 #      Rank = {colum[i]: row[i] for i in range(len(colum))}                        # SET RANKING TO ATTRIBUTE
 #      plotGraph.rankGraph(colum,row,'View Rank')                                  # plot
 #      return Rank

 #  def userRank(df):
 #      df["SUM"] = df.sum(axis=1)                                                  # Sum Row     
 #      df['Rank'] = df['SUM'].rank(ascending = False)                              # Ranking
 #      df = df.sort_values(by=['Rank'])                                            # Sort Rank
 #      x = df['ID']                                                                # Set Attribute to plot Rank Score
 #      y = round(df['Rank'])                                                       # Set Attribute to plot Rank Score & Round
 #      Rank = dict(zip(x, y))                                                      # Select Attribute to Build Rank Score                                              
 #      plotGraph.rankGraph(x,y,'User Rank')                                        # plot
 #      return Rank

    def Ranking(df):                                                                # Ranking Data 
        data = mode(df["product"])
        mm = [ { "Most Product Buy" :"000","Rank":"0"}
                ,{"Most Product Buy" :data,"Rank":"10"}
                ,{ "Most Product Buy" :"020","Rank":"0"}]
        return mm
   


class plotGraph():                                                                  #Plot
    def rankGraph(x,y,label):
        x = np.array(x)
        y = np.array(y)
        plt.ylabel(label)
        #plt.ylabel(xlabel)
        plt.bar(x, y)
        #plt.show()

 #class ML(self):
 #   def rec_content():

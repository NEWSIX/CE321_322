import pyrebase # https://github.com/thisbejim/Pyrebase
import pandas as pd
import numpy as np
from firebase import firebase as fb
                                                                                    #
class firebaseClass:
    def Retrieving(addr):                                                           # Config TO Firebase
        firebaseConfig = {                                                          
        "apiKey": "AIzaSyDVJn6ER2ATaspHaHFHVB0jU_s53tMlHJM",                        
        "authDomain": "javaproject-86658.firebaseapp.com",
        "databaseURL": "https://javaproject-86658-default-rtdb.firebaseio.com",
        "projectId": "javaproject-86658",
        "storageBucket": "javaproject-86658.appspot.com",
        "messagingSenderId": "449604717569",
        "appId": "1:449604717569:web:19059f5a8333a0901fc400",
        "measurementId": "G-SZ5KKGTP0S"
        }
        firebaseC=pyrebase.initialize_app(firebaseConfig)
        db = firebaseC.database()
        data = []
        user = db.child(addr).get()
        for user in user.each():                                                    # Retriev From Firebase
            #print(user.val())
            data.append(user.val())
            df = pd.DataFrame(data)
        return df

    def Commit(url,addr,att,value):                                                 # Commit or Update To Firebase
        firebaseC = fb.FirebaseApplication(url, None)
        firebaseC.put(addr,att,value) 

    def insert(url,addr,data):                                                      # Insert or Create New Schema(s)
        firebaseC = fb.FirebaseApplication(url, None)
        address = firebaseC.post(addr,data)
        print(address)
    
    def delete(url,addr,att):                                                       # Delete Shemas or Data
        firebaseC = fb.FirebaseApplication(url, None)
        firebaseC.delete(addr,att) 

    def RankCommit(rank,data):                                                      # Ranking Update
       # firebaseClass.delete('https://javaproject-86658-default-rtdb.firebaseio.com/',rank,None)
        firebaseClass.insert('https://javaproject-86658-default-rtdb.firebaseio.com/',rank,data) 



#firebaseClass.Commit('https://javaproject-86658-default-rtdb.firebaseio.com/','-MZ7pklV_oLTlSXkWSy8/0','Name','Bob6')
#data = {'ID':'0006','Name': 'Sean','Time':10,'view1':1,'view2':0,'view3':1}
#firebaseClass.insert('https://javaproject-86658-default-rtdb.firebaseio.com/',"WEB",data) 
#firebaseClass.Retrieving('DATA')
#firebaseClass.delete('https://javaproject-86658-default-rtdb.firebaseio.com/','WEB_HS',None)


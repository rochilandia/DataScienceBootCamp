
import pandas as pd 
import matplotlib.pyplot as plt
from functools import wraps

def prepost (*args,**kwargs):
    def inner (function):
        @wraps(function)
        def wrapper(*a, **k):
            if "url" in kwargs:
                df = pd.read_csv("url")
                print("IfCompleted")
            retval = function(*a, **k)
            df.hist()
            plt.show()
            print("graphDone-Correct")
            return retval
        return wrapper
    return inner

key_url = "http://winterolympicsmedals.com/medals.csv

@prepost(url=key_url)
def _f_protected ():
    l2 = [x for x in range(16)]
    z= lambda x : True if x > 5 else False
    return list(filter(z,l2))
    
_f_protected()


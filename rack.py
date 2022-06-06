import sys,random,time
import json,datetime
from rich.console import Console
from rich.progress import Progress,sys
types=["server_log","pip_log"]
data=''

#default settings
log_type=random.choice(types)
mode='normal'
limit=9999999999
if len(sys.argv)>1:
    for i in sys.argv[1:]:
        print(i)
        if '--type=' in i:
            i=i.split('--type')[-1]
            if i in types:
                log_type=i
        elif "--mode=" in i:
            i=i.split('--mode=')[-1]
            print(i)
            if i in ['incredible','fast','normal','slow']:
                mode=i
        elif '--limit=' in i:
            i=i.split('--limit=')[-1]
            try:
                i=int(i)
                limit=i
            except:
                pass
            
def load_data(filename,mode):
    global data
    with open(filename,mode) as f1:
        data=json.load(f1)
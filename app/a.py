import time
from rich.console import Console
from rich.progress import Progress,sys
import json,random
console=Console()
data=0
mode='normal'
limit=sys.maxsize
if len(sys.argv)>1:
    for i in sys.argv[1:]:
        print(i)
        
        if "--mode=" in i:
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
# incredible fast normal slow
if mode=='incredible':
    total_list=[200]
    step_list=[100,50]
elif mode=='fast':
    total_list=[300]
    step_list=[100,50]
elif mode=='normal':
    total_list=[200,500,400,600]
    step_list=[20,30,40]
elif mode=='slow':
    total_list=[500,700,600]
    step_list=[60,5,15,7,15,13]


with open("pip_log.json",'r') as f1:
    data=json.load(f1)

print(data)

def random_sleep():
    time.sleep(random.choice([1,0.5,0.4,0.3,0.2,0.1,0.02]))

for i in data['info']:
    console.print(i)
    random_sleep()

def progress_bar(total,step,delay,finish):
    with Progress() as progress:
        task1 = progress.add_task("[red]Downloading...", total=total)
        while not progress.finished:
            progress.update(task1, advance=step)
            time.sleep(delay)
    console.print(finish)

for i in range(1,limit):
    name,version=random.choice(list(data['packages'].items()))
    console.print("For package: "+name+":",style=f"{'blue'}")
    console.print("\t Downloading " + name+ " -->> total calculated size ("+str(random.choice(list(range(0,10))))+str(random.choice(list(range(0,10))))+"."+str(random.choice(list(range(0,10))))+"mb)" )
    print("suitable version on "+version )
    print("This lib is not at the path route please consider to move to the path route for env\n"*random.choice([0,1]),end='')
    progress_bar(random.choice(total_list),random.choice(step_list),0.02,"lib-->>>"+name+'downloading finished!-->>> local registered successfully!')
        
console.print("warnning: you are just using the package managing in version 3.0.0.1 but 3.0.0.2 is available, consider to upgrade the tool for more extensions".upper(),style='yellow')

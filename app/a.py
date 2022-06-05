import time
from rich.console import Console
from rich.progress import track,Progress
import json,random
console=Console()
data=0
non_stop=0
mode=''

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

total_tasks=random.choice(range(1,))
for i in range(1,99999):
    name,version=random.choice(list(data['packages'].items()))
    console.print("For package: "+name+":",style=f"{'blue'}")
    console.print("\t Downloading " + name+ " -->> total calculated size ("+str(random.choice(list(range(0,10))))+str(random.choice(list(range(0,10))))+"."+str(random.choice(list(range(0,10))))+"mb)" )
    print("suitable version on "+version )
    print("This lib is not at the path route please consider to move to the path route for env\n"*random.choice([0,1]),end='')
    progress_bar(random.choice([500,300,200,1000,700]),random.choice([7,12,15,100,70,4]),0.02,"lib-->>>"+name+'downloading finished!-->>> local registered successfully!')
        
console.print("warnning: you are just using the package managing in version 3.0.0.1 but 3.0.0.2 is available, consider to upgrade the tool for more extensions".upper(),style='yellow')

console.print(f"Hello World!", style= f"{'blue'}")

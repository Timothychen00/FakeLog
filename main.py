import sys,random,time
import json,datetime
log_type='server_log'
if len(sys.argv)==2:
    log_type=sys.argv[1]

def GetTimeStamp(format):
    if 'timestamp' in format:
        return datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))).strftime(format['timestamp'])
    else:
        return ''


def generate_fake_log(log_type):
    f1=open('settings.json',mode='r')
    data=json.load(f1)
    f1.close()
    print(data)
    
    if log_type in data:
        f2=open(log_type+'.json',mode='r')
        log_data=json.load(f2)
        sleep_time=log_data['sleep']
        separate=log_data['separate'][0]*log_data['separate'][1]
        
        
        #starting
        for i in log_data['data']['start']:
            print(GetTimeStamp(log_data['data'])+i)
            time.sleep(0.01)
        
        for k in range(100):
            print(separate)
            for i in log_data['data']['request']:
                if i!='url:':
                    print(i)
                else:
                    print(" url:  "+random.choice(log_data['method'])+"   "+random.choice(log_data['path'])+" HTTP/1.1")
                time.sleep(0.01)
            time.sleep(random.choice([0.01,0.01,0.01,0.01,0.01,0.03,0.05,0.07,0.1,0.2,0.4]))
        
        sleep_time=random.choice([0.01,0.01,0.01,0.03,0.05,0.07,0.1])
        time.sleep(sleep_time)
        print(sleep_time)
        print(log_data['type'])
        print(separate)
        f2.close()
    
    
generate_fake_log(log_type)
# datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))).strftime("%Y-%m-%d %H:%M:%S")
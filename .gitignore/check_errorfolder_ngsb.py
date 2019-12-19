import os
path = '/report/NgServiceBus'
try:
    for dirpath, dirnames, files in os.walk(path):
        if files:
            for dir in dirnames:
                dirpath = path+'/'+dir+'/'+'work'
                if os.path.exists(dirpath) and os.path.isdir(dirpath):
                    if not os.listdir(dirpath):
                        print(dirpath)
                        print("Directory is empty")
                    else:
                        print(dirpath)
                        print("### Directory is not empty ###")
except Exception as e:
    print(e)
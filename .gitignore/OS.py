import os


path = ("C:\\Users\\vteixeira\\Downloads\\")
print(path)

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
        for file in f:
            if '.csv' in file:
                files.append(os.path.join(r,file))

for f in files:
   os.rename(f,'C:\\Users\\vteixeira\\Downloads\\raw.csv')



import json as js
import sys

orig_stdout = sys.stdout

f = open('out.txt', 'w')
sys.stdout = f

with open('C:/Users/vteixeira/Documents/My Received Files/rede.txt') as js_file:
	data = js.load(js_file)
	for p in data['docs']:
		print(p['transactionId'])

sys.stdout = orig_stdout
f.close()
import json
import glob
import os
path="/home/rd/Documents/dust7/*"
for i in glob.glob(path):
	for j in glob.glob(i+"/*.json"):
		print(j)
		with open(j,"r+")as f:
			js=json.load(f)
			print(js['imagePath'])
			new_name=os.path.basename(j).split(".j")[0]
			for k in range(len(js["shapes"])):
				if js["shapes"][k]["label"] =="others":
					js["shapes"][k]["label"]="other"
					flag=True
		if flag==True:
			with open(j,"w+") as f:
				json.dump(js,f)
				flag=False

print("testing")

print("testing1")

import json

def read_json(filename):
    with open("../data/"+filename,"r",encoding="utf-8")as f:
        arr=[]
        for data in json.load(f).values():
            arr.append(list(data.values()))
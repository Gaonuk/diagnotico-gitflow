import json
import heapq
file = open("data.json", "r")

lines = file.readlines()

data = []
for line in lines:
    data.append(json.loads(line))

file.close()

def get_top_10_retweeted():
    top_10 = heapq.nlargest(10, data, key=lambda x:x["retweetCount"])
    return top_10

def main():
    pass
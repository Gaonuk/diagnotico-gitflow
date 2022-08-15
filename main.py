import json
import heapq

def load_data():
    file = open("data.json", "r")
    lines = file.readlines()
    data = []
    for line in lines:
        data.append(json.loads(line))
    file.close()
    return data

def get_top_10_retweeted(data):
    top_10 = heapq.nlargest(10, data, key=lambda x:x["retweetCount"])
    return top_10

def main():
    data = load_data()
    result = get_top_10_retweeted(data)
    print(result)

if __name__ == "__main__":
    main()
    
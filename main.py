import json
import heapq
from collections import Counter

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

def get_top_10_users_by_tweets(data):
    users = [x["user"]["username"] for x in data]
    counter = Counter(users)
    top_10 = counter.most_common(10)
    return top_10 

def main():
    data = load_data()
    print("Choose between the following functions:")
    print("1. Top 10 retweeted tweets")
    print("2. Top 10 users by tweets")
    print("3. Top 10 days with more tweets")
    print("4. Top 10 hashtags")
    user_input = int(input("Enter a number between 1 and 4: \n"))
    if user_input == 1:
        result = get_top_10_retweeted(data)
        print(result)
    elif user_input == 2:
        result = get_top_10_users_by_tweets(data)
        print(result)
    elif user_input == 3:
        pass
    elif user_input == 4:
        pass
    else:
        print("Invalid option.")


if __name__ == "__main__":
    main()
    
from twitterAPI import twitterAPI
import random
import time
import os

test = twitterAPI(os.environ['postgres_user'], os.environ['postgres_password'], 'twitterDB')
user_list = test.get_users()
n = 100

start_time = time.time()
for i in range(n):
    id = random.choice(user_list)
    timeline_list = test.home_timeline(id)
end_time = time.time()

timelines_per_sec = n / (end_time - start_time)
print("Timelines retrieved per second:", timelines_per_sec)
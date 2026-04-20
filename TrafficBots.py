import requests
import time

url = "http://quotes.toscrape.com"

request_times = []

print("Sending requests to:", url)

start_total = time.time()

for i in range(10):
    start = time.time()
    requests.get(url)
    end = time.time()

    request_times.append(end - start)

    time.sleep(0.1)   # simulate slight delay

end_total = time.time()

# Metrics
avg_time = sum(request_times) / len(request_times)
total_time = end_total - start_total

# Detection Logic
if avg_time < 0.3:
    result = "Bot Detected"
else:
    result = "Human User"

# Output
print("\n----- BOT DETECTION RESULT -----")
print("Website:", url)
print("Total Requests:", len(request_times))
print("Total Time Taken:", round(total_time, 2), "seconds")
print("Average Request Time:", round(avg_time, 3), "seconds")
print("Final Classification:", result)
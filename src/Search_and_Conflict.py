from datetime import datetime
import time 
from datetime import timedelta


# Functions below are designed to work with arrays of dictionaries(each event is a dictionary, and list of events is an array)

# Event = {"id": int, "title" : str, "date" : str, "time" : str, "location" : str }

# These functions cannot work with linked lists as indexing is not possible. It is not entirely impossible, but more complex to implement.

def linear_search(events, event_id):
    start_time = time.time()
    for e in events:
        if e["id"] == event_id:
            elapsed = time.time() - start_time
            print(f'Event found. Time elapsed: {elapsed}')
            return e
    
    # elapsed = time.time() - start_time
    # print(f'Event found. Time elapsed: {elapsed}')
    return None
    # Linear Search complexities:
    # Time Complexity: O(n)
    # Space Complexity: O(1)

def binary_search(events, event_id):
    start = time.time()
    low = 0
    high = len(events) - 1
    while low<=high:
        mid = (low+high)//2
        mid_id = events[mid]["id"]

        if mid_id == event_id:
            end = time.time() - start
            print(f'Found. Time elapsed: {end}')
            return events[mid]
        elif mid_id < event_id:
            low = mid + 1
        else:
            high = mid - 1
    print("Could not find event")
    return None

    # Binary Search complexities:
    # Time Complexity: O(log n)
    # Space Complexity: O(1)

def find_conflicts(events):
    def parse_datetime(event):
        date_string = f"{event['date']} {event['time']}"
        format_string = "%Y-%m-%d %H:%M"
        return datetime.strptime(date_string, format_string)

    sorted_events = sorted(events, key = lambda e: (e['date'], e['time'])) # Might have to use one of Sofie's sorting functions here
    
    for i in range(len(sorted_events)-1):
        e1 = sorted_events[i]
        e2 = sorted_events[i+1]

        if e1['date'] == e2['date']:
            t1_start = parse_datetime(e1)
            t1_end = t1_start + timedelta(hours=1)            
            t2_start = parse_datetime(e2)
            if t2_start < t1_end:
                print(f"{e1['id']} and {e2['id']} are conflicting on {e1['date']}")

    # Complexities for this function:
    # Time complexity: O(nlogn) due to sorting
    # Space complexity: O(n)

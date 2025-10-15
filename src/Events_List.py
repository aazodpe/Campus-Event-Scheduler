# define class 

class Events_List: 

    '''Array based list of event details 

    This class allows the user to create a list of events. Each element in the array is a dictionary 
    ----------------------------------
    Functions: 

    insert: insert an event at the end of the list 
    
    delete: Delete the event based on the ID 
    
    search_by_id: Returns event dictionary with matching id 

    list_all: Returns a copy of all events 

    
    '''
    # initialize array of event dictionaries 
    def __init__(self):
        self.data = []

    # Insert function
    def insert(self, event):
        self.data.append(event)

    # Delete 
    def delete(self, event_id):
        for i in range(len(self.data)): 
            if self.data[i]["id"] == event_id: 
                del self.data[i]
                return print(f'Event {event_id} deleted.')
        return print('Event not found, delete unsuccessful.')

    # Search for an event 
    def search_by_id(self, event_id): 

        for i in self.data: 
            if i['id'] == event_id:
                return i 

        return 'Event not found'
        
    # List all events 
    def list_all(self): 
        return self.data

#Generate n events:

def generate_events(n):
  '''
  Generates a list of n events. Note that this only generates dates and times, not location, ID, or title. This is because we only care       about the sorting performance, and the sorting is only based on date and time 
  
  '''
  
  import random
  
  events = Events_List()
  for i in range(n):
    events.insert({"date": f"2025-{random.randint(1,12):02d}-{random.randint(1,28):02d}",
                   "time": f"{random.randint(0,23):02d}:{random.randint(0,59):02d}"})
  return events

#Test runtime - Insertion:

def runtime(n, sort):
  import time 
    
  events = generate_events(n)
  begin = time.time()
  sort(events.data,'date','time')
  end = time.time()
  return end-begin




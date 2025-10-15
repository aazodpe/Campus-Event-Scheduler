
'''Sorting Algorithms
-------------------------------------------------
Below are the sorting algorithms. These are to be called as any other method of the class, and will re-define the event
array to be the sorted list. 

Algorithms: 

1. insertion_sort
2. merge_sort 
3. quick_sort 

'''

def insertion_sort(events, sort_by1, sort_by2=None):
    '''Parameters: 
    
    sort_by1 (str): Name of the dictionary key by which the list is to be sorted. To sort by date, 
                    call insertion_sort(events, 'date')
    sort_by2 (str): Default None, secondary sorting parameter to sort by time of day. Call 
                    insertion_sort(events, 'date', 'time')

    '''
    
    for i in range(1, len(events)):
        key = events[i]
        j = i - 1

        while j >= 0 and (events[j][sort_by1], events[j][sort_by2]) > (key[sort_by1], key[sort_by2]):
            events[j + 1] = events[j]
            j -= 1

        events[j + 1] = key

    return events



# Merge sort
def merge_sort(events, sort_by1, sort_by2):
    '''
    Note: When calling this function with an instance of the Events_List class, events parameter 
          must be events.data

    Parameters: 
        events: events.data 
        sort_by1 (str): Name of the dictionary key by which the list is to be sorted. To sort by date, 
                    call insertion_sort(events, 'date')
        sort_by2 (str): Default None, secondary sorting parameter to sort by time of day. Call 
                    insertion_sort(events, 'date', 'time') 
    
    '''
    #splits events into individual arrays each with length 1.
    if len(events)>1:
      mid = len(events) // 2
      left = events[:mid]
      right = events[mid:]

      left_sorted = merge_sort(left,sort_by1,sort_by2)
      right_sorted = merge_sort(right,sort_by1,sort_by2)

      i = j = k = 0

      #compare each array and place back into events
      while i < len(left) and j < len(right):
        if (left[i][sort_by1],left[i][sort_by2]) <=(right[j][sort_by1],right[j][sort_by2]):
          events[k]=left[i]
          i+=1

        else:
          events[k]=right[j]
          j+=1

        k+=1

      while i < len(left):
        events[k]=left[i]
        i+=1
        k+=1

      while j < len(right):
        events[k]=right[j]
        j+=1
        k+=1

    return events

# #Quick Sort

def quick_sort(events, sort_by1, sort_by2):
  
  def partition(events,low,high):

    pivot = (events[high][sort_by1],events[high].get(sort_by2,""))
    i = low -1
    for j in range(low,high):
      current = (events[j][sort_by1],events[j].get(sort_by2,""))
      if current <=pivot:
        i +=1
        events[i],events[j] = events[j],events[i]

    (events[i+1],events[high]) = (events[high],events[i+1])
    return i+1


  def _quick_sort(events,low,high):
    if low < high:
      new = partition(events,low,high)
      _quick_sort(events,low,new-1)
      _quick_sort(events,new+1,high)

  _quick_sort(events,0,len(events)-1)
  return events

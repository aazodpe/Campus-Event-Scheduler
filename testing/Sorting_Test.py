
# For arrays
trials = [10,50,100, 500,1000, 3000, 5000, 10000]
runtimes_insertion = []
runtimes_merge = []
runtimes_quick = []

for n in trials:
  s1 = runtime(n,LinkedEvents.insert_sort)
  runtimes_insertion.append(s1)
  # s2 = runtime(n,merge_sort)
  # runtimes_merge.append(s2)
  # s3 = runtime(n,quick_sort)
  # runtimes_quick.append(s3)

plt.figure(figsize=(6,6))
plt.semilogy(trials,runtimes_insertion, marker = 'o', label = 'Insertion Sort')
# plt.semilogy(trials,runtimes_merge, marker = 'x', label = 'Merge Sort')
# plt.semilogy(trials,runtimes_quick,marker='*',label ='Quick Sort')
# plt.legend()


# For linked List
trials = [10,50,100, 500,1000, 3000, 5000, 10000]
runtimes_insertion = []
runtimes_merge = []
runtimes_quick = []

for n in trials:
  s1 = runtime(n,insertion_sort)
  runtimes_insertion.append(s1)
  s2 = runtime(n,merge_sort)
  runtimes_merge.append(s2)
  s3 = runtime(n,quick_sort)
  runtimes_quick.append(s3)

plt.figure(figsize=(6,6))
plt.semilogy(trials,runtimes_insertion, marker = 'o', label = 'Insertion Sort')
plt.semilogy(trials,runtimes_merge, marker = 'x', label = 'Merge Sort')
plt.semilogy(trials,runtimes_quick,marker='*',label ='Quick Sort')
plt.legend()
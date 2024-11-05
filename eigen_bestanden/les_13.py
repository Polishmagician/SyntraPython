from queue import Queue
#Maak een queue aan met 4 posities
q = Queue(maxsize=4)
q.put("a")
print(q.get())
print(q.get())
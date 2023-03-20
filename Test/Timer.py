from threading import Timer

counter = 0

def increment_counter():
    global counter
    counter += 1
    print(counter)
    t = Timer(1.0, increment_counter)
    t.start()

increment_counter()
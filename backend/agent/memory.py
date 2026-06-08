MEMORY = []

def store(event: dict):
    MEMORY.append(event)

def recall():
    return MEMORY[-10:]

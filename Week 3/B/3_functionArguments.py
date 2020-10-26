def greet(message, name = "Max"):
    print("Hi", name + ", " + message)

def total_score(*scores):
    total = 0
    for score in range(0, len(scores)):
        total += scores[score]*(score + 1)
    return total

# greet("some message", "Tom")
print(total_score(1,3,4))
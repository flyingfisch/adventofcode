import hashlib

def checkHash(h, numOfZeros):
    hashIsValid = True

    if len(h) > numOfZeros:
        for i in range(0, numOfZeros):
            if h[i] != '0':
                hashIsValid = False

    return hashIsValid

def findAnswer(key, numOfZeros):
    i = -1
    h = hashlib.md5()

    while not checkHash(h.hexdigest(), numOfZeros):
        i += 1

        h = hashlib.md5()
        h.update((key + str(i)).encode('utf-8'))

    return i

print(findAnswer('abcdef', 5))
print(findAnswer('yzbqklnj', 5))
print(findAnswer('yzbqklnj', 6))

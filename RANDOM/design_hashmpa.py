class Bucket:

    def __init__(self):
        self.bucket = []

    def put(self, key: int, value: int) -> None:
        found = False
        for idx, item in enumerate(self.bucket):
            if item[0] == key:
                found = True
                self.bucket[idx] = (key, value)

        if not found:
            self.bucket.append((key, value))

    def get(self, key: int) -> int:
        found = False
        for idx, item in enumerate(self.bucket):
            if item[0] == key:
                return item[1]

        return -1

    def remove(self, key: int) -> None:
        for idx, item in enumerate(self.bucket):
            if item[0] == key:
                del self.bucket[idx]


class MyHashMap:

    def __init__(self):
        self.maxnum = 2069
        self.h = [Bucket() for i in range(self.maxnum)]

    def put(self, key: int, value: int) -> None:
        hash_key = key % self.maxnum
        self.h[hash_key].put(key, value)

    def get(self, key: int) -> int:
        hash_key = key % self.maxnum
        return self.h[hash_key].get(key)

    def remove(self, key: int) -> None:
        hash_key = key % self.maxnum
        self.h[hash_key].remove(key)

    # Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
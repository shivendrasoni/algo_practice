import mmh3
import math
from bitarray import bitarray

class BloomFilter:

    def __init__(self, size, hash_count):
        self.size = size
        self.hash_count = hash_count
        self.bit_array = bitarray(size)
        self.bit_array.setall(0)
        
    def add(self, string):
        for seed in range(self.hash_count):
            result = mmh3.hash(string, seed) % self.size
            self.bit_array[result] = 1
        
    def lookup(self, string):
        for seed in range(self.hash_count):
            result = mmh3.hash(string, seed) % self.size
            if self.bit_array[result] == 0:
                return "Not Present"
        return "Probably present"

    def negative_lookup(self, string):
        for seed in range(self.hash_count):
            result = mmh3.hash(string, seed) % self.size
            if self.bit_array[result] == 0:
                return True
        return False

def calculate_k(m, n):
    return (m/n) * math.log(2)
  
if __name__ == "__main__":
    
    n = 20  # no of items to add
    p = 0.6  # false positive probability
    
    m = -(n * math.log(p)) / (math.log(2) ** 2)  # size of bit array
    k = calculate_k(m, n)  # no of hash functions
    
    bloomf = BloomFilter(int(m), int(k))
    items = ["dog", "cat", "bird", "butterfly", "elephant"]
    
    for item in items:
        bloomf.add(item)
    
    print(bloomf.lookup("dog"))
    print(bloomf.lookup("cat"))
    print(bloomf.lookup("chicken"))

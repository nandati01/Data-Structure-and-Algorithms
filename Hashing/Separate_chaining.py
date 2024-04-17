BUCKET_SIZE = 7
class Hash:
    def __init__(self, bucket):
        self.bucket = bucket
        self.table = [[] for _ in range(bucket)] #creating a list of empty lists
    
    def hash_function(self, key):
        """Simple hash function to map keys to its indeces"""
        return key % self.bucket
    
    def insert_item(self, key):
        """Inserts a key into a hash table"""
        index = self.hash_function(key)
        return self.table[index].append(key)
    
    def delete_item(self, key):
        """Deletes a key from the hash table"""
        index = self.hash_function(key)
        if key not in self.table[index]:
            return
        return self.table[index].remove(key)
    
    def display_hash(self):
        """Displays the contents of the hash table"""
        for i in range(self.bucket):
            print(f"[{i}]", end = '')
            for key in self.table[i]:
                print(f"--> {key}", end = '')
            print()
            
if __name__ == "__main__":
    keys = [15, 11, 27, 8, 12, 9, 20]
    h = Hash(BUCKET_SIZE)
    #insert keys into the hash table
    for key in keys:
        h.insert_item(key)
    #display the hash table
    h.display_hash()
    #delete a key from the hash table
    h.delete_item(12)
    print("\nHash table after deleting 12:")
    h.display_hash()

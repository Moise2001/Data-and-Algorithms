# Create Hash Map class
class CreateHashTable:
    def __init__(self, initial_capacity=20):
        self.buckets = [[] for _ in range(initial_capacity)]

    # Inserts a new item into the hash table
    def insert(self, key, item):
        bucket = hash(key) % len(self.buckets)
        bucket_list = self.buckets[bucket]

        # Update the item if the key already exists
        for i, (existing_key, existing_item) in enumerate(bucket_list):
            if existing_key == key:
                bucket_list[i] = (key, item)
                return True

        # Insert the item to the end of the bucket list
        bucket_list.append((key, item))
        return True

    # Lookup items in hash table
    def lookup(self, key):
        bucket = hash(key) % len(self.buckets)
        bucket_list = self.buckets[bucket]

        for existing_key, existing_item in bucket_list:
            if key == existing_key:
                return existing_item

        return None

    # Hash remove method - removes item from hash table
    def remove(self, key):
        bucket = hash(key) % len(self.buckets)
        bucket_list = self.buckets[bucket]

        # Find the index of the key in the bucket list and remove it
        for i, (existing_key, _) in enumerate(bucket_list):
            if key == existing_key:
                del bucket_list[i]
                return True

        return False  # Key not found

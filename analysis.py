import time
import random
import sys
from quickSort import randomized_quicksort, deterministic_quicksort
from hashTable import HashTable

def generate_array(size, type='random'):
    if type == 'random':
        return [random.randint(1, 1000) for _ in range(size)]
    elif type == 'sorted':
        return list(range(1, size + 1))
    elif type == 'reverse':
        return list(range(size, 0, -1))
    elif type == 'repeated':
        return [random.randint(1, 10) for _ in range(size)]

def time_sort(sort_func, arr):
    start = time.time()
    sorted_arr = sort_func(arr.copy())
    end = time.time()
    return end - start, sorted_arr

def compare_quicksorts(f):
    sizes = [100, 1000, 10000, 100000]
    types = ['random', 'sorted', 'reverse', 'repeated']
    
    f.write("Quicksort Analysis:\n")
    for size in sizes:
        f.write(f"\nArray size: {size}\n")
        for type in types:
            arr = generate_array(size, type)
            random_time, random_sorted = time_sort(randomized_quicksort, arr)
            det_time, det_sorted = time_sort(deterministic_quicksort, arr)
            f.write(f"  {type.capitalize()} array:\n")
            f.write(f"    Randomized Quicksort: {random_time:.6f} seconds\n")
            f.write(f"    Deterministic Quicksort: {det_time:.6f} seconds\n")
            
            # Verify sorting
            assert random_sorted == sorted(arr), "Randomized Quicksort failed"
            assert det_sorted == sorted(arr), "Deterministic Quicksort failed"

def test_hash_table(f):
    f.write("\nHash Table Analysis:\n")
    ht = HashTable()

    # Insert
    start = time.time()
    for i in range(1000):
        ht.insert(f"key{i}", f"value{i}")
    insert_time = time.time() - start
    f.write(f"Insert 1000 items: {insert_time:.6f} seconds\n")

    # Search
    start = time.time()
    for i in range(1000):
        value = ht.search(f"key{i}")
        assert value == f"value{i}", f"Search failed for key{i}"
    search_time = time.time() - start
    f.write(f"Search 1000 items: {search_time:.6f} seconds\n")

    # Delete
    start = time.time()
    for i in range(1000):
        ht.delete(f"key{i}")
    delete_time = time.time() - start
    f.write(f"Delete 1000 items: {delete_time:.6f} seconds\n")

    # Example usage
    f.write("\nHash Table Example Usage:\n")
    ht.insert("name", "Alice")
    ht.insert("age", "30")
    ht.insert("city", "New York")
    
    f.write(f"Name: {ht.search('name')}\n")
    f.write(f"Age: {ht.search('age')}\n")
    f.write(f"City: {ht.search('city')}\n")
    
    ht.delete("age")
    f.write(f"Age after deletion: {ht.search('age')}\n")

if __name__ == "__main__":
    with open('output.txt', 'w') as f:
        compare_quicksorts(f)
        test_hash_table(f)
    print("Output has been written to output.txt")
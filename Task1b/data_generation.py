from pathlib import Path
import importlib.util, sys
import random, time

# Go up one level from Task1b to ADS-draft
PROJECT_ROOT = Path(__file__).resolve().parent.parent
CH10 = PROJECT_ROOT / "clrsPython" / "Chapter 10"
CH11 = PROJECT_ROOT / "clrsPython" / "Chapter 11"

for p in (str(CH11), str(CH10)):
    if p not in sys.path:
        sys.path.insert(0, p)

CH11_FILE = CH11 / "chained_hashtable.py"
spec = importlib.util.spec_from_file_location("chained_hashtable", CH11_FILE)
ch = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ch)

def generate_data(n):

    return list(range(n))

def build_hashtable(n, table_size=None):
    if table_size is None:
        table_size = n * 2 + 1  # Simple heuristic for table size
    h = ch.ChainedHashTable(table_size)
    dataset = generate_data(n)
    for item in dataset:
        h.insert(item)
    return h

def measure_average_search_time(h, n, num_queries=10000):
    """Measure average time per search over num_queries random queries"""
    total_time = 0
    
    for _ in range(num_queries):
        # Pick a random station name to search for
        random_key = random.randint(0, n - 1)
        
        # Measure time for this single search
        start_time = time.time()
        h.search(random_key)
        end_time = time.time()
        
        total_time += (end_time - start_time)
    
    # Calculate average
    average_time = total_time / num_queries
    return average_time, total_time, num_queries

if __name__ == "__main__":
    # Test different dataset sizes as required
    dataset_sizes = [1000, 5000, 10000, 25000, 50000]
    
    print("=" * 70)
    print("EMPIRICAL PERFORMANCE MEASUREMENT - CHAINED HASH TABLE")
    print("=" * 70)
    
    for n in dataset_sizes:
        print(f"\n Dataset Size: n = {n} ")
        
        h = build_hashtable(n)

        avg_time, total_time, num_queries = measure_average_search_time(h, n)
        
        # Display results
        print(f"\nResults for n = {n}:")
        print(f"  Number of queries: {num_queries}")
        print(f"  Total time: {total_time:.6f} seconds")
        print(f"  Average time per search: {avg_time:.9f} seconds")
     
    

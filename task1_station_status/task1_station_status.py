"""
Task 1a: Station Status System using CLRS chained hash table (separate chaining)

  clrsPython/
    Chapter 10/   (contains dll_sentinel.py)
    Uses DLLSentinel from Chapter 10 (a doubly linked list with a sentinel node) to store multiple items in the same
    hash bucket (handles collisions cleanly)

    Chapter 11/   (contains chained_hashtable.py, hash_functions.py)
    Uses a hash function from Chapter 11 to map each station name to a bucket index (ensures items are distributed
    across the table)
    division_hash (Chapter 11) to compute bucket indices for station name

"""

from pathlib import Path
import sys

# Using CLRS chapter folders to import Python's path
PROJECT_ROOT = Path(__file__).resolve().parent
CH10 = PROJECT_ROOT / "clrsPython" / "Chapter 10"
CH11 = PROJECT_ROOT / "clrsPython" / "Chapter 11"

# Putting both chapters at the front of sys.path so chained_hashtable's local imports work
for p in (str(CH11), str(CH10)):
    if p not in sys.path:
        sys.path.insert(0, p)

# pathlib builds the correct path to 'clrsPython/Chapter 11/chained_hashtable.py'
# importlib creates a module spec and loads it dynamically at runtime
from pathlib import Path
import importlib.util

PROJECT_ROOT = Path(__file__).resolve().parent
CH11_FILE = PROJECT_ROOT / "clrsPython" / "Chapter 11" / "chained_hashtable.py"

spec = importlib.util.spec_from_file_location("chained_hashtable", CH11_FILE)
ch = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ch)


# My five stations
STATIONS = [
    "Ealing Broadway",
    "Acton Main Line",
    "Paddington",
    "Bond Street",
    "Tottenham Court Road",
]

def main():
    # Small table size so collisions are visible in the bucket printout
    table_size = 7
    h = ch.ChainedHashTable(table_size)

    print("Inserting stations into CLRS chained hash table:\n")
    for s in STATIONS:
        print(f"  + {s}")
        h.insert(s)

    # Print internal state for manual-vs-code comparison
    print("\nHash Table Buckets after Insertion:")
    # Most CLRS ports expose underlying buckets via h.table each bucket is a Python list / chain
    for i, bucket in enumerate(h.table):
        print(f"Bucket {i}: {bucket}")

    # To test our code implementation
    print("\nSearch tests:")
    for q in ["Waterloo", "Paddington"]:
        found = h.search(q)
        print(f"  {q:>22} -> {'FOUND' if found else 'NOT FOUND'}")

if __name__ == "__main__":
    main()


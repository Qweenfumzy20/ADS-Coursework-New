"""
Task 1(a) — Operational Station Status (Hash Table)
Uses CLRS ChainedHashTable (separate chaining) + local copy of CLRS hashpjw.
hashpjw converts a string into a numeric value that can be used as an index in the hash table
"""

from pathlib import Path
import sys
import importlib.util

# locate and import the clrs chainedhashtable class
Root = Path(__file__).resolve().parent
CH10 = Root / "clrsPython" / "Chapter 10" # folder containing clrs linked list implementation
CH11 = Root / "clrsPython" / "Chapter 11" # folder containing clrs hash table implementation

#adding the two clrs chapter directories to python's import, so as to import their modules
for p in (CH11, CH10):
    if str(p) not in sys.path:
        sys.path.insert(0, str(p))

# to load a python file as a module
def _load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)  # type: ignore[attr-defined]
    return mod

chained_hashtable = _load_module("chained_hashtable", CH11 / "chained_hashtable.py")
ChainedHashTable = chained_hashtable.ChainedHashTable

# Local copy of CLRS hashpjw to avoid importing hash_functions (which depends on miller_rabin)
def hashpjw(key: str) -> int:
    h = 0
    for ch in str(key):
        h = (h << 4) + ord(ch)
        high = h & 0xF0000000
        if high != 0:
            h ^= high >> 24
            h &= ~high
    return h

# dataset of 5 stations
STATIONS = [
    "Paddington",
    "Bond Street",
    "Tottenham Court Road",
    "Farringdon",
    "Liverpool Street"
]

#Helpers to print the internal state of the CLRS DLLSentinel buckets
def bucket_as_list(bucket) -> list[str]:
 # Return the list of keys in a DLLSentinel chain (head -> tail).
    out = []
    cur = bucket.sentinel.next
    while cur is not bucket.sentinel:
        out.append(cur.data)
        cur = cur.next
    return out

def print_table_state(h: ChainedHashTable) -> None:
    # Print each table and the list of stations stored in that bucket (internal state)
    for i, bucket in enumerate(h.table):
        print(f"      bucket {i}: {bucket_as_list(bucket)}")

# Compute which bucket a given key will go into
def bucket_index(h: ChainedHashTable, key: str) -> int:
    return h.hash_function(h.get_key(key)) % h.m

# perform insertions and status checks with detailed tracing
def main():
    # create a small table with 7 bucket so collisions are visible
    m = 7
    h = ChainedHashTable(m=m, hash_func=hashpjw)

# inserting the stations one after the other
    print("== Inserting stations into our chosen data structure\n")
    for s in STATIONS:
        slot = bucket_index(h, s)
        print(f"  + insert '{s}'  -> bucket {slot}")
        h.insert(s)

        # display the internal state after each insertion
        print("    state after insert:")
        print_table_state(h)
        print()  # blank line for readability

    # Trace a successful status check
    present = "Paddington"
    slot = bucket_index(h, present)
    print(f"== Trace: check status of '{present}' ==")
    print(f"  bucket = hashpjw('{present}') % {h.m} = {slot}")
    print(f"  traverse bucket {slot} chain: {bucket_as_list(h.table[slot])}")
    found_station = h.search(present)
    print(f"  result: {'FOUND' if found_station else 'NOT FOUND'}\n")

    # Trace an unsuccessful status check
    absent = "Waterloo"
    slot_abs = bucket_index(h, absent)
    print(f"== Trace: check status of '{absent}' ==")
    print(f"  bucket = hashpjw('{absent}') % {h.m} = {slot_abs}")
    print(f"  traverse bucket {slot_abs} chain: {bucket_as_list(h.table[slot_abs])}")
    found_station2 = h.search(absent)
    print(f"  result: {'FOUND' if found_station2 else 'NOT FOUND'}")

if __name__ == "__main__":
    main()

from pathlib import Path
import importlib.util, sys

PROJECT_ROOT = Path(__file__).resolve().parent
CLRS_ROOT = PROJECT_ROOT / "clrsPython"



CH10 = CLRS_ROOT / "Chapter 10"
CH11 = CLRS_ROOT / "Chapter 11"
CH11_FILE = CH11 / "chained_hashtable.py"

print("Using CLRS path:", CH11_FILE)


# Make Chapter 10/11 available for their internal imports
for p in (str(CH11), str(CH10)):
    if p not in sys.path:
        sys.path.insert(0, p)

# Load the module
spec = importlib.util.spec_from_file_location("chained_hashtable", CH11_FILE)
ch = importlib.util.module_from_spec(spec)
sys.modules["chained_hashtable"] = ch
spec.loader.exec_module(ch)
# --- end path setup ---



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
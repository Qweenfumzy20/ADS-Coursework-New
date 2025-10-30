# ---- Simple dataset ---------------------------------------------------------
STATIONS = [
    "London Euston",
    "Reading",
    "Oxford",
    "Bristol Temple Meads",
    "Manchester Piccadilly",
]

NOT_PRESENT = "Leeds"  # for negative membership tests


# ---- HashSet version (uses Python's built-in set) ---------------------------
def hashset_ops(stations):
    """Insert, membership test, and deletion using a hash set."""
    s = set()

    # Insert
    for name in stations:
        s.add(name)

    # Membership tests (present + not present)
    _ = "Oxford" in s
    _ = NOT_PRESENT in s

    # Deletion (remove a couple)
    s.discard("Reading")
    s.discard("Oxford")

    return s


# ---- Minimal BST implementation --------------------------------------------
class BSTNode:
    def __init__(self, key: str):
        self.key = key
        self.left = None
        self.right = None


class BST:
    """A simple, beginner-friendly BST for strings (lexicographic order)."""

    def __init__(self):
        self.root = None

    # Insert a key into the BST
    def insert(self, key: str):
        def _insert(node, key):
            if node is None:
                return BSTNode(key)
            if key < node.key:
                node.left = _insert(node.left, key)
            elif key > node.key:
                node.right = _insert(node.right, key)
            else:
                # already present; do nothing
                pass
            return node

        self.root = _insert(self.root, key)

    # Check if a key exists
    def contains(self, key: str) -> bool:
        node = self.root
        while node:
            if key == node.key:
                return True
            node = node.left if key < node.key else node.right
        return False

    # Delete a key from the BST
    def delete(self, key: str):
        def _min_node(n):
            while n.left:
                n = n.left
            return n

        def _delete(node, key):
            if node is None:
                return None
            if key < node.key:
                node.left = _delete(node.left, key)
            elif key > node.key:
                node.right = _delete(node.right, key)
            else:
                # Found node to delete: 3 cases
                if node.left is None and node.right is None:  # leaf
                    return None
                if node.left is None:                         # one child (right)
                    return node.right
                if node.right is None:                        # one child (left)
                    return node.left
                # two children: swap with inorder successor and delete it
                successor = _min_node(node.right)
                node.key = successor.key
                node.right = _delete(node.right, successor.key)
            return node

        self.root = _delete(self.root, key)


def bst_ops(stations):
    """Insert, membership test, and deletion using a BST."""
    t = BST()

    # Insert
    for name in stations:
        t.insert(name)

    # Membership tests (present + not present)
    _ = t.contains("Oxford")
    _ = t.contains(NOT_PRESENT)

    # Deletion (remove a couple)
    t.delete("Reading")
    t.delete("Oxford")

    return t


# ---- Simple benchmark to compare -------------------------------------------
from time import perf_counter

def time_function(fn, repeats=20_000):
    start = perf_counter()
    for _ in range(repeats):
        fn(STATIONS)
    end = perf_counter()
    return end - start


def main():
    # Run once to show the internal results are sane
    print("=== Demo run (single execution) ===")
    hs_after = hashset_ops(STATIONS)
    print("HashSet remaining:", hs_after)  # should be without Reading & Oxford

    bst_after = bst_ops(STATIONS)
    # quick membership checks after deletes
    print("BST contains 'Reading'?", bst_after.contains("Reading"))
    print("BST contains 'Oxford'?", bst_after.contains("Oxford"))
    print("BST contains 'London Euston'?", bst_after.contains("London Euston"))
    print()

    # Benchmark (repeat many times to magnify differences)
    print("=== Benchmark (higher is slower) ===")
    hs_time = time_function(hashset_ops)
    bst_time = time_function(bst_ops)
    print(f"HashSet total time: {hs_time:.4f} s")
    print(f"BST     total time: {bst_time:.4f} s")

    # Quick takeaway
    if hs_time < bst_time:
        print("\nTakeaway: Hash set was faster in this workload (expected for insert/delete/membership).")
    else:
        print("\nTakeaway: BST was faster here (unusual on small in-memory sets, but possible).")


if __name__ == "__main__":
    main()

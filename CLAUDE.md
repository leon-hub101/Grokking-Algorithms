# Grokking Algorithms — Algorithm Study

Personal practice repository working through algorithms from the "Grokking Algorithms" book by Aditya Bhargava. Implementations in both JavaScript and Python.

## Tech Stack

- **JavaScript** (Node.js) — no dependencies, run with `node <file>`
- **Python 3** — no dependencies, run with `python <file>`
- No build tools, no package manager, no test framework

## Structure

All files are in the root directory (flat structure):

```
Grokking-Algorithms/
├── Binary-search-algo.js         # Binary search (3 variants: binarySearch1/2/3)
├── Binary_search_test_file.js    # JS binary search tests (inline)
├── Binary_search_test_file.py    # Python binary search implementation + tests
├── Selection-Sort-Algo.js        # Selection sort + findSmallest() helper
├── selectionSort_test_file.js    # JS selection sort tests (inline)
├── selectionSort_test_file.py    # Python selection sort + tests (with docs)
└── testFile.py                   # Scratch/minimal test file
```

## Running Files

```bash
node Binary-search-algo.js
node selectionSort_test_file.js
python Binary_search_test_file.py
python selectionSort_test_file.py
```

## Algorithms Covered

| Algorithm | JS | Python | Notes |
|-----------|----|----|-------|
| Binary Search | ✓ | ✓ | 3 JS variants (iterative approaches) |
| Selection Sort | ✓ | ✓ | Uses `findSmallest()` helper |

## Conventions

- Algorithm files: main implementation (e.g. `Binary-search-algo.js`)
- Test files: include `test_file` in the name
- Tests are inline with data — no separate test framework
- Both JS and Python versions maintained side-by-side for comparison

## Status

Active study project. Currently through Chapter 2 (Binary Search + Selection Sort). Follow the book chapter order when adding new algorithms.

```markdown
# Minimum Spanning Tree Algorithm

This Python project implements a GraphOptimization algorithm for finding the minimum spanning tree of a graph. It provides an efficient way to connect all nodes in a graph with the minimum possible total edge weight. This README will guide you on how to use the project and provide examples for better understanding.

## Table of Contents

- [Installation and Setup](#installation-and-setup)
- [Execution](#execution)
- [Input Format](#input-format)
- [Example](#example)
- [Collaboration](#collaboration)

## Installation and Setup

1. **Clone the Repository:** First, clone this repository to your local machine using the following command:

   ```bash
   git clone https://github.com/your-username/GraphOptimization.git
   ```

2. **Open a Terminal:** Open a terminal or command prompt on your local machine.

3. **Navigate to the Project Directory:** Use the `cd` command to navigate to the directory where the project code is located. For example:

   ```bash
   cd kruskals-minimum-spanning-tree
   ```

## Execution

To run the project, execute the following command:

```bash
python GraphOptimization.py
```

## Input Format

- The project reads a text file named `graph.txt` in the project directory.
- The text file should contain an adjacency matrix representing the graph.
- Each line should represent a node's connections to other nodes, separated by spaces.
- The distance to self (diagonal elements) should be marked as 0, and unconnected nodes should use a placeholder (e.g., -1).

Here's an example of the input format:

```
0 2 -1 4 -1
2 0 3 -1 -1
-1 3 0 -1 5
4 -1 -1 0 1
-1 -1 5 1 0
```

## Example

For a given input graph, the project will find and display the minimum spanning tree.

## Collaboration

This project is open for collaboration and contributions. Feel free to use it, modify it, and contribute to its development. It is released under the [MIT License](LICENSE).

Happy graph optimization!

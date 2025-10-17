#!/usr/bin/env python3
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, List, Optional, Tuple

@dataclass
class TreeNode:
    value: Any
    children: List[Tuple[Optional[Any], "TreeNode"]] = field(default_factory=list)

    def add_child(self, child_value: Any, edge_value: Optional[Any] = None) -> "TreeNode":
        child = TreeNode(child_value)
        self.children.append((edge_value, child))
        return child

class Tree:
    def __init__(self, root_value: Any):
        self.root = TreeNode(root_value)

    def __str__(self) -> str:
        lines: List[str] = []

        def walk(node: TreeNode, prefix: str, is_last: bool, incoming: Optional[Any]) -> None:
            connector = "└─" if is_last else "├─"
            if incoming is None:
                lines.append(f"{node.value!r}")
            else:
                lines.append(f"{prefix}{connector}[{incoming!r}]→ {node.value!r}")

            new_prefix = prefix + ("  " if is_last else "│ ")
            for i, (edge_val, child) in enumerate(node.children):
                last = i == len(node.children) - 1
                walk(child, new_prefix, last, edge_val)

        walk(self.root, "", True, None)
        return "\n".join(lines)

if __name__ == "__main__":
    t = Tree("root")
    a = t.root.add_child("A", "e1")
    t.root.add_child("B", "e2")
    a.add_child("A1", "e3")
    print(t)
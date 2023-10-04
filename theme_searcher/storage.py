from typing import TypeVar

from theme_searcher.models import Theme
from theme_searcher.utils import phrase_unify

SelfTreeNode = TypeVar("SelfTreeNode", bound="TreeNode")


class TreeNode:
    key: frozenset
    themes: set[Theme]
    children: set[SelfTreeNode]

    def __init__(self, phrase: str, theme: Theme | None = None):
        self.key = phrase_unify(phrase)
        self.themes = set()
        if theme is not None:
            self.themes.add(theme)
        self.children = set()

    def add_theme(self, themes: set[Theme]):
        self.themes.update(themes)

    def add_child(self, node: SelfTreeNode):
        self.children.add(node)

    def __str__(self):
        return (f"key={self.key}; "
                f"themes={{{', '.join(str(x) for x in self.themes)}}}; "
                f"children={{{', '.join(str(x) for x in self.children)}}}")


class PhraseTree:
    """
    Дерево фраз
    От меньшего к большему:
    '' -> '' -> ''
    """
    _root: TreeNode

    def __init__(self):
        self._root = TreeNode('')

    def _insert_node(self, node: TreeNode, root: TreeNode):
        # синхронная функция, потому что только расчеты
        if not root.children:
            root.children.add(node)
            return
        for child in root.children:
            if child.key == node.key:
                child.add_theme(node.themes)
                return
            if node.key.issubset(child.key):
                root.children.add(node)
                node.children.add(child)
                root.children.remove(child)
                return
            if child.key.issubset(node.key):
                self._insert_node(node, child)
                return
        root.children.add(node)

    def _search_nodes(self, search_key: frozenset, result: set[Theme], done_nodes: set[TreeNode], root: TreeNode):
        # синхронная функция, потому что только расчеты
        for child in root.children:
            if child in done_nodes:
                continue
            if child.key.issubset(search_key):
                result.update(child.themes)
                done_nodes.add(child)
                self._search_nodes(search_key, result, done_nodes, child)

    async def add_theme(self, theme: Theme):
        for phrase in theme.phrases:
            self._insert_node(TreeNode(phrase, theme), self._root)

    async def search(self, phrase: str) -> set[Theme] | None:
        result = set()
        done_nodes = set()
        search_key = phrase_unify(phrase)
        self._search_nodes(search_key, result, done_nodes, self._root)
        return result

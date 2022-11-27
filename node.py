def new_node(name):
    """Create a new node object."""
    return dict(name=name, children=[])


def append_node(node, new_node):
    """Append a node or leaf to a node."""
    assert isinstance(node, dict) and "children" in node
    node["children"].append(new_node)


def new_leaf(name, **kwargs):
    """Create a new leaf object."""
    return dict(name=name, value=kwargs)

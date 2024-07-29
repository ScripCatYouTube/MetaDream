from nodes.node import Node

def add_nodes(message_controller, node: Node) -> None:
    response = {
        'response': 'add_nodes',
        'nodes': node.get_source()
    }

    message_controller.add_message(response)


def delete_node(message_controller, node: (Node, str)): # in 'node' type Node or string(hash id)
    hash_id = 'hash'

    if isinstance(node, Node):
        hash_id = node.id

    elif isinstance(node, str):
        hash_id = node

    else:
        raise TypeError('node isn\'t type Node or string')

    response = {
        'response': 'delete_node',
        'id': hash_id
    }

    message_controller.add_message(response)


def change_data_node


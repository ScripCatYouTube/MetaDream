from nodes.node import Node

def add_nodes(message_controller, node: Node) -> None:
    message_controller.add_message({
        'response': 'add_nodes',
        'nodes': node.get_source()
    })


def delete_node(message_controller, node: (Node, str)): # in 'node' type Node or string(hash id)
    hash_id = 'hash'

    if isinstance(node, Node):
        hash_id = node.id

    elif isinstance(node, str):
        hash_id = node

    else:
        raise TypeError('node isn\'t type Node or string')

    message_controller.add_message({
        'response': 'delete_node',
        'id': hash_id
    })


def change_data_node(message_controller, node: Node, data: (Node, dict), id_hash: (Node, str) = None): # in 'data' type Node(change data from this node to 'node') or dict
    data_send = {}
    _id_hash = None

    if id_hash == None: pass

    elif isinstance(id_hash, Node):
        _id_hash = Node.id

    elif isinstance(id_hash, str):
        _id_hash = id_hash


    if isinstance(data, Node):
        data_send = node._get_source()

    elif isinstance(data, dict):
        data_send = node

    else:
        raise TypeError('node isn\'t type Node or dict')


    if _id_hash == None:
        _id_hash = data_send['id']


    message_controller.add_message({
        'response': 'change_node',
        'id': _id_hash,
        node:
            {
                'data': data_send
            }

    })





from nodes.node import Node

def add_nodes(message_controller, node: Node) -> None:
    response = node.get_source()

    message_controller.add_message(response)
import logging
import time
from threading import Thread
from nodes.node import Node, broadcast_message
from nodes.message import Message

committee_addr_list = [
    "127.0.0.1:4001",
    "127.0.0.1:4002",
    "127.0.0.1:4003",
    "127.0.0.1:4004",
    "127.0.0.1:4005",
    "127.0.0.1:4006",
    "127.0.0.1:4007",
    "127.0.0.1:4008",
    "127.0.0.1:4009",
    "127.0.0.1:4010",
    "127.0.0.1:4011",
    "127.0.0.1:4012",
    "127.0.0.1:4013",
    "127.0.0.1:4014",
    "127.0.0.1:4015",
]


def generate_nodes(num) -> []:
    committee_list = []
    for i in range(num):
        committee_list.append(Node(committee_addr_list[i], committee_addr_list[:num]))
    return committee_list


def start(node_num: int):
    print("n = {}".format(node_num))
    if node_num > len(committee_addr_list):
        logging.error("too much nodes")
        return
    if node_num < 5:
        print(committee_addr_list[:node_num])
    else:
        print("committee: [{} ~ {}]".format(committee_addr_list[0], committee_addr_list[node_num - 1]))

    # 创建委员会
    committee_list = generate_nodes(node_num)
    for _node in committee_list:
        Thread(target=_node.start_server, daemon=True).start()

    time.sleep(2)

    for _node in committee_list:
        while not _node.isRunning:
            pass
    print("================ All nodes are online now ==================")

    thread_list = []
    for node in committee_list:
        thread_list.append(
            Thread(target=broadcast_message, args=(node.peer_addr_list, Message("node", "node", {"a": 123})),
                   daemon=True))
    for thread in thread_list:
        thread.start()

    for _node in committee_list:
        _node.stop_server()
    print("================ All nodes are shutdown now =================")


if __name__ == '__main__':
    start(15)

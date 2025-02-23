from chs import CHS
from node_client import NodeClient
from ui import UserInterface
from exo_cluster import EXOCluster

def main():
    # Initialize the components
    chs = CHS()
    node_client = NodeClient(chs)
    exo_cluster = EXOCluster()
    ui = UserInterface(chs)

    # Start the user interface
    ui.start()

if __name__ == "__main__":
    main()

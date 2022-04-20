import torch
from torch_geometric.data import Data

edge_index = torch.tensor([[0, 1, 1, 2],
                           [1, 0, 2, 1]])

x = torch.tensor([[-1], [0], [1]], dtype=torch.float)

data = Data(x=x, edge_index=edge_index)

# printing data object.
print(f"graph keys: {data.keys}")
print(f"node attributes: \n {data['x']}")


print(f"graph keys and itens:") 
for key, item in data:
    print(f"{key}: {item}")


print(f"number of graph nodes : {data.num_nodes}")
print(f"number of graph edges : {data.num_edges}")
print(f"number of features in each node: {data.num_node_features}")
print(f"does the graph have isolated nodes: {data.has_isolated_nodes()}")
print(f"does the graph have self-loops : {data.has_self_loops()}")
print(f"is the graph directed: {data.is_directed()}")

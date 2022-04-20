from torch_geometric.datasets import TUDataset

dataset = TUDataset(root='/tmp/ENZYMES', name='ENZYMES')
print(f"ENZYMES dataset: ")
print(f"-----------------------------------------")
print(f"Number graphs in datasets: ", len(dataset))
print(f"graphs in datasets: ", len(dataset))

import numpy as np
def path_finder(area):
    rounds = np.asarray([list(round) for round in area.split('\n')], dtype=int)
    print(rounds)

        

a = "\n".join([
  "010",
  "101",
  "010"
])

path_finder(a)
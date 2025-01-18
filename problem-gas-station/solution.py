def checkGasStations(gas, cost):
  totalGas = sum(gas)
  totalCost = sum(cost)

  if totalGas < totalCost:
    return -1

  # reset tank
  tank = 0
  start = 0

  for i in range(len(gas)):
    tank += gas[i] - cost[i]
    
    if tank < 0:
      tank = 0
      start += 1

  return start

if __name__ == '__main__':
  gas = [1, 2, 3, 4, 5]
  cost = [3, 4, 5, 1, 2]
  print(checkGasStations(gas, cost))
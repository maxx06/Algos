#ACSL2020-2021_Senior3_Contest3
#March 2021
#Max Xiong


import numpy as np

originalLocation = (0, 0)
traveledLocations = [(0, 0)]

xcoords = [0]
ycoords = [0]

def turnIntoArrays(arrays):
  for strings in arrays:
    y = arrays.index(strings)
    u = []
    u.extend(strings.split())
    print(u)
    arrays[y] = u
  return arrays

def getDimensions(dim):
  dimensions = dim.split()
  row = int(dimensions[0])
  column = int(dimensions[1])
  return row, column

def separateIntoMatrices(dim, arrays):
  arrays = turnIntoArrays(arrays)
  print(arrays)
  row, column = getDimensions(dim)

  matrices = []
  for arr in arrays:
    arr = np.array(arr)
    arr = arr.reshape(row, column)
    matrices.append(arr)
  print(arrays)
  print(matrices)

  return matrices

def findSumOfPath(matrices, xcoords, ycoords):
  locations = []
  numsToSum = []
  sum = 0

  for i, j in zip(ycoords, xcoords):
    locations = []
    for matrix in matrices:
      pad = np.pad(matrix, [(0, 2), (0, 2)], mode='constant', constant_values=0)
      locations.append(pad[i][j])
    numsToSum.append(min(locations))
  print(numsToSum)
  for nums in numsToSum:
    sum += int(nums)
  
  print(sum)

  return sum
    

def largestUniqueValue(list):
  uniqueValuesList = []
  for i in list:
    if list.count(i) == 1:
      uniqueValuesList.append(i)

  print(uniqueValuesList)
  largestValue = max(uniqueValuesList)

  print(largestValue)

  return largestValue

def changeCoords(array, location):
  variable = array[location]
  (ycoord, xcoord) = variable

  traveledLocations.append(variable)

  xcoords.append(xcoord)
  ycoords.append(ycoord)
  print(traveledLocations)
  return ycoord, xcoord

def findNearbyNumbers(matrices, x, y, row, col):
  nearbyNumbers = []
  coords = []
  for matrix in matrices:
    pad1 = np.pad(matrix, [(0, 2), (0, 2)], mode='constant', constant_values=0)
    print(pad1)

    leftTop = pad1[y-1][x-1]
    top = pad1[y-1][x]
    rightTop = pad1[y-1][x+1]
    right = pad1[y][x+1]
    rightBottom = pad1[y+1][x+1]
    bottom = pad1[y+1][x]
    bottomLeft = pad1[y+1][x-1]
    left = pad1[y][x-1]
    
    #pls dont look at this part
    if y == 0 and x == 0:
      nearbyNumbers.extend((bottom, rightBottom, right))
      coords.extend(((y+1, x), (y+1, x+1), (y, x+1)))
    elif y == 0 and x == col:
      nearbyNumbers.extend((bottom, left, bottomLeft))
      coords.extend(((y+1, x), (y, x-1), (y+1, x-1)))
    elif y == row and x == col:
      nearbyNumbers.extend((top, left, leftTop))
      coords.extend(((y-1, x), (y, x-1), (y-1, x-1)))
    elif y == row and x == 0:
      nearbyNumbers.extend((top, right, rightTop))
      coords.extend(((y-1, x), (y, x+1), (y-1, x+1)))
    elif y == 0:
      nearbyNumbers.extend((bottom, rightBottom, right, bottomLeft, left))
      coords.extend(((y+1, x), (y+1, x+1), (y, x+1), (y+1, x-1), (y, x-1)))
    elif x == 0:
      nearbyNumbers.extend((bottom, right, top, rightTop, rightBottom))
      coords.extend(((y+1, x), (y, x+1), (y-1, x), (y-1, x+1), y+1, x+1))
    elif x == col:
      nearbyNumbers.extend((left, bottomLeft, bottom, top, leftTop))
      coords.extend(((y, x-1), (y+1, x-1), (y+1, x), (y-1, x), (y-1, x-1)))
    elif y == row:
      nearbyNumbers.extend((left, right, top, leftTop, rightTop))
      coords.extend(((y, x-1), (y, x+1), (y-1, x), (y-1, x-1), (y-1, x+1)))
    else:
      nearbyNumbers.extend((leftTop, top, rightTop, right, rightBottom, bottom, bottomLeft, left))
      coords.extend(((y-1, x-1), (y-1, x), (y-1, x+1), (y, x+1), (y+1, x+1), (y+1, x), (y+1, x-1), (y, x-1)))

  print(nearbyNumbers)
  num = largestUniqueValue(nearbyNumbers)
  location = nearbyNumbers.index(num)
  ycoord, xcoord = changeCoords(coords, location)
  print(location)
  print(coords)
  
  return ycoord, xcoord

def sumOfMinAlongPath(dim, arrays):
  matrices = separateIntoMatrices(dim, arrays)
  row, column = getDimensions(dim)
  xcoord = 0
  ycoord = 0
  
  currentLocation = (0, 0)
  while traveledLocations.count(currentLocation) <= 1:
    
    ycoord, xcoord = findNearbyNumbers(matrices, xcoord, ycoord, row, column)
    currentLocation = (ycoord, xcoord)
    
    if traveledLocations.count(currentLocation) > 1:
        xcoords.pop(-1)
        ycoords.pop(-1)

  print(ycoords, xcoords)

  print(ycoords, xcoords)
  
  sum = findSumOfPath(matrices, xcoords, ycoords)

  return sum
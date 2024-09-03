def printOddOccurences(array):
  odd = 0
  
  for element in array:
    
    odd = odd ^ element
    
  return odd

if __name__=='__main__':
  myArray = [3, 4, 1, 2, 5, 6, 5, 8]
  print(printOddOccurences(myArray))
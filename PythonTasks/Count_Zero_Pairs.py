def count_zero_pairs(numbers):
    
  n = len(numbers)
  
  for i in range(0, n):
      for j in range(i + 1, n):
          x = numbers[i]
          y = numbers[j]
        
          if x + y == 0:
            print(x, y)
  return "Pairs counted!"
                

print(count_zero_pairs([2, -2, 5, -5, 20, -20, 0, 10]))
        
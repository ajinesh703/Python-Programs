nested_map = {
  'fruit': {'apple': 5, 'banana': 10, 'mango': 12},
  'vegetable': {'aalu': 12, 'pyaj': 2, 'kathal': 2
    }
    
  
}

print("Number of kathals:", nested_map['vegetable']['kathal'])

nested_map['fruit']['cherry'] = 8
nested_map['vegetable']['bhindi'] = 10

print(nested_map)

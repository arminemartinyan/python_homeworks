# def make_unique_array(array):
#   unique_array = []
#   for num in array:
#     if num not in unique_array:
#       unique_array.append(num)
#   return unique_array


def sec_min(list):
  sec_min = 0

  #unique_list = make_unique_array(list)
  unique_list = []
  for num in list:
   if num not in unique_list:
    unique_list.append(num)

  ordered_list=[]

  while len(unique_list) > 0:
    unum = unique_list[0]
    ref = unum
    for member in unique_list:
      if member > ref:
        ref = member
    ordered_list.append(ref)
    unique_list.remove(ref)
    

  sec_min = ordered_list[len(ordered_list)-2]
  return sec_min

list = [5, 2, 1, 5, 2, 6, 4]

print(sec_min(list))
import numpy as np

def calculate(list):
  if len(list) == 9:
    np_list = np.array([
      [x for x in list[:3]],
      [x for x in list[3:6]],
      [x for x in list[6:]]
    ])
  else: 
    raise ValueError("List must contain nine numbers.")

# compute the numbers!
  col_mean = np.mean(np_list, axis=0).tolist()
  row_mean = np.mean(np_list, axis=1).tolist()
  mean = np.mean(np_list).tolist()

  col_var = np.var(np_list, axis=0).tolist()
  row_var = np.var(np_list, axis=1).tolist()  
  var = np.var(np_list).tolist()

  col_std = np.std(np_list, axis=0).tolist()
  row_std = np.std(np_list, axis=1).tolist()
  std = np.std(np_list).tolist()

  col_max = np.max(np_list, axis=0).tolist()
  row_max = np.max(np_list, axis=1).tolist()
  max = np.max(np_list).tolist()

  col_min = np.min(np_list, axis=0).tolist()
  row_min = np.min(np_list, axis=1).tolist()
  min = np.min(np_list).tolist()

  col_sum = np.sum(np_list, axis=0).tolist()
  row_sum = np.sum(np_list, axis=1).tolist()
  sum = np.sum(np_list).tolist()

  calculations = {
    'mean': [col_mean, row_mean, mean],
    'variance': [col_var, row_var, var],
    'standard deviation': [col_std, row_std, std],
    'max': [col_max, row_max, max],
    'min': [col_min, row_min, min],
    'sum': [col_sum, row_sum, sum]
  }


  return calculations
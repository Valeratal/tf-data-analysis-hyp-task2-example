import pandas as pd
import numpy as np
from scipy.stats import ttest_ind

chat_id = 252926140 # your chat ID, don't change the variable name

def solution(x: np.array, y: np.array) -> bool:
  alpha = 0.09
  t_stat, p_val = ttest_ind(x, y)
  return p_val < alpha

import pandas as pd
import numpy as np
from scipy.stats import ks_2samp

chat_id = 252926140 # your chat ID, don't change the variable name

def solution(x: np.array, y: np.array) -> bool:
  _, p_value = ks_2samp(x, y)
  significance_level = 0.09
  return p_value < significance_level

import numpy as np
from sklearn.metrics import fbeta_score

# Is this mathematically sound?
# Code adapted from: https://www.kaggle.com/c/planet-understanding-the-amazon-from-space/discussion/32475
def f2_optimized_thresholds(y_true, y_pred, verbose=True, resolution=100):
  def score_for_threshold(x):
    #p2 = np.zeros_like(p)
    p2 = (y_pred > x).astype(np.int)
    score = fbeta_score(y_true, p2, beta=2, average='samples')
    return score

  x = [0.5]*17
  for i in range(17):
    best_i2 = 0
    best_score = 0
    for i2 in range(resolution):
      i2 /= float(resolution)
      x[i] = i2
      score = score_for_threshold(x)
      if score > best_score:
        best_i2 = i2
        best_score = score
    x[i] = best_i2
    if verbose:
      print('label:{} threshold:{} score:{}'.format(i, best_i2, best_score))
  return x
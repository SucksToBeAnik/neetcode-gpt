import numpy as np
from numpy.typing import NDArray


class Solution:

    def softmax(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array of logits
        # Hint: subtract max(z) for numerical stability before computing exp
        # return np.round(your_answer, 4)
        max_of_z = np.max(z)
        exp_z = np.exp(z - max_of_z)
        sum_exp = np.sum(exp_z)

        def convert(x):
            return np.exp(x - max_of_z) / sum_exp
        
        vfunc = np.vectorize(convert)
        return np.round(vfunc(z), 4)
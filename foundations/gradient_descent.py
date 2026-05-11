class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        # Objective function: f(x) = x^2
        # Derivative:         f'(x) = 2x
        # Update rule:        x = x - learning_rate * f'(x)
        res = init
        for i in range(iterations):
            res = res - learning_rate * 2*res
        # Round final answer to 5 decimal places
        return round(res,5)

sol = Solution()
print(sol.get_minimizer(10,0.01,5))
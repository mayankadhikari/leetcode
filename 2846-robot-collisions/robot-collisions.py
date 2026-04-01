class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)

        indices = list(range(n))

        indices.sort(key=lambda i: positions[i])

        stack = []

        for idx in indices:
            if directions[idx] == 'R':
                stack.append(idx)
            else:
                while stack and healths[idx] > 0:
                    top_idx = stack[-1]

                    if healths[top_idx] < healths[idx]:
                        stack.pop()
                        healths[idx] -= 1
                        healths[top_idx] = 0

                    elif healths[top_idx] == healths[idx]:
                        stack.pop()
                        healths[top_idx] = 0
                        healths[idx] = 0

                    else:
                        healths[top_idx] -= 1
                        healths[idx] = 0

        result = []

        for health in healths:
            if health > 0:
                result.append(health)

        return result
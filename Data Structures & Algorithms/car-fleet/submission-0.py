class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = list(zip(position, speed))
        pairs = sorted(pairs, key=lambda x: x[0])
        res = 0

        while len(pairs) >= 2:
            p_1, s_1 = pairs.pop()
            p_2, s_2 = pairs.pop()

            time_1 = (target - p_1) / s_1
            time_2 = (target - p_2) / s_2
            # если предыдущий догонит
            # (его скорость - максимальная из тех, кто сзади)
            if time_1 >= time_2:
                fleet = p_1, s_1
                pairs.append(fleet)
            else: # если предыдущий не догонит
                res += 1
                pairs.append((p_2, s_2))
            
        res += 1
        return res
            
                





        

            




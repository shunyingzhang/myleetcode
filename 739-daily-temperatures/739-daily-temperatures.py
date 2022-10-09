class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        Res = [0] * len(temperatures)
        TempDay = []
        for i, t in enumerate(temperatures):
            while TempDay and t >  TempDay[-1][0]:
                temp, day = TempDay.pop()
                Res[day] = i - day
            TempDay.append((t, i))
        return Res
        
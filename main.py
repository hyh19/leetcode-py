from typing import List


class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        clips.sort(key=lambda clip: (clip[0], -clip[1]))
        count = 0
        cover_end = 0
        i, n = 0, len(clips)
        # 当 clips[i] 与 [0, cover_end] 重叠（相交或被覆盖）时
        while i < n and clips[i][0] <= cover_end:
            # 记录与 [0, cover_end] 重叠的所有区间中最大的 end
            max_end = 0
            while i < n and clips[i][0] <= cover_end:
                max_end = max(max_end, clips[i][1])
                i += 1
            count += 1
            cover_end = max_end
            if cover_end >= time:
                return count
        return -1

#더 맵게
#섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
from heapq import heappush, heappop
def solution(scoville, K):
    answer = 0
    
    heap = []
    for i in scoville:
        heappush(heap, i)
    
    while(heap[0] < K):
        if(len(heap)<2):
            return -1
        heappush(heap, heappop(heap)+heappop(heap)*2)
        answer+=1
    
    return answer
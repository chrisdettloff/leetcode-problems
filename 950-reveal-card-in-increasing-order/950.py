class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        n = len(deck)
        queue = deque(range(n))
        result = [None] * n

        for i in range(n):
            result[queue.popleft()] = deck[i]
            if queue:
                queue.append(queue.popleft())
        return result
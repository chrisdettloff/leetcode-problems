class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Count the occurrences of each task
        count = Counter(tasks)

        # Create a max heap storing the negative task counts for prioritization
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque()

        while maxHeap or q:
            time += 1

            if maxHeap:
                # Take the next task from the heap (highest remaining count)
                cnt = 1 + heapq.heappop(maxHeap)

                # If the task still has occurrences left, add it to the cooldown queue
                if cnt:
                    q.append([cnt, time + n])  # Store remaining count and cooldown end time

            # If the front of the queue has a task ready to run
            if q and q[0][1] == time:
                # Put the task back on the heap for future scheduling
                heapq.heappush(maxHeap, q.popleft()[0])

        return time

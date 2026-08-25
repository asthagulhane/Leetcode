class Solution:

    def openLock(self, deadends: list[str], target: str) -> int:
        # Use a single set to track both invalid paths and visited states
        vis = set(deadends)
        if "0000" in vis:
            return -1

        # Queue stores tuples of (current_lock_state, current_turns)
        q = deque([("0000", 0)])
        vis.add("0000")

        while q:
            curr, turns = q.popleft()
            if curr == target:
                return turns

            # Generate all 8 possible next combinations (4 wheels * 2 directions)
            for i in range(4):
                for d in (-1, 1):
                    nxt = (
                        curr[:i] + str((int(curr[i]) + d) % 10) + curr[i + 1 :]
                    )
                    if nxt not in vis:
                        vis.add(nxt)
                        q.append((nxt, turns + 1))

        return -1

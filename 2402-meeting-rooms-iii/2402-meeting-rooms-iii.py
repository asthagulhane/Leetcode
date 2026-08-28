class Solution:

    def mostBooked(self, n: int, meetings: list[list[int]]) -> int:
        # Sort meetings by their original start time
        meetings.sort(key=lambda x: x)

        # Min-heap for available room IDs
        unused_rooms = list(range(n))
        heapq.heapify(unused_rooms)

        # Min-heap for ongoing meetings: stores tuples of (end_time, room_id)
        ongoing_meetings = []

        # Track number of meetings hosted by each room
        room_count = [0] * n

        for start, end in meetings:
            # 1. Free up all rooms whose meetings have finished by the current start time
            while ongoing_meetings and ongoing_meetings[0][0] <= start:
                _, room = heapq.heappop(ongoing_meetings)
                heapq.heappush(unused_rooms, room)

            # 2. If a room is free, assign it immediately
            if unused_rooms:
                room = heapq.heappop(unused_rooms)
                heapq.heappush(ongoing_meetings, (end, room))
            # 3. If all rooms are full, wait for the earliest meeting to finish
            else:
                earliest_end, room = heapq.heappop(ongoing_meetings)
                new_end = earliest_end + (end - start)  # Maintain original duration
                heapq.heappush(ongoing_meetings, (new_end, room))

            room_count[room] += 1

        # Return the room with the maximum meetings (index naturally handles the lowest-index tie-breaker)
        return room_count.index(max(room_count))

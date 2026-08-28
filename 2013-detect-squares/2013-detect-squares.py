class DetectSquares:

    def __init__(self):
        # Maps (x, y) tuple to its frequency count
        self.points_count = Counter()
        # Groups y-coordinates by their x-coordinate to quickly find vertical matches
        self.x_to_ys = defaultdict(list)

    def add(self, point: list[int]) -> None:
        x, y = point
        self.points_count[(x, y)] += 1
        self.x_to_ys[x].append(y)

    def count(self, point: list[int]) -> int:
        px, py = point
        total_squares = 0

        # Iterate through all points sharing the same x-coordinate
        for y in self.x_to_ys[px]:
            if y == py:
                continue  # Skip the query point itself (requires positive area)

            # Side length of the square
            side = abs(py - y)

            # Check for squares extending to the right (px + side)
            x_right = px + side
            total_squares += (
                self.points_count[(x_right, py)] * self.points_count[(x_right, y)]
            )

            # Check for squares extending to the left (px - side)
            x_left = px - side
            total_squares += (
                self.points_count[(x_left, py)] * self.points_count[(x_left, y)]
            )

        return total_squares

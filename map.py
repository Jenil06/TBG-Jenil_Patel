class Map:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.tiles = [['O' for _ in range(width)] for _ in range(height)]
        self.start_position = (0, 0)
        self.end_position = (width - 1, height - 1)

    def print_map(self, player_position):
        for i, row in enumerate(self.tiles):
            for j, tile in enumerate(row):
                if (i, j) == player_position:
                    print("P", end=" ")
                else:
                    print(tile, end=" ")
            print()
            

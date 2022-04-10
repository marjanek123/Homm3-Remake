
class Pathfinding():
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, position=None, cost=0, arrow=0):
        self.parent = parent
        self.position = position
        self.cost = cost
        self.arrow = arrow

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position


def astar(maze, start, end):
    """Returns a list of tuples as a path from the given start to the given end in the given maze"""

    # Create start and end node
    start_node = Pathfinding(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Pathfinding(None, end)
    end_node.g = end_node.h = end_node.f = 0

    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Add the start node
    open_list.append(start_node)

    # Loop until you find the end
    while len(open_list) > 0:

        # Get the current node
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)

        # Found the goal
        if current_node == end_node:
            path = []
            current_node.arrow = 0
            current = current_node
            cost = 0
            while current is not None:
                path.append((current.position, current.cost, current.arrow))
                # cost += current.cost
                current = current.parent
            # path[1] = end_node
            return path[:-1]  # Return reversed path

        # Generate children
        children = []
        # Adjacent squares
        for new_position in [(0, -1, 100, 5), (0, 1, 100, 1), (-1, 0, 100, 8), (1, 0, 100, 3), (-1, -1, 144, 6), (-1, 1, 144, 9), (1, -1, 144, 4), (1, 1, 144, 2)]:

            # Get node position
            node_position = (
                current_node.position[0] +
                new_position[0],
                current_node.position[1] +
                new_position[1])

            # Make sure within range
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) - 1) or node_position[1] < 0:
                continue

            # Make sure walkable terrain
            if maze[node_position[0]][node_position[1]] != 0:
                continue

            # Create new node
            new_node = Pathfinding(
                current_node, node_position, new_position[2], new_position[3])

            # Append
            children.append(new_node)

        # Loop through children
        for child in children:

            # Child is on the closed list
            for closed_child in closed_list:
                if child == closed_child:
                    continue

            # Create the f, g, and h values
            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) **
                       2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            # Child is already in the open list
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            # Add the child to the open list
            open_list.append(child)


# def main():

#     maze = registry.global_controllers.assets_controller.mapk

#     start = (0, 0)
#     end = (9, 8)

#     path = astar(maze, start, end)
#     # print(path)
#     skrr(path, maze)


# def skrr(path, maze):
#     for w in path:
#         maze[w[0]][w[1]] = 5
#     # print(maze)
#     return maze


# main()

class BlockWorld:
    def __init__(self, initial_state):
        self.state = initial_state

    def move(self, block, source, destination):
        if block in self.state[source]:
            self.state[source].remove(block)
            self.state[destination].append(block)
            return True
        else:
            return False

    def stack(self, block1, block2):
        for position, stack in enumerate(self.state):
            if block1 in stack and (block2 in stack or not stack):
                self.state[position].remove(block1)
                self.state[position].append(block2)
                return True
        return False

    def unstack(self, block1, block2):
        for position, stack in enumerate(self.state):
            if block1 in stack and block2 in stack and stack.index(block1) == len(stack) - 1:
                self.state[position].remove(block1)
                self.state.append([block1])
                return True
        return False


def depth_limited_search(state, goal, actions, depth_limit, path=None):
    if path is None:
        path = []
    if state == goal:
        return path
    elif depth_limit == 0:
        return None
    else:
        for action in actions:
            child_state = apply_action(state, action)
            if child_state is not None:
                result = depth_limited_search(child_state, goal, actions, depth_limit - 1, path + [action])
                if result is not None:
                    return result
        return None

def apply_action(state, action):
    # Assuming state is an instance of BlockWorld
    if action[0] == 'move':
        return state.move(action[1], action[2], action[3])
    elif action[0] == 'stack':
        return state.stack(action[1], action[2])
    elif action[0] == 'unstack':
        return state.unstack(action[1], action[2])
    else:
        return None

# Example usage
initial_state = [['A'], ['B'], ['C', 'D']]
goal_state = [['A', 'B'], ['C'], ['D']]
actions = [('move', 'C', 2, 0), ('stack', 'A', 'B'), ('unstack', 'A', 'B')]
depth_limit = 5

block_world = BlockWorld(initial_state)
solution = depth_limited_search(block_world, goal_state, actions, depth_limit)

if solution is not None:
    print("Solution found:", solution)
else:
    print("No solution within depth limit")

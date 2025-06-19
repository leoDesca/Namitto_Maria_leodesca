import numpy as np
import random

# Define the environment
position = 5  # number of positions (0 to 4)
actions = 2   # number of possible actions: 0 (left), 1 (right)

# Initialize the Q-table with 5 positions and 2 actions
Q = np.zeros((position, actions))

# Define the parameters
episodes = 1000       # Increased episodes for better learning
learning_rate = 0.8   # learning rate
gamma = 0.9           # discount factor
epsilon = 0.3         # exploration rate

# Car-related variables
car_positions = []
car_spawn_prob = 0.3  # Probability of a new car spawning

# Training loop
for episode in range(episodes):
    # Reset environment for each episode
    state = 0  # Start at leftmost position
    car_positions = []  # Clear existing cars
    done = False
    
    while not done:
        # Epsilon-greedy action selection
        if random.uniform(0, 1) < epsilon:
            action = random.randint(0, actions - 1)  # Explore
        else:
            action = np.argmax(Q[state])  # Exploit
        
        # Move agent
        if action == 0:  # Move left
            next_state = max(0, state - 1)
        else:  # Move right
            next_state = min(position - 1, state + 1)
        
        # Update car positions (move cars left)
        car_positions = [pos-1 for pos in car_positions if pos-1 >= 0]
        
        # Spawn new car with some probability
        if random.random() < car_spawn_prob:
            car_positions.append(position - 1)  # Spawn at rightmost position
        
        # Check for collision
        collision = next_state in car_positions
        
        # Reward structure
        if next_state == position - 1:  # Reached goal
            reward = 10
            done = True
        elif collision:  # Hit by car
            reward = -10
            done = True
        else:  # Normal move
            reward = -1
        
        # Q-learning update
        Q[state, action] = Q[state, action] + learning_rate * (
            reward + gamma * np.max(Q[next_state]) - Q[state, action]
        )
        
        # Transition to next state
        state = next_state

# Test the trained agent
print("\nAgent crossing the road:")
state = 0  # Start position
car_positions = []  # Reset cars
steps = 0
success = False

print(" [A]=Agent, [C]=Car")
while not success and steps < 20:  # Limit steps to prevent infinite loops
    # Visualize current state
    road = ['_'] * position
    road[state] = 'A'  # Agent position
    for car in car_positions:
        if 0 <= car < position:
            road[car] = 'C'  # Car position
    print(f"Step {steps}: |{'|'.join(road)}|")
    
    # Move cars
    car_positions = [pos-1 for pos in car_positions if pos-1 >= 0]
    
    # Spawn new car
    if random.random() < car_spawn_prob:
        car_positions.append(position - 1)
    
    # Agent chooses action
    action = np.argmax(Q[state])
    if action == 0:  # Move left
        next_state = max(0, state - 1)
    else:  # Move right
        next_state = min(position - 1, state + 1)
    
    # Check for success or collision
    if next_state == position - 1:
        print("SUCCESS: Agent crossed the road!")
        success = True
    elif next_state in car_positions:
        print("FAIL: Agent hit by car!")
        break
    
    # Update state
    state = next_state
    steps += 1

# Final Q-table
print("\nFinal Q-table:")
print(Q)
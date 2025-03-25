import pygame 
import sys 
from itertools import permutations 
# Initialize Pygame 
pygame.init() 
# Screen dimensions 
WIDTH, HEIGHT = 600, 400 
screen = pygame.display.set_mode((WIDTH, HEIGHT)) 
pygame.display.set_caption("Brute Force Algorithm") 
# Colors 
WHITE = (255, 255, 255) 
BLACK = (0, 0, 0) 
RED = (255, 0, 0) 
GREEN = (0, 255, 0) 
BLUE = (0, 0, 255) 
# Graph representation 
graph = { 
'A': {'B': 2, 'C': 7}, 
'B': {'A': 4, 'C': 7, 'D': 5}, 
    'C': {'A': 4, 'B': 2, 'D': 5}, 
    'D': {'B': 2, 'C': 7} 
} 
 
# Update edge weights (example: update A-B to 5) 
graph['A']['B'] = 5 
graph['B']['A'] = 5 
 
# Node positions for visualization 
node_positions = { 
    'A': (100, 200), 
    'B': (300, 100), 
    'C': (300, 300), 
    'D': (500, 200) 
} 
 
# Brute Force Algorithm 
def brute_force_pathfinding(graph, start, end): 
    nodes = list(graph.keys()) 
    nodes.remove(start) 
    nodes.remove(end) 
    all_paths = permutations(nodes) 
 
    shortest_path = None 
    min_cost = float('inf') 
 
    for path in all_paths: 
        current_path = [start] + list(path) + [end] 
        current_cost = 0 
        for i in range(len(current_path) - 1): 
            current_cost += graph[current_path[i]][current_path[i + 1]] 
         
        if current_cost < min_cost: 
            min_cost = current_cost 
            shortest_path = current_path 
 
    return shortest_path, min_cost 
 
# Find the shortest path 
start, end = 'A', 'D' 
shortest_path, cost = brute_force_pathfinding(graph, start, end) 
print(f"Shortest Path: {shortest_path}, Cost: {cost}") 
 
# Pygame visualization 
def draw_graph(): 
    screen.fill(WHITE) 
    # Track labeled edges to avoid duplicates 
    labeled_edges = set() 
    # Draw all edges and add numbers 
    for node, edges in graph.items(): 
        for neighbor, weight in edges.items(): 
            # Skip if the edge has already been labeled 
            if (node, neighbor) in labeled_edges or (neighbor, node) in labeled_edges: 
                continue 
            # Draw the edge 
            pygame.draw.line(screen, BLACK, node_positions[node], node_positions[neighbor], 2) 
            # Calculate midpoint for the number 
            mid_point = ( 
                (node_positions[node][0] + node_positions[neighbor][0]) // 2, 
                (node_positions[node][1] + node_positions[neighbor][1]) // 2 
            ) 
            # Offset the number to avoid overlap 
            if node_positions[node][1] < node_positions[neighbor][1]: 
                # Edge goes downward, place number above 
                offset_x, offset_y = 0, -20 
            else: 
                # Edge goes upward, place number below 
                offset_x, offset_y = 0, 20 
            number_pos = (mid_point[0] + offset_x, mid_point[1] + offset_y) 
            # Draw the weight number 
            font = pygame.font.Font(None, 24) 
            text = font.render(str(weight), True, BLACK) 
            screen.blit(text, number_pos) 
            # Mark the edge as labeled 
            labeled_edges.add((node, neighbor)) 
    # Draw all nodes 
    for node, pos in node_positions.items(): 
        pygame.draw.circle(screen, GREEN, pos, 20) 
        font = pygame.font.Font(None, 36) 
        text = font.render(node, True, WHITE) 
        screen.blit(text, (pos[0] - 10, pos[1] - 10)) 
    # Highlight shortest path 
    for i in range(len(shortest_path) - 1): 
        pygame.draw.line(screen, RED, node_positions[shortest_path[i]], 
node_positions[shortest_path[i + 1]], 4) 
    pygame.display.flip() 
 
# Main loop 
running = True 
while running: 
for event in pygame.event.get(): 
if event.type == pygame.QUIT: 
running = False 
draw_graph() 
pygame.quit() 
sys.exit()
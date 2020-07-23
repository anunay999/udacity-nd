import heapq
import math

def eucld_norm_dist(a, b):
    return math.hypot(b[0] - a[0], b[1] - a[1])


def shortest_path(M, start, goal):
    frontier_node = [[0,start]]
    parent_node = dict()
    visited_node_costs = dict()
    shortest_path = list()
    parent_node[start] = None
    visited_node_costs[start] = 0
    current_node = None
    
    while len(frontier_node) > 0:
        current_node = heapq.heappop(frontier_node)[1]
        if current_node == goal:
            break
        for neighbor in M.roads[current_node]:
            estimated_cost = eucld_norm_dist(M.intersections[current_node], M.intersections[neighbor])
            estimated_cost += visited_node_costs[current_node] 
            if neighbor not in visited_node_costs or estimated_cost < visited_node_costs[neighbor]:
                heapq.heappush(frontier_node, [estimated_cost,neighbor])
                parent_node[neighbor] = current_node
                visited_node_costs[neighbor] = estimated_cost              
    
    current_node = goal
    #if current_node not in parent_node:
     #   return None
    while current_node != start:
        shortest_path.append(current_node)
        current_node = parent_node[current_node]
                
    shortest_path.append(start)
    shortest_path.reverse()
    return shortest_path

    
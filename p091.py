import math
import time
import matplotlib.pyplot as plt
import numpy as np

start = time.time()

grid_generator = lambda t: [(x, y) for x in range(0, t + 1) for y in range(0, t + 1)]
perp_line = lambda a, b, x, y: b * y == -a*x + a**2 + b**2   

def initial_plot(max_coor):
    '''
        Initial plot with coordinate limits
    '''
    plt.grid(True, linewidth=0.5, color='#000000', linestyle='-')
    plt.xticks(np.arange(0, max_coor + 1, 1))
    plt.yticks(np.arange(0, max_coor + 1, 1))
    plt.gca().set_aspect('equal', adjustable='box')

    return plt

def triangle_plot(points, max_triangle_coor):
    '''
        Plots triangle from points (e.g. [(0, 0), (1, 0), (1, 1)])
    '''
    x = np.array([point[0] for point in points])
    y = np.array([point[1] for point in points])

    plt.plot(x, y)
    plt.scatter(x, y)

    initial_plot(max_triangle_coor)

    return plt

def right_triangles_graph(right_triangles):

    max_subplots = math.ceil(math.sqrt(len(right_triangles))) ** 2
    nrows = ncols = int(math.sqrt(max_subplots))

    max_triangle_coor = max([max(triangle_coor) for triangle_coor in right_triangles])[0]

    for triangle_coor in right_triangles:
        plt.subplot(nrows, ncols, right_triangles.index(triangle_coor) + 1)
        triangle_plot(triangle_coor + [(0, 0)], max_triangle_coor)

    plt.show()

def main():

    O = (0, 0)
    right_triangles = []
    G_t = grid_generator(50)
    G_t.remove(O)

    K_x = [point for point in G_t if point[1] == 0]
    K_y = [point for point in G_t if point[0] == 0]
    K_r = [point for point in G_t if point not in K_x and point not in K_y]
    
    for P in G_t:
        for Q in G_t:
            if Q != P and Q[0] + Q[1] > P[0] and Q[0] + Q[1] > P[1] and perp_line(P[0], P[1], Q[0], Q[1]):
                right_triangles.append([O, P, Q])

    for point_y in K_y:
        for point_x in K_x:
            right_triangles.append([O, point_x, point_y])

    # graph = int(input('Thelei grafiki parastasi twn trigwnwn i oki? = '))
   
    # if graph: right_triangles_graph(right_triangles)
    
    print(time.time() - start)

    return len(right_triangles)


if __name__ == '__main__':

    a = main()
    print(a)
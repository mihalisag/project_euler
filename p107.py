import time
from math import inf

file = open('p107_network.txt','r')
graph = file.read()
graph = str(graph)
g = graph.split('\n')
graph_matrix = []


for i in g:
	graph_matrix.append((i.split(',')))

#print(graph_matrix)

def vertex_names(ng):

	vertex_list = []

	for subscript in range(1,ng+1):
		vertex_list.append('v'+str(subscript))

	return vertex_list



def edge_dict(graph_matrix):

	v_list = vertex_names(len(graph_matrix[0]))
	e_dict = {}

	for row in range(1,len(v_list)+1):
		for column in range(1,len(v_list)+1):

			cost = graph_matrix[row-1][column-1]

			if cost != '-':
				edge = ('v'+str(row),'v'+str(column))
				e_dict[edge] = cost

	return e_dict



def neighborhood_of_vertex(vertex):

	e_dict = edge_dict(graph_matrix)
	edges = e_dict.keys()
	n_set = set()

	for tuple in edges:
		if vertex in tuple:
			temp = list(tuple)
			temp.remove(vertex)
			neighbor = temp[0]
			n_set.add(neighbor)

	return n_set



def vertex_dict():

	v_list = vertex_names(len(graph_matrix[0]))
	e_dict = edge_dict(graph_matrix)
	v_dict = {}

	for vertex in v_list:
		v_dict[vertex] = set()

	edges = e_dict.keys()

	for tuple in edges:
		for vertex in tuple:
			v_dict[vertex].add(int(e_dict[tuple]))

	return v_dict



def min_cost_dict(vertex_dict):

	vertices = vertex_dict.keys()
	min_cost_dict = {}

	for vertex in vertices:
		min_cost_dict[vertex] = min(vertex_dict[vertex])

	return min_cost_dict

def key_with_min_value(dict):

	min_value = min(dict.values())

	for key in dict:
		if dict[key] == min_value:
			return key


def spanning_tree():

	tree = ['v1','v2']
	v_dict = vertex_dict()
	md = min_cost_dict(v_dict)
	not_list = vertex_names(len(graph_matrix[0]))
	start_len = len(not_list)
	vc_dict = {not_list[0]:0}

	for vertex in not_list[1:]:
		vc_dict[vertex] = inf

	tree_vertex = tree[0]

	if len(tree) < start_len:

		neigh_dict = {}
		n_vertices_list = []

		for vertex in tree:
			v = neighborhood_of_vertex(vertex)
			n_vertices_list.append(v)

		for neighborhood in n_vertices_list:
			minimum = inf
			for vertex in neighborhood:
				if md[vertex]<minimum:
					minimum = md[vertex]
					min_vertex = vertex

		tree.append(min_vertex
					)
		print(tree)

		# for vertex in n_vertices:
		# 	neigh_dict[vertex] = md[vertex]
		#
		# print(neigh_dict)

		tree_vertex = key_with_min_value(vc_dict)
		tree.append(tree_vertex)




	return vc_dict




if __name__ == '__main__':

	start = time.time()

	example = [['-', '16', '12', '21', '-', '-', '-'],
			   ['16', '-', '-', '17', '20', '-', '-'],
			   ['12', '-', '-', '28', '-', '31', '-'],
			   ['21', '17', '28', '-', '18', '19', '23'],
			   ['-', '20', '-', '18', '-', '-', '11'],
			   ['-', '-', '31', '19', '-', '-', '27'],
			   ['-', '-', '-', '23', '11', '27', '-']]

	graph_matrix = example
	e_dict = edge_dict(graph_matrix)
	v_dict = vertex_dict()
	md = min_cost_dict(v_dict)
	vc = spanning_tree()
	nv = neighborhood_of_vertex('v7')
	sm = key_with_min_value(md)

	print(md)
	print(sm)

	end = time.time()-start

	print(end,'s')


# να δω με τομη για την γειτονια
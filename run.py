#!/usr/bin/python

import sys
import os
import heapq
from PIL import Image


class DangerousMaze:

    def __init__(self, file):
        self.board = open(file, 'r').readlines()
        self.visited_nodes = []
        self.heap = []
        self.cost = 0
        self.start_coord = self.find_coord_of_symbol('S')
        self.current_node = {'coord': self.start_coord, 'path': ''}
        self.finish_coord = self.find_coord_of_symbol('G')
        self.traceback = []
        self.computed = False

    def __str__(self):
        self.compute()
        return "Total cost: {} HP".format(self.cost)

    def generate_image(self):
        self.compute()
        print("Generating image...")
        img_data = []
        for row in range(0, len(self.board) - 1):
            for column in range(0, len(self.board[0]) - 1):
                if (row, column) in self.traceback:
                    pixel = (155, 155, 155)
                elif self.board[row][column] == ' ':
                    pixel = (255, 255, 255)
                elif self.board[row][column] == 'm':
                    pixel = (255, 0, 0)
                elif self.board[row][column] == 'S':
                    pixel = (0, 255, 0)
                elif self.board[row][column] == 'G':
                    pixel = (0, 0, 255)
                else:
                    pixel = (0, 0, 0)
                img_data.append(pixel)

        img = Image.new('RGB', (len(self.board), len(self.board[0])))
        img.putdata(img_data)
        img.save('image.png')


    def find_coord_of_symbol(self, symbol):
        for rowIdx, row in enumerate(self.board):
            for columnIdx, column in enumerate(row):
                if column == symbol:
                    return rowIdx, columnIdx

    def compute(self):
        if self.computed:
            return
        self.compute_cost()
        self.compute_traceback()
        self.computed = True

    def compute_cost(self):
        print("Computing cost...")
        while self.current_node['coord'] != self.finish_coord:
            coords_to_check = [(self.current_node['coord'][0] + i[0], self.current_node['coord'][1] + i[1])
                               for i in [(-1, 0), (1, 0), (0, -1), (0, 1)]]
            d = [i['coord'] for i in self.visited_nodes]
            for coord in coords_to_check:
                if self.board[coord[0]][coord[1]] != '#' and coord not in d:
                    if self.board[coord[0]][coord[1]] == ' ' or self.board[coord[0]][coord[1]] == 'G':
                        added_cost = 1
                    else:
                        added_cost = 11
                    new_cost = self.cost + added_cost
                    c = dict((i[1]['coord'], i[0]) for i in self.heap)
                    v = dict((i[1]['coord'], i[1]['path']) for i in self.heap)
                    if coord in c:
                        old_cost = c[coord]
                        old_path = v[coord]
                        if old_cost >= new_cost:
                            self.heap.remove((old_cost, {'coord': coord, 'path': old_path}))
                            heapq.heappush(self.heap, (new_cost, {'coord': coord, 'path': self.current_node['coord']}))
                        else:
                            pass
                    else:
                        heapq.heappush(self.heap, (new_cost, {'coord': coord, 'path': self.current_node['coord']}))
            self.visited_nodes.append(self.current_node)
            next_node = heapq.heappop(self.heap)
            self.cost = next_node[0]
            self.current_node = next_node[1]

    def compute_traceback(self):
        trace = self.current_node['path']
        d = dict((i['coord'], i['path']) for i in self.visited_nodes)
        while trace != self.start_coord:
            self.traceback.append(trace)
            trace = d[trace]

if __name__ == "__main__":
    maze_location = "{}/{}".format(os.path.dirname(os.path.realpath(__file__)), sys.argv[1])
    maze = DangerousMaze(maze_location)
    print(maze)
    maze.generate_image()

#!/usr/bin/python

import sys
import os
import heapq
import time


class DangerousMaze:

    def __init__(self, file):
        t = time.time()
        print("Computing path...")

        self.board = self.parse_board(file)
        self.visitedNodes = []
        self.heap = []
        self.currentCost = 0
        self.currentNode = self.find_start_node()
        self.finishCoord = self.find_finish_coord()
        self.find_cost()

        print("Time elapsed: {} seconds".format(time.time() - t))
        print("Total cost: {}".format(self.currentCost))

        print("Generating image...")
        self.find_traceback()
        print(self.heap)

    def find_cost(self):
        while self.currentNode['coord'] != self.finishCoord:
            coords_to_check = [(self.currentNode['coord'][0] + i[0], self.currentNode['coord'][1] + i[1])
                               for i in [(-1, 0), (1, 0), (0, -1), (0, 1)]]

            d = [i['coord'] for i in self.visitedNodes]
            for coord in coords_to_check:
                if self.board[coord[0]][coord[1]] != '#' and coord not in d:
                    if self.board[coord[0]][coord[1]] == ' ' or self.board[coord[0]][coord[1]] == 'G':
                        addedCost = 1
                    else: # elif self.board[coord[0], coord[1]] == 'm':
                        addedCost = 11

                    newCost = self.currentCost + addedCost

                    h = dict((i[1]['coord'], i[0]) for i in self.heap)
                    v = dict((i[1]['coord'], i[1]['via-path']) for i in self.heap)
                    if coord in h:
                        oldCost = h[coord]
                        oldViaPath = v[coord]
                        if oldCost >= newCost:
                            self.heap.remove((oldCost, {'coord': coord,
                                                        'via-path': oldViaPath}))
                            heapq.heappush(self.heap, (newCost, {'coord': coord,
                                                                 'via-path': self.currentNode['coord']}))
                        else:
                            pass
                    else:
                        heapq.heappush(self.heap, (newCost, {'coord': coord,
                                                             'via-path': self.currentNode['coord']}))

            self.visitedNodes.append(self.currentNode)
            next_node = heapq.heappop(self.heap)
            self.currentCost = next_node[0]
            self.currentNode = next_node[1]

    def find_start_node(self):
        for rowIdx, row in enumerate(self.board):
            for columnIdx, column in enumerate(row):
                if column == 'S':
                    return {'coord': (rowIdx, columnIdx), 'via-path': ''}

    def find_finish_coord(self):
        for rowIdx, row in enumerate(self.board):
            for columnIdx, column in enumerate(row):
                if column == 'G':
                    return (rowIdx, columnIdx)

    def parse_board(self, file):
        return open(file, 'r').readlines()




if __name__ == "__main__":
    file = "{}/{}".format(os.path.dirname(os.path.realpath(__file__)), sys.argv[1])
    maze = DangerousMaze(file)
    # print("%s\nCost:%d".format(maze.board, maze.cost))

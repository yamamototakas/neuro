#!C:\bin\Python34\python.exe
# -*- coding: utf-8 -*-

# import random
# import time
# import re
# import requests
import math
import random


def function(input):
    return 1.0 / (1.0 + math.exp(-1.0*input))


class Neuron:
    def __init__(self, layer_id, unit_id, num_unit, eta, alpha, initial_value=0):
        self.lid = layer_id
        self.uid = unit_id
        self.eta = eta
        self.alpha = alpha
        self.weight = []
        self.d_weight = []

        if(layer_id > 0):
            if(initial_value == 0):
                for i in range(num_unit[layer_id-1]):
                    self.weight.append(random.random()/5 - 0.1)
                    self.d_weight.append(0.0)
            else:
                for i in range(num_unit[layer_id-1]):
                    self.weight.append(initial_value)
                    self.d_weight.append(0.0)
        else:
            # print("First layer: no weight")
            pass
        # print("constructer(w: d_w) ->", self.weight, self.d_weight)

    def output(self, fstream):
        temp = 0.0
        # print("lid:uid ->", self.lid, ":", self.uid)
        # print(fstream, self.weight)
        for j in range(len(self.weight)):
            # print(self.lid-1, "/", j, "/", len(self.weight))
            # print("fstream[self.lid-1][j]:self.weight[j] ->", fstream[self.lid-1][j], self.weight[j])
            temp += fstream[self.lid-1][j]*self.weight[j]

        fstream[self.lid][self.uid] = function(temp)
        # print("In output, w; ", self.weight, self.d_weight)

        return fstream[self.lid][self.uid]

    def propagation(self, fstream, bstream):
        # print("In BP w; ", self.weight, self.d_weight)
        bstream[self.lid][self.uid] = bstream[self.lid][self.uid] *\
            fstream[self.lid][self.uid] * (1-fstream[self.lid][self.uid])
        # print("In bp; lid:uid -> ", self.lid, self.uid, bstream[self.lid][self.uid])
        # print("w; ", self.weight, self.d_weight)
        # print("bstream ->", bstream[self.lid][self.uid])

        for j in range(len(self.weight)):
            bstream[self.lid-1][j] += bstream[self.lid][self.uid]*self.weight[j]
        
        # print(" In bp; weight", self.weight)
        return True

    def modify(self, fstream, bstream):
        for j in range(len(self.weight)):
            self.d_weight[j] = self.eta * bstream[self.lid][self.uid] *\
                fstream[self.lid-1][j] + self.alpha*self.d_weight[j]
            self.weight[j] += self.d_weight[j]
        
        # print("weight after modify ->", self.d_weight, self.weight)

        return True


class NeuralNet():
    def __init__(self, num_unit, eta, alpha):
        self.n_layer = len(num_unit)
        self.units = []
        self.f_stream = []
        self.b_stream = []

        for i in range(self.n_layer):
            temp_units = []
            temp_fstream = []
            temp_bstream = []
            for j in range(num_unit[i]):
                temp_unit = Neuron(i, j, num_unit, eta, alpha)
                # , initial_value=0.1)
                temp_units.append(temp_unit)
                temp_fstream.append(1.0)
                temp_bstream.append(0.0)
            # print(temp_units)
            self.units.append(temp_units)
            self.f_stream.append(temp_fstream)
            self.b_stream.append(temp_bstream)
        # print(self.f_stream, self.b_stream, self.units)

    def final_output(self, in_value, out_value):
        for j in range(len(in_value)):
            self.f_stream[0][j] = in_value[j]

        for i in range(1, self.n_layer):
            for j in range(len(self.units[i])):
                # print(i, " ", j)
                self.units[i][j].output(self.f_stream)

        for j in range(len(out_value)):
            out_value[j] = self.f_stream[self.n_layer-1][j]

        # print("f;", self.f_stream)

        return True

    def back_propagation(self, target_value):
        for i in range(self.n_layer):
            for j in range(len(self.b_stream[i])):
                self.b_stream[i][j] = 0.0

        for j in range(len(target_value)):
            self.b_stream[self.n_layer-1][j] = target_value[j] - self.f_stream[self.n_layer-1][j]

        # print("b;", self.b_stream)

        for i in range(self.n_layer-1, 0, -1):
            for j in range(len(self.b_stream[i])):
                self.units[i][j].propagation(self.f_stream, self.b_stream)
            # print('i=', i, end="")
        # print()
        # print(" After BP ->", self.b_stream)

        for i in range(1, self.n_layer):
            for j in range(len(self.units[i])):
                self.units[i][j].modify(self.f_stream, self.b_stream)

        return True

    def print_bstream(self, flag):
        if(flag):
            for layer in self.b_stream:
                for each in layer:
                    print(each, " ", end="")
                else:
                    print()


    

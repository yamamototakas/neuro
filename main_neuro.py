#!C:\bin\Python34\python.exe
# -*- coding: utf-8 -*-

import collections
import Neuro
import os
import sys
import pdb
# from pudb import set_trace; set_trace()
# import random
# import time
# import re
# import requests


def input_data(file_path: str):
    data = []
    try:
        f = open(file_path, 'r')
    except FileNotFoundError as e:
        print('except: Cannot write to {0}'.format(file_path), file=sys.stderr)
        print('  e: [{0}]'.format(e), file=sys.stderr)
    except IndexError as e:
        print('Usage: %s TEXTFILE')
    except IOError as e:
        print('%s cannot be opened.')
    except:
        print("other exception")
    else:
        # print('contains', len(f.read().split(' ')), 'words.')
        for line in f:
            words = line.split(',')
            temp_dic = {}
            if(words[0].isdigit() and len(words) == 10):
                temp_dic['Date'] = int(words[0])
                temp_dic['Open_price'] = float(words[1])
                temp_dic['Hi_price'] = float(words[2])
                temp_dic['Low_price'] = float(words[3])
                temp_dic['End_price'] = float(words[4])
                temp_dic['S_price'] = float(words[5])
                temp_dic['Swap'] = int(words[6])
                temp_dic['Volume'] = int(words[7])
                temp_dic['Open_Int'] = int(words[8])
                data.append(temp_dic)
            else:
                pass
    finally:
        f.close()
    return tuple(data)


def input_data_dic(file_path):
    data = []
    try:
        f = open(file_path, 'r')
    except FileNotFoundError as e:
        print('except: Cannot write to {0}'.format(file_path), file=sys.stderr)
        print('  e: [{0}]'.format(e), file=sys.stderr)
    except IndexError as e:
        print('Usage: %s TEXTFILE')
    except IOError as e:
        print('%s cannot be opened.')
    except:
        print("other exception")
    else:
        # print('contains', len(f.read().split(' ')), 'words.')
        for line in f:
            words = line.split(',')
            temp_dic = {}
            data_dic = {}
            if(words[0].isdigit() and len(words) == 10):
                temp_dic['Open_price'] = float(words[1])
                temp_dic['Hi_price'] = float(words[2])
                temp_dic['Low_price'] = float(words[3])
                temp_dic['End_price'] = float(words[4])
                temp_dic['S_price'] = float(words[5])
                temp_dic['Swap'] = int(words[6])
                temp_dic['Volume'] = int(words[7])
                temp_dic['Open_Int'] = int(words[8])
                data_dic[words[0]] = temp_dic
                data.append(data_dic)
            else:
                pass
    finally:
        f.close()
    return tuple(data)


if __name__ == '__main__':
    print("Hello World")

    script_name = sys.argv[0]
    infile = 'USDollar.csv'
    lastuidl_lists = []
    '''
    print(__name__)
    print(__file__)
    print(script_name)
    print(os.path.basename(__file__)) # スクリプト名
    print(os.path.abspath(__file__))  # スクリプトの絶対パス
    print(os.path.dirname(__file__))
    print(os.path.abspath(os.path.dirname(__file__)))  # スクリプトあるディレクトリの絶対パス
    print(os.getcwd())  # 実行時カレントディレクトリの絶対パス
    '''

    file_path = os.path.abspath(os.path.dirname(__file__))
    exe_path = os.getcwd()
    infile = file_path + "\\" + infile
    input_data(infile)
    input_data_dic(infile)

    units = [2, 2, 2]
    in_value = [0.2, 0.8]
    output = [0, 0]
    nuralnet = Neuro.NeuralNet(units, 0.5, 0.5)
    nuralnet.print_bstream(True)
    nuralnet.final_output(in_value, output)

    test_layer = 5
    test_units = []
    for i in range(5):
        test_temp_units = []
        for j in range(8):
            test_temp_units.append(i*j)
        test_units.append(test_temp_units)

    print(test_units)

    '''
    # t_units = defaultdict(list)

    for layer in test_units:
        for unit in layer:
            print(unit, end="")
        else:
            print()
            # "os.linesep)
        for i, unit in enumerate(reversed(layer)):
            print(i, '-->', unit)
    '''
    # End of function

    te_units = [2, 2, 1]
    te_in = [[0.9, 0.9], [0.9, 0.1], [0.1, 0.1], [0.1, 0.9]]
    te_target = [[0.1], [0.9], [0.1], [0.9]]
    te_out = [0.0]

    te_nuralnet = Neuro.NeuralNet(te_units, 0.5, 0.5)
    # te_nuralnet.print_bstream(True)
    for T in range(10000):
        for i, each_target in enumerate(te_target):
            pdb.set_trace()
            te_nuralnet.final_output(te_in[i], te_out)
            print(te_out, end="")
            te_nuralnet.BP(each_target)
        print()

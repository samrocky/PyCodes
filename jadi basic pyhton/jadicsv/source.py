import csv
from statistics import mean 
from os.path import dirname, join
from collections import OrderedDict

def calculate_averages(input_file_name, output_file_name):
    with open(join(dirname(__file__), "./{}".format(input_file_name)), 'r') as fin:
        reader = csv.reader(fin)
        outlist = []
        for row in reader:
            grades = []
            name = row[0]
            for i in row[1:]:
                grades.append(float(i))
            #print(name, mean(grades))
            a = '{},{}\n'.format(name, mean(grades))
            outlist.append(a)
    with open(join(dirname(__file__), "./{}".format(output_file_name)), 'w') as fout:
        for i in outlist:
            fout.write(i)
        fout.close()
    #print(outlist)

def calculate_sorted_averages(input_file_name, output_file_name):
    with open(join(dirname(__file__), "./{}".format(input_file_name)), 'r') as fin:
        reader = csv.reader(fin)
        meanod = OrderedDict()
        sortedod = []
        for row in reader:
            grades = []
            name = row[0]
            for i in row[1:]:
                grades.append(float(i))
            meanod[mean(grades)] = name
            #print(name, mean(grades))
        sortedod = sorted(meanod)
        #for i, j in meanod.items():
            #print(i, j)
        #print(sortedod)
        outlist = []
        for i in sortedod:
            a = '{},{}\n'.format(meanod[i], i)
            outlist.append(a)
        #print(outlist)
    with open(join(dirname(__file__), "./{}".format(output_file_name)), 'w') as fout:
        for i in outlist:
            fout.write(i)
        fout.close()

def calculate_three_best(input_file_name, output_file_name):
    with open(join(dirname(__file__), "./{}".format(input_file_name)), 'r') as fin:
        reader = csv.reader(fin)
        meanod = OrderedDict()
        sortedod = []
        for row in reader:
            grades = []
            name = row[0]
            for i in row[1:]:
                grades.append(float(i))
            meanod[mean(grades)] = name
            #print(name, mean(grades))
        sortedod = sorted(meanod)
        #for i, j in meanod.items():
            #print(i, j)
        #print(sortedod)
        outlist = []
        for i in sortedod[::-1][0:3]:
            a = '{},{}\n'.format(meanod[i], i)
            outlist.append(a)
        #print(outlist)
    with open(join(dirname(__file__), "./{}".format(output_file_name)), 'w') as fout:
        for i in outlist:
            fout.write(i)
        fout.close()

def calculate_three_worst(input_file_name, output_file_name):
    with open(join(dirname(__file__), "./{}".format(input_file_name)), 'r') as fin:
        reader = csv.reader(fin)
        meanod = OrderedDict()
        sortedod = []
        for row in reader:
            grades = []
            name = row[0]
            for i in row[1:]:
                grades.append(float(i))
            meanod[mean(grades)] = name
            #print(name, mean(grades))
        sortedod = sorted(meanod)
        #for i, j in meanod.items():
            #print(i, j)
        #print(sortedod)
        outlist = []
        for i in sortedod[0:3]:
            #a = '{},{}\n'.format(meanod[i], i)
            a = '{}\n'.format(i)
            outlist.append(a)
        #print(outlist)
    with open(join(dirname(__file__), "./{}".format(output_file_name)), 'w') as fout:
        for i in outlist:
            fout.write(i)
        fout.close()

def calculate_average_of_averages(input_file_name, output_file_name):
    with open(join(dirname(__file__), "./{}".format(input_file_name)), 'r') as fin:
        reader = csv.reader(fin)
        outlist = []
        for row in reader:
            grades = []
            name = row[0]
            for i in row[1:]:
                grades.append(float(i))
            #print(name, mean(grades))
            outlist.append(mean(grades))
    with open(join(dirname(__file__), "./{}".format(output_file_name)), 'w') as fout:
        fout.write(str(mean(outlist)))
        fout.close()
    #print(outlist)
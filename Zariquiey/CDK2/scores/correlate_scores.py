#!/usr/bin/env python3

import sys
import re
from scipy import stats

if len(sys.argv) != 3:
    raise Exception("This script requires two arguments")

def read_scores_file(fn):
    scores = {}
    with open(fn, "r") as score_file:
        for line in score_file:
            line = line.strip()
            if re.match('^ *$', line):
                continue
            if re.match('^ *#', line):
                continue
            name, value = line.split()
            if re.match(r'[-+]?\d*\.?\d+(?:[eE][-+]?\d+)?$',value):
                scores[name] = float(value)
            else:
                print("Score is not a number")
                exit()

    return scores

def check_keys(scores_a, scores_b):
    if len(scores_a) != len(scores_b):
        raise Exception("The score tables do not have the same size")
    for key, val in scores_a.items():
        if not key in scores_b:
            raise Exception(f"Entry {key} not found in both files")

def correlation_r(scores_a, scores_b):
    x = []
    y = []
    for key, val in scores_a.items():
        x.append(scores_a[key])
        y.append(scores_b[key])
    r, p = stats.pearsonr(x, y)
    return r


# Read files
scores1 = read_scores_file(sys.argv[1])
scores2 = read_scores_file(sys.argv[2])
check_keys(scores1, scores2)

# Calculate correlation
print("%.3f" % correlation_r(scores1, scores2)**2)


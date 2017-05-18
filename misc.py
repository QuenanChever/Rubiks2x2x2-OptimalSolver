# ########################################  Miscellaneous functions ####################################################
from os import path, mkdir


def rotate_right(arr, l, r):
    """"Rotates array arr right between l and r. r is included."""
    temp = arr[r]
    for i in range(r, l, -1):
        arr[i] = arr[i-1]
    arr[l] = temp


def rotate_left(arr, l, r):
    """"Rotates array arr left between l and r. r is included."""
    temp = arr[l]
    for i in range(l, r):
        arr[i] = arr[i+1]
    arr[r] = temp


def get_pruning_table_path(table_name):
    """Returns the path corresponding to the given pruning table"""
    pruning_dir = path.join(path.dirname(path.realpath(__file__)), 'pruning')
    if not path.exists(pruning_dir):
        mkdir(pruning_dir)
    return path.join(pruning_dir, table_name)

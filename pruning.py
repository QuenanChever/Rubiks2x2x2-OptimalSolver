# ##################### The pruning table cuts the search tree during the search. ######################################
# ########################## In this case it it gives the exact distance to the solved state. ##########################

import defs
import enums
import moves as mv
from os import path
from misc import get_pruning_table_path
import array as ar

corner_depth = None


def create_cornerprun_table():
    """Creates/loads the corner pruning table."""
    table_name = "cornerprun"
    table_path = get_pruning_table_path(table_name)
    global corner_depth
    if not path.isfile(table_path):
        print("creating " + table_name + " table...")
        corner_depth = ar.array('b', [-1] * (defs.N_CORNERS * defs.N_TWIST))
        corners = 0  # values for solved cube
        twist = 0
        corner_depth[defs.N_TWIST * corners + twist] = 0
        done = 1
        depth = 0
        while done != defs.N_CORNERS * defs.N_TWIST:
            for corners in range(defs.N_CORNERS):
                for twist in range(defs.N_TWIST):
                    if corner_depth[defs.N_TWIST * corners + twist] == depth:
                        for m in enums.Move:
                            corners1 = mv.cornperm_move[9 * corners + m]
                            twist1 = mv.corntwist_move[9 * twist + m]
                            idx1 = defs.N_TWIST * corners1 + twist1
                            if corner_depth[idx1] == -1:  # entry not yet filled
                                corner_depth[idx1] = depth + 1
                                done += 1
                                if done % 50000 == 0:
                                    print('.', end='', flush=True)

            depth += 1
        print()
        fh = open(table_path, "wb")
        corner_depth.tofile(fh)
    else:
        # print("loading " + table_name + " table...")
        fh = open(table_path, "rb")
        corner_depth = ar.array('b')
        corner_depth.fromfile(fh, defs.N_CORNERS * defs.N_TWIST)
    fh.close()

create_cornerprun_table()


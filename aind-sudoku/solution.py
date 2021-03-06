
from utils import *
import collections

row_units = [cross(r, cols) for r in rows]
column_units = [cross(rows, c) for c in cols]
square_units = [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')]
diagonal_units = [['A1','B2','C3','D4','E5','F6','G7','H8','I9'],['A9','B8','C7','D6','E5','F4','G3','H2','I1']]
unitlist = row_units + column_units + square_units + diagonal_units


# Must be called after all units (including diagonals) are added to the unitlist
units = extract_units(unitlist, boxes)
peers = extract_peers(units, boxes)


def naked_twins(values):
    for u in unitlist:
        val = [values[p] for p in u]
        uni = set(val)

        num = collections.defaultdict(int)  
        for item in val:
            num[item] += 1

        for key in num:
            if len(key)==2 and num[key]==2:
                for p in u:
                    if not values[p]==key:
                        values[p] = values[p].replace(key[0], '')
                        values[p] = values[p].replace(key[1], '')
    return values


def eliminate(values, new_assign):
    for key in new_assign:
        v = values[key]
        for p in peers[key]:
            values[p] = values[p].replace(v,'')
    naked_twins(values)


def only_choice(values, tocheck):
    new_assign = []
    for key in tocheck:
        val = []
        for p in units[key]:
            val.append(''.join([values[i] for i in p if not i==key]))

        assign = False
        for v in values[key]:
            for p in val:
                if p.find(v)<0 and not assign:
                    assign = True
                    values[key] = v
                    new_assign.append(key)
                    tocheck.remove(key)
    return new_assign, tocheck


def reduce_puzzle(values, new_assign, tocheck):
    stalled = False
    eliminate(values, new_assign)
    while not stalled:
        num_to_check_before = len(tocheck)
        new_assign, tocheck = only_choice(values, tocheck)
        eliminate(values, new_assign)

        stalled = len(tocheck) == num_to_check_before
        if len([box for box in values.keys() if len(values[box]) == 0]):
            return tocheck, False
    return tocheck, True


def recur_search(values, new_assign, tocheck):
    tocheck, ret = reduce_puzzle(values, new_assign, tocheck)
    if len(tocheck)==0 and ret: return values, True
        
    sol = values
    valid = False
    if ret:
        tocheck.sort(key=lambda t : len(values[t]))
        key = tocheck[0]
        tocheck.remove(key)
        
        for v in values[key]:
            new_values = values.copy()
            new_tocheck = tocheck.copy()
            
            new_assign = [key]
            new_values[key] = v
            sol, valid = recur_search(new_values, new_assign, new_tocheck)
            if valid: break
    return sol, valid


def search(values):
    new_assign = [box for box in values.keys() if len(values[box]) == 1]
    tocheck = [box for box in values.keys() if len(values[box]) > 1]
    reduce_puzzle(values, new_assign, tocheck)
    sol, valid = recur_search(values, new_assign, tocheck)
    return sol


def solve(grid):
    values = grid2values(grid)
    values = search(values)
    return values


if __name__ == "__main__":
    diag_sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    display(grid2values(diag_sudoku_grid))
    result = solve(diag_sudoku_grid)
    display(result)

    try:
        import PySudoku
        PySudoku.play(grid2values(diag_sudoku_grid), result, history)

    except SystemExit:
        pass
    except:
        print('We could not visualize your board due to a pygame issue. Not a problem! It is not a requirement.')

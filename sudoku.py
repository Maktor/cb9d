import matplotlib.pyplot as plt
import random

def create_base_grid():
    base = 3
    side = base * base

    def pattern(r, c):
        return (base * (r % base) + r // base + c) % side

    def shuffle(s):
        return random.sample(s, len(s))

    rBase = range(base)
    rows = [g * base + r for g in shuffle(rBase) for r in shuffle(rBase)]
    cols = [g * base + c for g in shuffle(rBase) for c in shuffle(rBase)]
    nums = shuffle(range(1, base * base + 1))

    board = [[nums[pattern(r, c)] for c in cols] for r in rows]
    return board

def mask_grid(board, difficulty=0.6):
    side = 9
    squares = side * side
    empties = int(squares * difficulty)

    puzzle = [row[:] for row in board]

    for p in random.sample(range(squares), empties):
        puzzle[p // side][p % side] = 0

    return puzzle

def save_sudoku_image(puzzle, filename):
    fig, ax = plt.subplots(figsize=(8, 8))

    for i in range(10):
        linewidth = 3 if i % 3 == 0 else 1
        ax.plot([0, 9], [i, i], color='black', linewidth=linewidth)
        ax.plot([i, i], [0, 9], color='black', linewidth=linewidth)

    for r in range(9):
        for c in range(9):
            val = puzzle[r][c]
            if val != 0:
                ax.text(c + 0.5, 8.5 - r, str(val),
                        va='center', ha='center', fontsize=22, family='sans-serif', weight='bold')

    ax.set_xlim(0, 9)
    ax.set_ylim(0, 9)
    ax.axis('off')

    plt.savefig(filename, bbox_inches='tight', dpi=300)
    plt.close()

full_solution = create_base_grid()
puzzle_state = mask_grid(full_solution, difficulty=0.6)

print("GTFA SOLUTION GRID:")
for row in full_solution:
    print(row)

save_sudoku_image(puzzle_state, "hickory_sudoku_taskkkkk.png")

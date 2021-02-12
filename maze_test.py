# Archivo de pruebas

import pytest
import maze

"""
Solution test
"""
@pytest.mark.parametrize(
    "file, goal_coord",
    [
        ( "mazes/maze1.txt", (0,5) ),
        ( "mazes/maze2.txt", (8,13)),
        ( "mazes/maze3.txt", (2,1) ),
        ( "mazes/maze4.txt", (2,1) ),
        ( "mazes/maze5.txt", (0,1) ),
    ]
)
def test_maze_solution(file, goal_coord): 
    m = maze.Maze(file)
    m.solve()
    assert m.solution[1][-1] == goal_coord, "solution test failed"


"""
Explored nodes test
"""
@pytest.mark.parametrize(
    "file, num_explored",
    [
        ( "mazes/maze1.txt", 11),
        ( "mazes/maze2.txt", 77),
        ( "mazes/maze3.txt",  6),
        ( "mazes/maze4.txt", 27),
        ( "mazes/maze5.txt",  6),
    ]
)
def test_num_explored(file, num_explored):
    m = maze.Maze(file)
    m.solve()
    assert m.num_explored == num_explored, "number of nodes test failed"
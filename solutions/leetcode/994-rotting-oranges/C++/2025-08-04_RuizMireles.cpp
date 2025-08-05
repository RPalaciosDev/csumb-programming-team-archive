/**
* ===========================================================
*     Author:        Hugo Ruiz Mireles
*     Created:       2025-08-05
*     Last Updated:  2025-08-05
*     Problem:       994 - Rotting Oranges
*     Platform:      LeetCode
*     Difficulty:    Medium
*     Language:      C++
*     Tags:          Graph, DFT, DFS
* ===========================================================
*
* Description:
* --------------------
* You are given an `m x n` grid where each cell can have one of three values:
* 
* - `0` representing an empty cell,
* - `1` representing a fresh orange, or
* - `2` representing a rotten orange.
* 
* Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.
* 
* Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return `-1`.
* 
* Approach:
* ___________________
* The normal solution uses Breadth-First Traversal (BFT) to simulate the rotting process.
* However, this solution uses Depth-First Traversal (DFT) to achieve the same result.
*
* First, the grid is modified to represent the time in minutes instead of the status of the oranges.
*
* The grid is modified to have:
* - `-1` for empty cells (Negative time makes it easy to ignore)
* - `INT_MAX` for fresh oranges (Outside the range of time so easy to check for after DFT)
* - `0` for rotten oranges (Time zero since they are already rotten and take not time to rot)
* We simultaneously collect the coordinates of all rotten oranges to start the DFT from them efficiently.
* 
* We loop through all the initially rotten orange coordinates and call the `dft` function starting at that coordinate.
* The function arguments are the grid, the rotten orange row and column, and the starting time 0 minutes.
* 
* In the `dft` function we have two base cases:
* 1. If the current row or column is out of bounds, we return.
* 2. If the current cell's time is less than the current minute, we return (this is like if the orange was already rotten when we got there).
*
* If neither base case is hit, we set the current cell's time to the current minute.
* 
* Then we recursively call `dft` on the four adjacent cells (up, down, left, right) with the current minute incremented by one.
*
* Finally, the maximum time taken for any orange to rot is returned, or `-1` if any fresh orange remains.
*/

#include <iostream>
#include <vector>
#include <utility> // for std::pair
#include <algorithm> // for std::max

using namespace std;

class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        const int ROTTEN = 2;
        const int FRESH = 1;
        const int EMPTY = 0;

        const int ROTTEN_TIME = 0;
        const int FRESH_TIME = INT_MAX;
        const int EMPTY_TIME = -1;
        
        int numRows = grid.size();
        int numCols = grid[0].size();
        
        std::vector<std::pair<int, int>> rottenCoordinates;

        // change grid to represent minutes not statuses
        for (int r = 0; r < numRows; r++) {
            for (int c = 0; c < numCols; c++) {
                if (grid[r][c] == EMPTY) {
                    grid[r][c] = EMPTY_TIME;
                } else if (grid[r][c] == FRESH) {
                    grid[r][c] = FRESH_TIME;
                } else if (grid[r][c] == ROTTEN) {
                    grid[r][c] = ROTTEN_TIME;
                    rottenCoordinates.push_back({ r, c });
                } 
            }
        }

        for (auto [row, col] : rottenCoordinates) {
            dft(grid, row, col, 0);
        }

        int minutes = 0;
        for (int r = 0; r < numRows; r++) {
            for (int c = 0; c < numCols; c++) {
                if (grid[r][c] == FRESH_TIME) {
                    return -1;
                }
                minutes = std::max(minutes, grid[r][c]);
            }
        }
        return minutes;
    }
private:
    void dft(std::vector<std::vector<int>>& timeGrid, int row, int col, int currentMinute) {
        int numRows = timeGrid.size();
        int numCols = timeGrid[0].size();

        if ((row < 0 || row >= numRows) || (col < 0 || col >= numCols) || (timeGrid[row][col] < currentMinute)) return;

        timeGrid[row][col] = currentMinute;

        dft(timeGrid, row + 1, col, currentMinute + 1);
        dft(timeGrid, row - 1, col, currentMinute + 1);
        dft(timeGrid, row, col + 1, currentMinute + 1);
        dft(timeGrid, row, col - 1, currentMinute + 1);
    }
};

void printGrid(const vector<vector<int>>& grid);

int main() {
    Solution solution;
    vector<vector<int>> grid = {
        {2, 1, 1},
        {1, 1, 0},
        {0, 1, 1}
    };
    printGrid(grid);
    int result = solution.orangesRotting(grid); // should be 4
    cout << "Test 1, Minimum time to rot all oranges: " << result << " minutes" << endl;

    grid = {
        {2, 1, 1},
        {1, 1, 0},
        {0, 0, 1}
    };

    printGrid(grid);
    result = solution.orangesRotting(grid); // should be -1
    cout << "Test 2, Minimum time to rot all oranges: " << result << " minutes" << endl;

    grid = {
        {0, 2}
    };
    printGrid(grid);
    result = solution.orangesRotting(grid); // should be 0
    cout << "Test 3, Minimum time to rot all oranges: " << result << " minutes" << endl;
    
    return 0;
}

void printGrid(const vector<vector<int>>& grid) {
    cout << "Grid:" << endl;
    for (const auto& row : grid) {
        for (int cell : row) {
            cout << cell << " ";
        }
        cout << endl;
    }
}
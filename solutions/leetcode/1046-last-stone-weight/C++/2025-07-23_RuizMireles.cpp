/**
* ===========================================================
*     Author:        Hugo Ruiz-Mireles
*     Created:       2025-07-23
*     Last Updated:  2025-07-23
*     Problem:       1046 - Last Stone Weight
*     Platform:      LeetCode
*     Difficulty:    Easy
*     Language:      C++
*     Tags:          Heap
* ===========================================================
*
* Description:
* --------------------
* 
* Approach:
* ___________________
* We can use a max heap to keep track of the stones.
* We can then pop the two heaviest stones and calculate the difference.
* If the difference is not 0, we can push the difference back into the heap.
* We can continue this process until there is at most one stone left.
* If there is one stone left, we can return its weight.
* If there are no stones left, we can return 0.
*/

# include <iostream>
# include <vector>
# include <algorithm>

using namespace std;

class Solution {
    private:
        void smashRocks(vector<int>& stones) {
            if (stones.size() < 2) return;
    
            std::pop_heap(stones.begin(), stones.end());
            int y = stones.back();
            stones.pop_back();
    
            std::pop_heap(stones.begin(), stones.end());
            int x = stones.back();
            stones.pop_back();
    
            int result;
            if (x < y)
                result = y - x;
            else
                result = x - y;
            
            if (result != 0) {
                stones.push_back(result);
                std::push_heap(stones.begin(), stones.end());
            }
            
            smashRocks(stones);
        }
    public:
        int lastStoneWeight(vector<int>& stones) {
            std::make_heap(stones.begin(), stones.end());
            smashRocks(stones);
    
            if (stones.empty())
                return 0;
            else
                return stones[0];
        }
    };
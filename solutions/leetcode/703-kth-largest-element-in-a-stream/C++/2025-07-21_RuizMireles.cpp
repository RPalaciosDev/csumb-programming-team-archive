/**
* ===========================================================
*     Author:        Hugo Ruiz-Mireles
*     Created:       2025-07-21
*     Last Updated:  2025-07-21
*     Problem:       703 - Kth Largest Element in a Stream
*     Platform:      LeetCode
*     Difficulty:    Easy
*     Language:      C++
*     Tags:          
* ===========================================================
*
* Description:
* --------------------
* Design a class to find the kth largest element in a stream.
* Note that it is the kth largest element in the sorted order, not the kth distinct element.
* Implement the KthLargest class:
* - KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
* - int add(int val) Appends the integer val to the stream and returns the element representing the kth largest element in the stream.
* 
* Approach:
* ___________________
* XXXXX
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
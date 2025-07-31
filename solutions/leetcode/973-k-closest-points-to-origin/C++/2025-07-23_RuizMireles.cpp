/**
* ===========================================================
*     Author:        Hugo Ruiz-Mireles
*     Created:       2025-07-23
*     Last Updated:  2025-07-23
*     Problem:       973 - K Closest Points to Origin
*     Platform:      LeetCode
*     Difficulty:    Easy
*     Language:      C++
*     Tags:          
* ===========================================================
*
* Description:
* --------------------
* Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, 
* return the k closest points to the origin (0, 0).
* The distance between two points on the X-Y plane is the Euclidean distance (i.e., sqrt((x1 - x2)^2 + (y1 - y2)^2)).
* You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).
* 
* Approach:
* ___________________
* XXXXX
*/
# include <iostream>
# include <vector>
# include <algorithm>
# include <queue>

using namespace std;

class Solution {
    private:
        // heaps sort pairs by the first element
        std::priority_queue<std::pair<int, std::vector<int>>> maxHeap;
    public:
        vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
            // initial idea, use a max heap of pairs where 
            //  - the first value is dist: (sqrt((x1 - x2)^2 + (y1 - y2)^2))
            //    - This would mean the heap would be organized by distances
            //  - The second element will be the nested vectors from points
            //
            //  Then we just calculate the dist of each and see if we can put it into the heap
            //  The heap will be limited to size k 
            // 
    
            for (int i = 0; i < points.size(); i++) {
                int x = points[i][0] * points[i][0];
                int y = points[i][1] * points[i][1];
            
                maxHeap.push({x + y, points[i]});
            
                if (maxHeap.size() > k) {
                    maxHeap.pop();
                }
            }
    
            std::vector<std::vector<int>> ans(k);
            int i = 0;
            while (!maxHeap.empty()) {
                ans[i++] = maxHeap.top().second;
                maxHeap.pop();
            }
    
            return ans;
        }
    };
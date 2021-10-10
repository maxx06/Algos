/*

    Max Xiong
    C++, Leetcode - Contains Duplicates
    9 October 2021
    _________________________________
    


*/

#include <iostream>

#include <fstream>

#include <string>

#include <vector>

using namespace std;

class Solution {

public:

    bool containsDuplicate(vector<int>& nums) {

        // Solution 1: Generally worse than the second, less code. 
        // Hashing to a set to remove duplicates and compare sizes of the two
	    // return nums.size() != set(nums.begin(), nums.end()).size();
        
        
        // Solution 2: better time & space complexity, iterative searching, 
        // checking index with next index to see if they match. SORT FIRST. 
        // Let's say we have an array with size 4, we add the "-1" so that 
        // the last index we check is index 2, and 2 + 1 is 3, the last index. 
        // We will get a heap overflow without it.
        
        if(nums.size() == 0 || nums.size() == 1)
        {
            return false;
        }
        
        sort(nums.begin(), nums.end());
        for(int i = 0; i < nums.size()-1; i++)
        {
            if(nums[i] == nums[i+1])
            {
                return true;
            }
        }
        return false;

    }

};

int main(){
    
}
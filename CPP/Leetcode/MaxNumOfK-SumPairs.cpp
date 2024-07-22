class Solution {
public:
    int maxOperations(vector<int>& nums, int k) {
        int count = 0;

        // O(n log n) solution, O(1) space
        // sort(nums.begin(), nums.end());
        // int l = 0, r = nums.size()-1;
        // while(l < r){
        //     if(nums[l] + nums[r] == k){
        //         count++;
        //         l++;
        //         r--;
        //     }
        //     else if(nums[l] + nums[r] < k){
        //         l++;
        //     }
        //     else r--;
        // }

        // O(N) w/ hashmap, O(N) space; throw a hashmap at it
        unordered_map<int, int> hash;
        for(int i : nums){
            hash[i]++;
        }
        for(int i : nums){
            if(i == k-i){
                if(hash[i] >= 2){
                    count++;
                    hash[i]=hash[i]-2;
                }
            }
            else if(hash[i] > 0 && hash[k-i] > 0){
                count++;
                hash[i]--;
                hash[k-i]--;
            }
        }
        return count;
    }
};
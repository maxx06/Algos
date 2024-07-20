class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        /*
        ANALYSIS:

        naive approach ofc is to iterate array twice and manually calculate each product excluding self

        more time optimized: use prefix and suffic arrays
        product of everything except itself is just the product of everything before multiplied by everything after it: in code,
        pref[i-1] * suff[i+1].

        account for corner cases as well


        more space optimized: 
        
        */
        int pref[nums.size()], suff[nums.size()];
        pref[0] = nums[0];
        suff[nums.size()-1] = nums[nums.size()-1];

        for(int i = 1; i < nums.size(); i++){
            pref[i] = pref[i-1] * nums[i];
        }
        for(int i = nums.size()-2; i >= 0; i--){
            suff[i] = suff[i+1] * nums[i];
        }

        vector<int> res;
        res.push_back(suff[1]);
        for(int i = 1; i < nums.size()-1; i++){
            res.push_back(pref[i-1] * suff[i+1]);
        }
        res.push_back(pref[nums.size()-2]);
        return res;
    }
};
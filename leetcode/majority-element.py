class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int size = nums.size();
        int freq;
        for(int i = 0; i < size; ++i){
            freq = 0;
            for(int j = i; j < size; ++j){
                if(nums[j] == nums[i]) freq++;
            }
            if ( freq > size/2) return nums[i];
        }
        return 0;
    }
};
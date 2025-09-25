class Solution {
public:
    int majorityElement(vector<int>& nums) {

        int freq;
        for(int i = 0; i < nums.size(); ++i){
            freq = 0;
            for(int j = i; j < nums.size(); ++j){
                if(j == i) freq = freq+1;
            }
            if ( freq > (nums.size()/2)) return nums[i];
        }
        return 0;
    }
};
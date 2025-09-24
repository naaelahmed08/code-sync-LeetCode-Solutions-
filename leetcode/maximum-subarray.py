class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        // length = nums.size(); 
        int max_sum = INT_MIN;
        for(int start = 0; start < nums.size(); start ++){
            int curr_sum = 0;
            for(int end = start; end < nums.size(); end++){
                curr_sum = curr_sum + nums[end];
                max_sum = max(max_sum , curr_sum);
                if(curr_sum < 0) curr_sum = 0;
            }
        }

        return max_sum;
        
    }
};
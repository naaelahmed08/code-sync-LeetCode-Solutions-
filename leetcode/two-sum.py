class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int length = nums.size();
        for (int i = 0; i < length; ++i){
            for (int j = i+1; j < length; ++j ){
                if (target == nums[i] + nums [j]){
                return {i,j};
            }
        }
    }
        return {};
}
    
    
};
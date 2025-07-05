class Solution {
public:
    int findLucky(vector<int>& arr) {
        unordered_map<int,int> freq;
        for (int x : arr) 
            ++freq[x];

        int ans = -1;
        for (auto& [num, count] : freq) {
            if (num == count && num > ans)
                ans = num;
        }

        return ans;
    }
};
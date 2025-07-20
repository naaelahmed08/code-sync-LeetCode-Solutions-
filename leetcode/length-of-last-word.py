class Solution {
public:
    int lengthOfLastWord(string s) {
        std::istringstream ss(s);
        string word;
        int len = 0;
        while (ss >> word) {
            len = word.size();  // overwrite len with the current word’s length
        }
        return len;
    }
};
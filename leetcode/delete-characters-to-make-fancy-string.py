class Solution {
public:
    string makeFancyString(string s) {
        stringstream ss (s);
        char c;
        vector<char> v;
        int i = 0;
        while(ss >> c){
            v.push_back(c);
        }
        int len = v.size();
        
    }
};
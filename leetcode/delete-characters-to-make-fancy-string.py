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
        char comp = v[0];
        int comp_count = 1;
        for (int  i = 1; i < v.size(); ++i){
            if(comp == v[i]){
                ++ comp_count;
            }else{
                comp = v[i];
                comp_count = 1;
            }

            if(comp_count == 3){
                v.erase(v.begin() + i);
            }
        }
        // for(int i = 0;i < v.size(); ++i){
        //     v[i] >> ss;
        // }
        // cout << s;

        string final(v.begin(), v.end());
        return final;
    }
};
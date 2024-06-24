class Solution {
public:
    string removeStars(string s) {
        // simple string solution
        // string res;
        // for(char c : s){
        //     if(c != '*'){
        //         res += c;
        //     }
        //     else
        //         res.erase(res.size()-1, 1);
        // }
        // return res;

        // intended stack solution (both O(N) )
        stack<char> st;
        for(char c : s){
            if(c != '*')
                st.push(c);
            else 
                st.pop();
        }
        string res = "";
        while(!st.empty()){
            res = st.top() + res;
            st.pop();
        }
        return res;
        
    }
};
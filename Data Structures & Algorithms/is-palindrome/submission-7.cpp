class Solution {
public:
    bool isPalindrome(string s) {
        int start = 0;
        int end = s.length() - 1;

        while (end > start) {
            if (!iswalnum(s[start])) {
                start++;
                continue;
            }
            else if (!iswalnum(s[end])) {
                end--;
                continue;
            }
            char first = (char)tolower(s[start]);
            char last = (char)tolower(s[end]);

            if (first != last) {
                return false;
            }
            else {
                start++;
                end--;
            }
        }
        return true;
    }
};

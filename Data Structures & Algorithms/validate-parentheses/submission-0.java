class Solution {
    public boolean isValid(String s) {
        Stack<Character> stacks = new Stack<>();

        for (char c : s.toCharArray()) {
            if (c == '(' || c == '{' || c == '[') {
                stacks.push(c);
            }
            else {
                if (!stacks.isEmpty()) {
                    char out = stacks.pop();
                    if (c == '}' && out == '{') {

                    }
                    else if (c == ']' && out == '[') {
                        
                    }
                    else if (c == ')' && out == '(') {
                        
                    }
                    else {
                        return false;
                    }
                }
                else {
                    return false;
                }
            }
        }
        if (!stacks.isEmpty()) {
            return false;
        }
        return true;
    }
}

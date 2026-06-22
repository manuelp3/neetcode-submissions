class Solution {
    public int evalRPN(String[] tokens) {
        Stack<Integer> stack = new Stack<>();
        int total = 0;
        stack.push(total);

        if (tokens.length == 1) {
            return Integer.parseInt(tokens[0]);
        }

        for (String token : tokens) {
            if (!(token.equals("+") || token.equals("-") || token.equals("*") || token.equals("/"))) {
                stack.push(Integer.parseInt(token));
            }
            else {
                int num = stack.pop();
                
                if (token.equals("+")) {
                    total = stack.pop() + num;
                }
                else if (token.equals("-")) {
                    total = stack.pop() - num;
                }
                else if (token.equals("*")) {
                    total =  stack.pop() * num;
                }
                else if (token.equals("/")) {
                    total = stack.pop() / num;
                }
                stack.push(total);
            }
        }
        return total;
    }
}

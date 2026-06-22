class Solution {

    public void backtrack(StringBuilder s, int open, int closed, int n, ArrayList<String> arr) {
        if (open == closed && open == n) {
            arr.add(s.toString());
            return;
        }
        if (open < n) {
            s.append("(");
            backtrack(s, open+1, closed, n, arr);
            s.deleteCharAt(s.length() - 1);
        }
        if (closed < open) {
            s.append(")");
            backtrack(s, open, closed+1, n, arr);
            s.deleteCharAt(s.length() - 1);
        }
    }

    public List<String> generateParenthesis(int n) {
        ArrayList<String> arr = new ArrayList<>();
        StringBuilder s = new StringBuilder();
        int open = 0;
        int closed = 0;
        backtrack(s, open, closed, n, arr);

        return arr;
    }
}

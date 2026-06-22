class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        int[] solution = new int[temperatures.length];
        Stack<int[]> s = new Stack<>();

        for (int i = 0; i < temperatures.length; i++) {
            while (!s.isEmpty() && temperatures[i] > s.peek()[0]) {
                int[] temp = s.pop();
                solution[temp[1]] = i - temp[1];
            }
            s.push(new int[]{temperatures[i], i});
        }
        return solution;
    }
}

class Solution {
    public int carFleet(int target, int[] position, int[] speed) {
        int[][] pair = new int[position.length][2];
        for (int i = 0; i < position.length; i++) {
            pair[i][0] = position[i];
            pair[i][1] = speed[i];
        }
        
        //System.out.println(Arrays.deepToString(pair));
        
        Arrays.sort(pair, (a, b) -> Integer.compare(a[0], b[0]));
        double min = (double)(target - pair[position.length - 1][0]) / pair[position.length - 1][1];
        int count = 1;
        
        //System.out.println(Arrays.deepToString(pair));
        
        //System.out.println(min);
        
        for (int i = position.length - 2; i >= 0; i--) {
            double calc = (double)(target - pair[i][0]) / pair[i][1];
            if (calc > min) {
                count++;
                min = calc;
                //System.out.println(min);
            }
        }
        return count;
    }
}

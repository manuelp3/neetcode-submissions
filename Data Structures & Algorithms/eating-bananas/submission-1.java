class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        Arrays.sort(piles);
        //System.out.println(Arrays.toString(piles));
        //int speed = piles[piles.length - 1];
        int speed = 1;
        //System.out.println(speed);

        while (true) {
            int count = 0;
            for (int i = piles.length - 1; i >= 0; i--) {
                count += (int)Math.ceil((double)piles[i]/speed);
                if (count > h) {
                    break;
                }
            }
            if (count <= h) {
                return speed;
            }
            speed++;
        }
        //return speed;
    }
}

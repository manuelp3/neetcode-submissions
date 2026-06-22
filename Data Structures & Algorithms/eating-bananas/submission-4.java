class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        Arrays.sort(piles);

        int l = 1;
        int r = piles[piles.length - 1];
        int mid = (l + r)/2;

        int min = r;

        while (l <= r) {
            int count = 0;

            for (int i = 0; i < piles.length; i++) {
                count += Math.ceil((double)piles[i]/mid);
            }

            if (count <= h) {
                min = Math.min(min, mid);
                r = mid - 1;
            }
            else {
                l = mid + 1;
            }
            mid = (l + r)/2;
        }
        return min;
    }
}

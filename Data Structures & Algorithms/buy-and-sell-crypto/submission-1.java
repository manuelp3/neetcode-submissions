class Solution {
    public int maxProfit(int[] prices) {
        int l = 0;
        int r = 1;
        int maxDif = 0;

        while (r < prices.length) {
            maxDif = Math.max(maxDif, prices[r] - prices[l]);
            if (prices[r] < prices[l]) {
                l = r;
            }
            r++;
        }
        return maxDif;
    }
}

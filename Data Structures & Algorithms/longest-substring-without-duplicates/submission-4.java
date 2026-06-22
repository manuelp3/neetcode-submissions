class Solution {
    public int lengthOfLongestSubstring(String s) {
        Map<Character, Integer> map = new HashMap<>();
        int length = 0;
        int maxLength = 0;

        int left = 0;
        int right = 0;

        while (right < s.length()) {
            if (!map.containsKey(s.charAt(right))) {
                map.put(s.charAt(right), right);
                length++;
            }
            else {
                left = Math.max(left, map.get(s.charAt(right)) + 1);
                map.put(s.charAt(right), right);
                length = right - left + 1;
            }
            maxLength = Math.max(maxLength, length);
            right++;
        }
        return maxLength;
    }
}

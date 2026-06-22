class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, ArrayList<String>> map = new HashMap<>();

        for (String s : strs) {
            int[] chars = new int[26];

            for (char c : s.toCharArray()) {
                chars[c - 'a']++;
            }
            String key = Arrays.toString(chars);
            map.putIfAbsent(key, new ArrayList<>());
            map.get(key).add(s);
        }
        return new ArrayList<>(map.values());
    }
}

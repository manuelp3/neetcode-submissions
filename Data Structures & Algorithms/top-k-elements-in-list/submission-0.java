class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> count = new HashMap<>();
        List<Integer>[] freq = new List[nums.length + 1];

        for (int i = 0; i < freq.length; i++) {
            freq[i] = new ArrayList<>();
        }

        for (int item : nums) {
            count.put(item, count.getOrDefault(item, 0) + 1);
        }

        for (Map.Entry<Integer, Integer> entry : count.entrySet()) {
            freq[entry.getValue()].add(entry.getKey());
        }

        int[] solution = new int[k];
        int index = 0;

        for (int i = freq.length - 1; i > 0; i--) {
            for (int j = 0; j < freq[i].size(); j++) {
                solution[index] = freq[i].get(j);
                index++;
                if (index == k) {
                    return solution;
                }
            }
        }
        return solution;
    }
}

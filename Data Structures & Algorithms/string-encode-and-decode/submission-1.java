class Solution {

    public String encode(List<String> strs) {
        String solution = "";
        
        for (String s : strs) {
            solution += "'" + Integer.toString(s.length()) + "\"" + s;
        }
        return solution;
    }

    public List<String> decode(String str) {
        List<String> arr = new ArrayList<>();

        for (int i = 0; i < str.length(); i++) {
            if (str.charAt(i) == '\'') {
                int count = i + 1;
                while (str.charAt(count) != '\"') {
                    count++;
                }
                int length = Integer.parseInt(str.substring(i + 1, count));

                String toAdd = str.substring(count + 1, count + length + 1);
                arr.add(toAdd);
            }
        }
        return arr;
    }
}

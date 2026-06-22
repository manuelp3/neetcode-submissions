class Solution {
    public boolean isPalindrome(String s) {
        s = s.toLowerCase();
        s = s.replaceAll("[^a-zA-Z0-9]", "");
        String check = "";
        
        System.out.println(s);

        if (s.length() == 0) return true;

        for (int i = s.length() - 1; i >= s.length() / 2; i--) {
            check += Character.toString(s.charAt(i));
        }
        
        if (s.length() % 2 == 0) {
            return s.substring(0, s.length()/2).equals(check);
        }
        return s.substring(0, s.length()/2 + 1).equals(check);
    }
}

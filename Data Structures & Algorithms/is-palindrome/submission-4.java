class Solution {
    public boolean isPalindrome(String s) {
        int count = 0;
        int length = s.length() - 1;

        while (length > count) {
            while (!Character.isLetterOrDigit(s.charAt(count)) && length > count) {
                count++;
            }
            while (!Character.isLetterOrDigit(s.charAt(length)) && length > count) {
                length--;
            }
            if (Character.toLowerCase(s.charAt(count)) != Character.toLowerCase(s.charAt(length))) {
                return false;
            }
            count++;
            length--;
        }
        return true;
    }
}

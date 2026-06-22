class Solution {
    public boolean isValidSudoku(char[][] board) {
        for (int i = 0; i < board.length; i++) {
            Set<Character> set = new HashSet<>();
            for (int j = 0; j < board[i].length; j++) {
                if (board[i][j] != '.') {
                    if (set.contains(board[i][j])) {
                        return false;
                    }
                    else {
                        set.add(board[i][j]);
                    }
                }
            }
        }

        for (int i = 0; i < board.length; i++) {
            Set<Character> set = new HashSet<>();
            for (int j = 0; j < board[i].length; j++) {
                if (board[j][i] != '.') {
                    if (set.contains(board[j][i])) {
                        return false;
                    }
                    else {
                        set.add(board[j][i]);
                    }
                }
            }
        }

        for (int a = 0; a < 9; a++) {
            Set<Character> set = new HashSet<>();
            for (int i = 0; i < 3; i++) {
                for (int j = 0; j < 3; j++) {
                    int row = (a / 3) * 3 + i;
                    int col = (a % 3) * 3 + j;
                    if (board[row][col] != '.') {
                        if (set.contains(board[row][col])) {
                            return false;
                        }
                        else {
                            set.add(board[row][col]);
                        }
                    }
                }
            }
        }
        return true;
    }
}

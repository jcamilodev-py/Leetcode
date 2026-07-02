import java.util.HashSet;

public class Problem2133_CheckifEveryRowandColumnContainsAllNumbers {
     public static void main(String[] args) {
        Solution2133 s = new Solution2133();
        System.out.println(s.checkValid(new int[][]{{1,2,3}, {2,3,1}, {3,1,2}}));
    }
}


class Solution2133 {
    public boolean checkValid(int[][] matrix) {
        int n = matrix.length;

        for (int i = 0; i < n; i++) {
            HashSet<Integer> r = new HashSet<>();
            HashSet<Integer> c = new HashSet<>();

            for (int j = 0; j < n; j++) {
                if (matrix[i][j] < 1 || matrix[i][j] > n ||
                    matrix[j][i] < 1 || matrix[j][i] > n) {
                    return false;
                }

                if (!r.add(matrix[i][j])) {
                    return false;
                }

                if (!c.add(matrix[j][i])) {
                    return false;
                }
            }
        }

        return true;
    }
}
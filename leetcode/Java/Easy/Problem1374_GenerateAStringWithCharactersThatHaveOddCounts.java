public class Problem1374_GenerateAStringWithCharactersThatHaveOddCounts {
    public static void main(String[] args) {
        Solution1374 s = new Solution1374();
        System.out.println(s.generateTheString(2));
    }
}

class Solution1374 {
    public String generateTheString(int n) {
        StringBuilder ans = new StringBuilder();

        if (n % 2 != 0) {
            for (int i=0; i < n; i++) {
                ans.append("a");
            }
            return ans.toString();

        }
        for (int i = 0; i < n-1; i++) {
            ans.append("a");
        }
        ans.append("b");

        return ans.toString();
    }
}
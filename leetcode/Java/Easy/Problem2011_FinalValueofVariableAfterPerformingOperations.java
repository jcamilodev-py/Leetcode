public class Problem2011_FinalValueofVariableAfterPerformingOperations {
    public static void main(String[] args) {
        Solution2011 s = new Solution2011();
        System.out.println(s.finalValueAfterOperations(new String[]{"--X","X++","X++"}));
    }
}

class Solution2011 {
    public int finalValueAfterOperations(String[] operations) {
        int ans = 0;

        for (String i : operations) {
            if (i.equals("--X") || i.equals("X--")) {
                ans--;
            } else {
                ans++;
            }
        }
        return ans;
    }
}

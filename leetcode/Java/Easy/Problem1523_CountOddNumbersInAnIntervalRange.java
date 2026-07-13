public class Problem1523_CountOddNumbersInAnIntervalRange {
    public static void main(String[] args) {
        Solution1523 s = new Solution1523();
        System.out.println(s.countOdds(8, 10));

    }
}

class Solution1523 {
    public int countOdds(int low, int high) {
        if (low % 2 == 0 && high % 2 == 0) {
            return (high - low) / 2;
        } else {
            return ((high - low) / 2) + 1;
            }
    }
        
}      
import java.util.Arrays;

public class Problem3921_ScoreValidator {
    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(Arrays.toString(s.scoreValidator(new String[]{"1","4","W","6","WD"})));
    }
}

class Solution {
    public int[] scoreValidator(String[] events) {
        int score = 0;
        int counter = 0;

        for (String i : events) {
            if (counter == 10) {
                return new int[]{score, counter};
            }
            
            if (i.equals("0") || i.equals("1") || i.equals("2") || i.equals("3") || i.equals("4") || i.equals("6") ) {
                score+=Integer.parseInt(i);
            } else if (i.equals("W")) {
                counter++;
            } else {
                score++;
            }
            
        }

        return new int []{score, counter};
    }
}
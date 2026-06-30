import java.util.ArrayList;
import java.util.List;

public class Problem119_PascalsTriangleII {
    public static void main(String[] args) {
        Solution119 s = new Solution119();
        System.out.println(s.getRow(3));
        
    }
}

class Solution119 {
    public List<Integer> getRow(int rowIndex) {
        long value = 1;
        ArrayList<Integer> ans = new ArrayList<>();

        for (int i = 0; i<=rowIndex; i++) {
            ans.add((int)value);
            value = value * (rowIndex - i) / (i+1);

        }
        return ans;
    }
}
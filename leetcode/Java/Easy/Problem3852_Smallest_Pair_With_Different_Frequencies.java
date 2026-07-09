import java.util.Arrays;
import java.util.HashMap;
import java.util.TreeMap;

public class Problem3852_Smallest_Pair_With_Different_Frequencies {
    public static void main(String[] args){
        Solution3852 s = new Solution3852();
        System.out.println(Arrays.toString(s.minDistinctFreqPair(new int[]{1,1,2,2,3,4})));
    }
}

class Solution3852 {
    public int[] minDistinctFreqPair(int[] nums) {
        HashMap<Integer, Integer> c = new HashMap<>();
        
        for (int i : nums) {
            c.put(i, c.getOrDefault(i, 0) + 1);
        }

        TreeMap<Integer, Integer> sorted = new TreeMap<>(c);

        int[] ans = {-1, -1};
        int freq = -1;

        for (int k : sorted.keySet()) {
            if (ans[0] == -1) {
                ans[0] = k;
                freq = sorted.get(k);
            } else {
                if (sorted.get(k) != freq) {
                    ans[1] = k;
                    return ans;
                }
            }
        }
        return new int[]{-1,-1};


    }
}
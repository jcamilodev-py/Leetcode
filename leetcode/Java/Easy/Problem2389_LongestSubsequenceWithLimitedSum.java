import java.util.Arrays;
import java.util.ArrayList;

public class Problem2389_LongestSubsequenceWithLimitedSum {
     public static void main(String[] args) {
        Solution2389 s = new Solution2389();
        System.out.println(Arrays.toString(s.answerQueries(new int[]{2,3,4,5}, new int[]{1})));
    }
}

class Solution2389 {
    public int bs(int[] p, int target) {
            int l = 0;
            int r = p.length;

            while (l < r) {
                int m = l + (r - l) / 2;

                if (p[m] <= target) {
                    l = m+1;
                } else {
                    r = m;
                }
            }
            return l;
        }
    public int[] answerQueries(int[] nums, int[] queries) {

        Arrays.sort(nums);
        int[] p = new int[nums.length];
        Arrays.fill(p, nums[0]);
        ArrayList<Integer> ans = new ArrayList<>();

        
        for (int i = 1; i < nums.length; i++) {
            p[i] = nums[i] + p[i-1];
        }
    
        for (int q : queries) {
            int value = bs(p, q);
            ans.add(value);

        }
        return ans.stream().mapToInt(Integer::intValue).toArray();

    }
}
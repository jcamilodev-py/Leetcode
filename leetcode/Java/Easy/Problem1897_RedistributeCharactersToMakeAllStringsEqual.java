import java.util.HashMap;
import java.util.Map;

public class Problem1897_RedistributeCharactersToMakeAllStringsEqual {
    public static void main(String[] args) {
        Solution1987 s = new Solution1987();
        System.out.println(s.makeEqual(new String[]{"a", "b"}));
    }
}

class Solution1987 {
    public boolean makeEqual(String[] words) {

        Map<Character, Integer> c = new HashMap<>();
        int n = words.length;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < words[i].length(); j++) {
                c.merge(words[i].charAt(j), 1, Integer::sum);
                
            }
        }
        for (int value : c.values()) {
            if (value % n != 0) {
                return false;
            } 
        }
        return true;

    }
}
import java.util.ArrayList;

public class Problem500_KeyboardRow {
    public static void main(String[] args) {
        Solution500 s = new Solution500();
        System.out.println(s.findWords(new String[]{"Hello","Alaska","Dad","Peace"}));
    }
}


class Solution500 {
    public String[] findWords(String[] words) {
        String r1 = "qwertyuiop";
        String r2 = "asdfghjkl";
        String r3 = "zxcvbnm";
        ArrayList<String> ans = new ArrayList<>();

        for (String i : words) {
            String w = i.toLowerCase();

            if (p(w, r1) ||
                p(w, r2) ||
                p(w, r3)) {
                    ans.add(i);
            }
        }
        return ans.toArray(new String[0]);

    }

    public boolean p (String w, String row) {
        for (char c : w.toCharArray()) {
            if (!row.contains(String.valueOf(c))) {
                return false;
            }
        }
        return true;
    }
}

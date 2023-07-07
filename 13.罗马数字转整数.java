/*
 * @lc app=leetcode.cn id=13 lang=java
 *
 * [13] 罗马数字转整数
 */

// @lc code=start
class Solution {
    public int romanToInt(String s) {
        int res = 0;
        for(int i = 0; i < s.length(); i ++) {
            char c = s.charAt(i);
            switch(c) {
                case 'I':
                    res += 1 * (i+1==s.length() || s.charAt(i+1) != 'V' && s.charAt(i+1) != 'X' ? 1 : -1);
                    break;
                case 'V':
                    res += 5;
                    break;
                case 'X':
                    res += 10 * (i+1==s.length() || s.charAt(i+1) != 'L' && s.charAt(i+1) != 'C' ? 1 : -1);
                    break;
                case 'L':
                    res += 50;
                    break;
                case 'C':
                    res += 100 * (i+1==s.length() || s.charAt(i+1) != 'D' && s.charAt(i+1) != 'M' ? 1 : -1);
                    break;
                case 'D':
                    res += 500;
                    break;
                case 'M':
                    res += 1000;
                    break;
            }
        }
        return res;
       
    }
    public static void main(String[] args) {
        new Solution().romanToInt("MCMXCIV");
        
    }
}
// @lc code=end


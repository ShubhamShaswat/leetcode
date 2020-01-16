class Solution {
    public int countCharacters(String[] words, String chars) {
        int[] table = new int[26];
        for (int i = 0; i < chars.length(); i++)
            table[chars.charAt(i) - 'a']++;
        int count = 0;
        for (String str : words) {
            if (canSpellWords(str, table)) count += str.length();
        }
        return count;
    }

    public boolean canSpellWords(String str, int[] table) {
        int[] tableCopy = new int[26];
        System.arraycopy(table, 0, tableCopy, 0, 26);
        for (int i = 0; i < str.length(); i++) {
            char wordChar = str.charAt(i);
            if (tableCopy[wordChar - 'a'] <= 0)
                return false;
            tableCopy[wordChar - 'a']--;
        }
        return true;
    }
}
class Solution {
    public boolean isValid(String s) {
        ArrayList<Character> a = new ArrayList<Character>();

        for(int i = 0; i < s.length(); i++){
            if(s.charAt(i) == ')')
                if(a.size() == 0 || a.get(a.size() - 1) != '(')
                    return false;
                else a.remove(a.size() - 1);
            if(s.charAt(i) == '(')
                a.add(s.charAt(i));

            if(s.charAt(i) == ']')
                if(a.size() == 0 || a.get(a.size() - 1) != '[')
                    return false;
                else a.remove(a.size() - 1);
            if(s.charAt(i) == '[')
                a.add(s.charAt(i));

            if(s.charAt(i) == '}')
                if(a.size() == 0 || a.get(a.size() - 1) != '{')
                    return false;
                else a.remove(a.size() - 1);
            if(s.charAt(i) == '{')
                a.add(s.charAt(i));               
        }

        if(a.size() == 0)
            return true;
        return false;    
    }
}
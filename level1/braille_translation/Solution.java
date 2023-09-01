package level1.braille_translation;

import java.util.HashMap;
import java.util.stream.Collectors;

public class Solution {

    public static String solution(String s) {
        return s.chars()
                .mapToObj(ch -> charToBraille((char) ch))
                .collect(Collectors.joining());
    }

    private static String charToBraille(char c) {
        String out = "";

        if (c >= 'A' && c <= 'Z') {
            out += BrailleDots.capitalMark;
            c = Character.toLowerCase(c);
        }

        out += BrailleDots.charToBrailleMap.get(String.valueOf(c));
        return out;
    }

    private final static class BrailleDots {
        private static final HashMap<String, String> charToBrailleMap;
        private static final String capitalMark = "000001";

        static {
            charToBrailleMap = new HashMap<>();
            charToBrailleMap.put(" ", "000000");
            charToBrailleMap.put("a", "100000");
            charToBrailleMap.put("b", "110000");
            charToBrailleMap.put("c", "100100");
            charToBrailleMap.put("d", "100110");
            charToBrailleMap.put("e", "100010");
            charToBrailleMap.put("f", "110100");
            charToBrailleMap.put("g", "110110");
            charToBrailleMap.put("h", "110010");
            charToBrailleMap.put("i", "010100");
            charToBrailleMap.put("j", "010110");
            charToBrailleMap.put("k", "101000");
            charToBrailleMap.put("l", "111000");
            charToBrailleMap.put("m", "101100");
            charToBrailleMap.put("n", "101110");
            charToBrailleMap.put("o", "101010");
            charToBrailleMap.put("p", "111100");
            charToBrailleMap.put("q", "111110");
            charToBrailleMap.put("r", "111010");
            charToBrailleMap.put("s", "011100");
            charToBrailleMap.put("t", "011110");
            charToBrailleMap.put("u", "101001");
            charToBrailleMap.put("v", "111001");
            charToBrailleMap.put("w", "010111");
            charToBrailleMap.put("x", "101101");
            charToBrailleMap.put("y", "101111");
            charToBrailleMap.put("z", "101011");
        }
    }
}
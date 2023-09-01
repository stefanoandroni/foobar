package please_pass_the_coded_messages;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;
import java.util.stream.Collectors;

public class Solution {

    public static int solution(int[] l) {
        List<Integer> module0List = new ArrayList<>();
        List<Integer> module1List = new ArrayList<>();
        List<Integer> module2List = new ArrayList<>();

        for (int i : l) {
            switch (i % 3) {
                case 0:
                    module0List.add(i);
                    break;
                case 1:
                    module1List.add(i);
                    break;
                case 2:
                    module2List.add(i);
                    break;
            }
        }

        Collections.sort(module0List);
        Collections.sort(module1List);
        Collections.sort(module2List);

        Integer remainder = (module1List.size() * 1 + module2List.size() * 2) % 3;

        switch (remainder) {
            case 0:
                break;
            case 1:
                if (module1List.size() > 0) { // - (1%3)=1
                    module1List.remove(0);
                } else if (module2List.size() > 1) { // - ((2*2)%3)=(4%3)=1
                    module2List.remove(0);
                    module2List.remove(0);
                } else {
                    return 0;
                }
                break;
            case 2:
                if (module2List.size() > 0) { // - (2%3)=2
                    module2List.remove(0);
                } else if (module1List.size() > 1) { // - ((2*1)%3)=2
                    module1List.remove(0);
                    module1List.remove(0);
                } else {
                    return 0;
                }
                break;
        }

        List<Integer> outList = new ArrayList<>();
        outList.addAll(module0List);
        outList.addAll(module1List);
        outList.addAll(module2List);
        Collections.sort(outList, Comparator.reverseOrder());

        if (outList.size() == 0) {
            return 0;
        }

        return Integer.parseInt(outList.stream()
                .map(Object::toString)
                .collect(Collectors.joining()));
    }
}
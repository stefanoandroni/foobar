package power_hungry;

import java.math.BigInteger;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Solution {
    public static String solution(int[] xs) {
        // BigInteger => +- 1000^50
        List<Integer> posNumbers = new ArrayList<>();
        List<Integer> negNumbers = new ArrayList<>();
        boolean containsZero = false;

        for (int x : xs) {
            if (x > 0) {
                posNumbers.add(x);
            } else if (x < 0) {
                negNumbers.add(x);
            } else {
                containsZero = true;
            }
        }

        BigInteger posProduct = posNumbers.stream()
                .map(BigInteger::valueOf)
                .reduce(BigInteger.ONE, BigInteger::multiply);

        BigInteger negProduct = negNumbers.stream()
                .map(BigInteger::valueOf)
                .reduce(BigInteger.ONE, BigInteger::multiply);

        if (negNumbers.size() > 1 && negNumbers.size() % 2 != 0) { // negNumbers.size() > 1 && negProduct.compareTo(BigInteger.valueOf(0)) < 0
            negProduct = negProduct.divide(BigInteger.valueOf(Collections.max(negNumbers)));
        }

        BigInteger sol;
        if (negNumbers.size() > 0 && posNumbers.size() > 0) {
            sol = negProduct.signum() > 0 ? negProduct.multiply(posProduct) : posProduct;
        } else if (negNumbers.size() == 0 && posNumbers.size() > 0) {
            sol = posProduct;
        } else { // (negNumbers.size() != 0 && posNumbers.size() == 0)
            sol = containsZero ? BigInteger.ZERO : negProduct;
        }

        return sol.toString();
    }

}
// Advent of Code 2025 - Day 6 Part 2: Cephalopod Math
// Numbers are read column-by-column, right-to-left within each problem
// Each column forms a number with most significant digit at top

import java.io.*;
import java.math.BigInteger;
import java.util.*;

public class Solution2 {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new FileReader("input"));
        List<String> lines = new ArrayList<>();
        String line;
        
        while ((line = reader.readLine()) != null) {
            lines.add(line);
        }
        reader.close();
        
        if (lines.isEmpty()) {
            System.out.println("No input");
            return;
        }
        
        // Find max line length
        int maxLen = 0;
        for (String l : lines) {
            if (l.length() > maxLen) maxLen = l.length();
        }
        
        // Pad all lines to same length
        List<String> paddedLines = new ArrayList<>();
        for (String l : lines) {
            StringBuilder sb = new StringBuilder(l);
            while (sb.length() < maxLen) sb.append(' ');
            paddedLines.add(sb.toString());
        }
        
        // Separate number lines from operator line
        List<String> numberLines = new ArrayList<>();
        String operatorLine = "";
        
        for (String l : paddedLines) {
            String trimmed = l.trim();
            if (trimmed.isEmpty()) continue;
            
            boolean isOpLine = true;
            for (char c : trimmed.toCharArray()) {
                if (c != '+' && c != '*' && c != ' ') {
                    isOpLine = false;
                    break;
                }
            }
            
            if (isOpLine) {
                operatorLine = l;
            } else {
                numberLines.add(l);
            }
        }
        
        // Find problem boundaries (columns that contain content)
        List<int[]> problems = new ArrayList<>();
        boolean inProblem = false;
        int problemStart = 0;
        
        for (int col = 0; col < maxLen; col++) {
            boolean columnEmpty = true;
            for (String nl : numberLines) {
                if (col < nl.length() && nl.charAt(col) != ' ') {
                    columnEmpty = false;
                    break;
                }
            }
            
            if (!columnEmpty && !inProblem) {
                problemStart = col;
                inProblem = true;
            } else if (columnEmpty && inProblem) {
                problems.add(new int[]{problemStart, col - 1});
                inProblem = false;
            }
        }
        if (inProblem) {
            problems.add(new int[]{problemStart, maxLen - 1});
        }
        
        BigInteger grandTotal = BigInteger.ZERO;
        
        for (int[] prob : problems) {
            int startCol = prob[0];
            int endCol = prob[1];
            
            // For Part 2: Read columns RIGHT-TO-LEFT
            // Each column that has digits forms a number (top digit = most significant)
            List<BigInteger> numbers = new ArrayList<>();
            
            // Process columns from RIGHT to LEFT within this problem
            for (int col = endCol; col >= startCol; col--) {
                StringBuilder numStr = new StringBuilder();
                
                // Read digits from TOP to BOTTOM (most significant to least significant)
                for (String nl : numberLines) {
                    if (col < nl.length()) {
                        char c = nl.charAt(col);
                        if (Character.isDigit(c)) {
                            numStr.append(c);
                        }
                    }
                }
                
                // If this column had any digits, it forms a number
                if (numStr.length() > 0) {
                    numbers.add(new BigInteger(numStr.toString()));
                }
            }
            
            // Get operator
            int endIdx = Math.min(endCol + 1, operatorLine.length());
            int startIdx = Math.min(startCol, operatorLine.length());
            String op = operatorLine.substring(startIdx, endIdx).trim();
            
            // Calculate result
            BigInteger result;
            if (op.equals("+")) {
                result = BigInteger.ZERO;
                for (BigInteger n : numbers) {
                    result = result.add(n);
                }
            } else {
                result = BigInteger.ONE;
                for (BigInteger n : numbers) {
                    result = result.multiply(n);
                }
            }
            
            grandTotal = grandTotal.add(result);
        }
        
        System.out.println("Grand Total: " + grandTotal);
    }
}

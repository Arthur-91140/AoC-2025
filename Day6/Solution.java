// Advent of Code 2025 - Day 6: Cephalopod Math
// Solution in Java

import java.io.*;
import java.math.BigInteger;
import java.util.*;

public class Solution {
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
        
        // Find problem boundaries
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
            
            // Extract numbers from this problem
            List<BigInteger> numbers = new ArrayList<>();
            
            for (String nl : numberLines) {
                int endIdx = Math.min(endCol + 1, nl.length());
                int startIdx = Math.min(startCol, nl.length());
                if (startIdx >= nl.length()) continue;
                
                String substring = nl.substring(startIdx, endIdx);
                
                // Parse numbers
                StringBuilder numStr = new StringBuilder();
                for (char c : substring.toCharArray()) {
                    if (Character.isDigit(c)) {
                        numStr.append(c);
                    } else if (numStr.length() > 0) {
                        numbers.add(new BigInteger(numStr.toString()));
                        numStr = new StringBuilder();
                    }
                }
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

public class javafunc2 {
    static int getCountofWords(String input) {
        if (input == null || input.isEmpty()) {
            return 0;
        }

        int countOfWords = 1; // Start with 1 for the first word
        boolean inWord = false;

        for (int index = 0; index < input.length(); index++) {
            char oneChar = input.charAt(index);
            if (oneChar == ' ' || oneChar == '\n' || oneChar == '\t') {
                if (inWord) {
                    countOfWords++;
                    inWord = false;
                }
            } else {
                inWord = true;
            }
        }

        // Handle case where string is all whitespace
        if (!inWord) {
            countOfWords--;
        }

        return countOfWords;
    }
    public static void main(String[] args) {
        String testString = "Hello, this is a test string.";
        int wordCount = getCountofWords(testString);
        System.out.println("Word count: " + wordCount);
        }
    }
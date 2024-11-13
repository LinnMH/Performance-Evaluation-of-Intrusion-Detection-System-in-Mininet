package preprocessing;

import java.io.*;

public class CSVUtil {

    /**
     * Combines all CSV files in the specified folder into a single output file
     *
     * @param inputFolder  Path to the input folder containing CSV files
     * @param outputFile   Path to the output file
     * @throws IOException If an error occurs during file reading or writing
     */
    public static void combineFolder(String inputFolder, String outputFile) throws IOException {
        File folder = new File(inputFolder);
        File[] files = folder.listFiles((dir, name) -> name.toLowerCase().endsWith(".csv"));

        if (files == null || files.length == 0) {
            System.out.println("No CSV files found in the directory.");
            return;
        }

        try (BufferedWriter writer = new BufferedWriter(new FileWriter(outputFile))) {
            boolean headerWritten = false;

            for (File file : files) {
                try (BufferedReader reader = new BufferedReader(new FileReader(file))) {
                    String line;
                    boolean isFirstLine = true;

                    while ((line = reader.readLine()) != null) {
                        // Skip header line (unless it's the first file)
                        if (isFirstLine) {
                            isFirstLine = false;
                            if (headerWritten) continue;
                            headerWritten = true;
                        }
                        writer.write(line);
                        writer.newLine();
                    }
                }
            }
        }
        System.out.println("Finished combining CSV files into " + outputFile);
    }
}

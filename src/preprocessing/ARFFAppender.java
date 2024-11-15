package preprocessing;

import java.io.*;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class ARFFAppender {

    public static void main(String[] args) {
        String dosFilePath = "D:/bowen/CS-775/project/dataset/DoS.arff";
        String ids2017FilePath = "D:/bowen/CS-775/project/dataset/IDS2017_train_filtered_noDoS.arff";

        try {
            // Step 1: Load 20% of the DoS data
            System.out.println("Loading 20% of DoS data from DoS.arff...");
            List<String> dosData = loadArffData(dosFilePath);
            List<String> dosSample = sampleData(dosData, 0.2);
            System.out.println("Number of DoS samples selected: " + dosSample.size());

            // Step 2: Load IDS2017 data
            System.out.println("Loading IDS2017 data from IDS2017_train_filtered.arff...");
            List<String> ids2017Data = loadArffData(ids2017FilePath);
            System.out.println("IDS2017 data loaded successfully.");

            // Step 3: Append DoS samples to IDS2017 data
            System.out.println("Appending DoS samples to IDS2017 data...");
            ids2017Data.addAll(dosSample);

            // Step 4: Overwrite IDS2017_train_filtered.arff with appended data
            System.out.println("Saving the appended data back to IDS2017_train_filtered.arff...");
            saveArffData(ids2017FilePath, ids2017Data);
            System.out.println("Data appended successfully to 'IDS2017_train_filtered.arff'.");

        } catch (IOException e) {
            System.out.println("An error occurred: " + e.getMessage());
        }
    }

    // Loads ARFF data and returns lines as a List of Strings
    private static List<String> loadArffData(String filePath) throws IOException {
        List<String> data = new ArrayList<>();
        boolean isDataSection = false;
        try (BufferedReader reader = new BufferedReader(new FileReader(filePath))) {
            String line;
            while ((line = reader.readLine()) != null) {
                data.add(line);
                if (line.trim().equals("@data")) {
                    isDataSection = true;
                } else if (isDataSection) {
                    data.add(line);
                }
            }
        }
        return data;
    }

    // Selects a sample of data lines based on the specified fraction
    private static List<String> sampleData(List<String> data, double fraction) {
        List<String> sample = new ArrayList<>();
        Random random = new Random();
        for (String line : data) {
            if (random.nextDouble() < fraction) {
                sample.add(line);
            }
        }
        return sample;
    }

    // Saves the appended data back to the original ARFF file
    private static void saveArffData(String filePath, List<String> data) throws IOException {
        try (BufferedWriter writer = new BufferedWriter(new FileWriter(filePath))) {
            for (String line : data) {
                writer.write(line);
                writer.newLine();
            }
        }
    }
}

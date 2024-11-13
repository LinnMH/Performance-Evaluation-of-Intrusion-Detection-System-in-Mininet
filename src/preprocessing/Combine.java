package preprocessing;

public class Combine {

    public static void main(String[] args) throws Exception {
        // Correct the method call here to match the defined method name
        combineCSVFile("D:\\bowen\\CS-775\\project\\dataset\\test", "D:\\bowen\\CS-775\\project\\dataset\\test\\Combined.csv");
    }

    // Ensure the method name matches what is being called in main
    public static void combineCSVFile(String inputFolder, String outputFile) throws Exception {
        CSVUtil.combineFolder(inputFolder, outputFile);
        System.out.println("Finished combining CSV files");
    }
}

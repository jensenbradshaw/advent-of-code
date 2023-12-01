import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class day1 {
    public static void main(String[] args) {
        try {
            File myObj = new File("/mnt/c/Users/Jensen/git/advent-of-code/23/day1.txt");
            Scanner myReader = new Scanner(myObj);
            char firstInt;
            char lastInt;
            String calibrationValue;
            int runningTotal = 0;
            while (myReader.hasNextLine()) {
                String data = myReader.nextLine();
                System.out.println(data);
                firstInt = Character.MIN_VALUE;
                lastInt = Character.MIN_VALUE;
                calibrationValue = "";
                for (int i = 0; i < data.length(); i++) { // doesn't work for odd numbered inputs
                    if ((firstInt == Character.MIN_VALUE ) && Character.isDigit(data.charAt(i))) {
                        firstInt = data.charAt(i);
                    }    
                    if ((lastInt == Character.MIN_VALUE ) && Character.isDigit(data.charAt(data.length()-1-i))) {
                        lastInt = data.charAt(data.length()-1-i);
                    }
                } 
                calibrationValue = new String(new char[] { firstInt, lastInt});
                System.out.println(calibrationValue);
                runningTotal = runningTotal + Integer.parseInt(calibrationValue);
            }
            myReader.close();
            System.out.println(runningTotal);
        } catch (FileNotFoundException e) {
            System.out.println("An error ocurred.");
            e.printStackTrace();
        }
    }
}
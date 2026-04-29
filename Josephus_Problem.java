import java.util.Scanner;

public class Josephus_Problem
{
	public static void main(String[] args) {
	    	    Scanner sc = new Scanner(System.in);
	    	    int anzahl =0;
	    System.out.println("Sie sitzen im Kreis uns jeder Zweite wird ausgesiebt.");
	    System.out.println("Wer am Schluss übrig bleibt gewinnt.Sie suchen den besten Sitzplatz.");
		System.out.print("Geben Sie die Anzahl der Teilnehmer an: ");
		anzahl = sc.nextInt();
		double a=(Math.log(anzahl) / Math.log(2));
		int b=(int)Math.floor(a);
		int sitzplatz = 2*anzahl-(int) (2*Math.pow(2, b)-1);
		
		System.out.print("Der beste Sitzplatz ist: "+sitzplatz);
		sc.close();
		
		
	}
}
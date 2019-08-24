
import java.util.Scanner;
import java.util.Random;
public class testingJava{
	public static void main(String args[])
	{
		Scanner sc = new Scanner(System.in);
		Random rand = new Random();
		int game[][] = new int[4][4];
		int tile[] = new int[2];
		tile[0] = 2;
		tile[1] = 4;
		for(int i = 0; i<4; i++)
		{
			for(int j = 0; j<4; j++)
			{
				game[i][j] = sc.nextInt();
			}
		}
		int flag = 0;
		while(flag==0)
		{
			int i = rand.nextInt(4);
			int j = rand.nextInt(4);
			if(game[i][j]==0)
			{
				int x = tile[rand.nextInt(2)];
				System.out.print(j);
				System.out.print(" ");
				System.out.println(i);
				System.out.println(x);
				flag = 1;
			}
		}
		
	}
}
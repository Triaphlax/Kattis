using System;

namespace Kattis
{
    public class QualityOfLife
    {
        public static void Solve()
        {
            int lines = Convert.ToInt32(Console.ReadLine());
            int runningTotal = 0;
            for (int i = 0; i < lines; i++)
            {
                string input = Console.ReadLine();
                input = input.Trim('.');
                string[] values = input.Split(' ');
                runningTotal += Convert.ToInt32(values[0]) * Convert.ToInt32(values[1]);
            }
            Console.WriteLine(runningTotal / 10);
        }
    }
}

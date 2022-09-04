using System;

namespace Kattis
{
    public static class Sibice
    {
        public static void Solve()
        {
            int[] settings = Array.ConvertAll(Console.ReadLine().Split(' '), line => int.Parse(line));
            int nofMatches = settings[0];
            int xDim = settings[1];
            int yDim = settings[2];
            double maxLength = Math.Sqrt(Math.Pow(xDim, 2) + Math.Pow(yDim, 2));

            for (int i = 0; i < nofMatches; i++)
            {
                int matchLength = int.Parse(Console.ReadLine());
                if(matchLength <= maxLength)
                    Console.WriteLine("DA");
                else
                    Console.WriteLine("NE");
            }
        }
    }
}
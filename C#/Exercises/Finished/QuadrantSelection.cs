using System;

namespace Kattis
{
    public class QuadrantSelection
    {
        public static void Solve()
        {
            string xStr = Console.ReadLine();
            string yStr = Console.ReadLine();

            int quadrant = 0;
            quadrant = Convert.ToInt32(yStr) > 0 ? 1 : -4;
            quadrant += Convert.ToInt32(xStr) > 0 ? 0 : 1;
            quadrant = Math.Abs(quadrant);

            Console.WriteLine(quadrant);
        }
    }
}
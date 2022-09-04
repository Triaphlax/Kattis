using System.Collections.Generic;

namespace Kattis
{
    public static class PickUpSticks
    {
        public static void Solve()
        {
        }

        public static void toposort(Dictionary<int, int[]> graph, Dictionary<int, bool> visited, int start, Stack<int> resultStack)
        {
            var stack = new Stack<int>();

            while(stack.Count != 0)
            {
                int node = stack.Pop();

                foreach(int neighbor in graph[node])
                {
                    stack.Push(neighbor);
                }


            }
        }

        public static bool checkNoCycles(Dictionary<int, int[]> graph)
        {
            var stack = new Stack<int>();
            var leftToVisit = new HashSet<int>(graph.Keys);
            while(leftToVisit.Count != 0)
            {
                stack.Push(leftToVisit.);
                while(stack.Count != 0)
                {
                    int node = stack.Pop();

                    if (visited.Contains(node))
                    {
                        
                    }
                    foreach(int neighbor in graph[node])
                    {
                        stack.Push(neighbor);
                    }


                }
            }

            return visited;
        }
    }
}
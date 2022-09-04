using System;
using System.Collections.Generic;

// This gives a run-time error on Kattis for some reason

namespace Kattis
{
    public class Node
    {
        public int number { get; }
        int nofInitialPartners, nofCurrentPartners;
        public bool inEU { get; set; }
        public bool wantsToLeave { get; set; }
        public Dictionary<int, bool> partners { get; }

        public Node(int number)
        {
            this.number = number;
            this.partners = new Dictionary<int, bool>();
            this.nofInitialPartners = -1;
            this.nofCurrentPartners = -1;
            this.inEU = true;
            this.wantsToLeave = false;
        }

        public void AddPartner(int partner)
        {
            this.partners[partner] = true;
        }

        public void FinalizeNode()
        {
            this.nofInitialPartners = this.partners.Count;
            this.nofCurrentPartners = this.partners.Count;
        }

        public void RemovePartner(int partner)
        {
            this.partners[partner] = false;
            this.nofCurrentPartners -= 1;
            if (this.nofInitialPartners - this.nofCurrentPartners >= (nofInitialPartners - 1) / 2 + 1 && !this.wantsToLeave)
            {
                this.wantsToLeave = true;
            }
        }

        public void Leave()
        {
            this.inEU = false;
        }
    }

    public static class Brexit
    {
        public static void Solve()
        {
            int[] settings = Array.ConvertAll(Console.ReadLine().Split(' '), s => int.Parse(s));
            int nofCountries = settings[0];
            int nofTradingPartnerships = settings[1];
            int homeCountry = settings[2];
            int firstCountryToLeave = settings[3];

            Dictionary<int, Node> nodeDict = new Dictionary<int, Node>();

            for (int country = 1; country <= nofCountries; country++) // countries are 1-indexed
            {
                nodeDict[country] = new Node(country);
            }

            for (int lol = 0; lol < nofTradingPartnerships; lol++)
            {
                int[] partnershipSettings = Array.ConvertAll(Console.ReadLine().Split(' '), s => int.Parse(s));
                Node node1 = nodeDict[partnershipSettings[0]];
                Node node2 = nodeDict[partnershipSettings[1]];
                node1.AddPartner(node2.number);
                node2.AddPartner(node1.number);
            }

            foreach (Node node in nodeDict.Values)
            {
                node.FinalizeNode();
            }

            var queue = new Queue<int>();
            queue.Enqueue(firstCountryToLeave);
            nodeDict[firstCountryToLeave].wantsToLeave = true;
            while (queue.Count != 0)
            {
                int currentCountryNumber = queue.Dequeue();
                Node currentCountryNode = nodeDict[currentCountryNumber];

                if (!currentCountryNode.inEU)
                {
                    continue;
                }

                foreach (var partnerDetails in currentCountryNode.partners)
                {
                    if (partnerDetails.Value)
                    {
                        Node partnerNode = nodeDict[partnerDetails.Key];
                        partnerNode.RemovePartner(currentCountryNode.number);
                        currentCountryNode.RemovePartner(partnerNode.number);
                        if (partnerNode.wantsToLeave)
                        {
                            queue.Enqueue(partnerNode.number);
                        }
                    }
                }

                currentCountryNode.Leave();
            }

            if (nodeDict[homeCountry].inEU)
            {
                Console.WriteLine("stay");
            }
            else
            {
                Console.WriteLine("leave");
            }

        }
    }
}
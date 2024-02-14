﻿using System;

namespace FishTank
{
    class Program
    {
        static void Main(string[] args)
        {
            int length = int.Parse(Console.ReadLine());
            int width = int.Parse(Console.ReadLine());
            int height = int.Parse(Console.ReadLine());
            double percent = double.Parse(Console.ReadLine());

            double volume = (length * width * height) * 0.001;
            double volumeFull = ((double)percent / 100) * volume;

            double volumeLeft = volume - volumeFull;

            Console.WriteLine(volumeLeft);
        }
    }
}
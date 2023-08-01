using System;
using System.Threading;

public class SimpleThreadExample
{
    private bool stopTimer = false;

    public void StartMultipleThread()
    {
        DateTime startTime = DateTime.Now;

        // Timer thread
        Thread timerThread = new Thread(() =>
        {
            while (!stopTimer)
            {
                Thread.Sleep(1000);
                TimeSpan elapsedTime = DateTime.Now - startTime;
                Console.WriteLine("Time elapsed: {0} seconds", elapsedTime.TotalSeconds);
            }
        });

        // Your existing threads
        Thread t1 = new Thread(() =>
        {
            int numberOfSeconds = 0;
            while (numberOfSeconds < 5)
            {
                Thread.Sleep(1000);
                numberOfSeconds++;
            }
            Console.WriteLine("I ran for 5 seconds");
        });

        Thread t2 = new Thread(() =>
        {
            int numberOfSeconds = 0;
            while (numberOfSeconds < 8)
            {
                Thread.Sleep(1000);
                numberOfSeconds++;
            }
            Console.WriteLine("I ran for 8 seconds");
        });

        // Parameterized thread
        Thread t3 = new Thread(p =>
        {
            int numberOfSeconds = 0;
            while (numberOfSeconds < Convert.ToInt32(p))
            {
                Thread.Sleep(1000);
                numberOfSeconds++;
            }
            Console.WriteLine("I ran for {0} seconds", numberOfSeconds);
        });

        // Start all threads
        timerThread.Start();
        t1.Start();
        t2.Start();
        t3.Start(20);

        // Wait for t1, t2, and t3 to finish
        t1.Join();
        t2.Join();
        t3.Join();

        // Stop the timer thread
        stopTimer = true;
        timerThread.Join();

        Console.WriteLine("All Threads Exited in {0} seconds", (DateTime.Now - startTime).TotalSeconds);
    }
}

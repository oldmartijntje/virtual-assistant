using System;
using System.Threading;

public class SharedDataExample
{
    private int henk = 0;
    private int cheese = 0;
    private int calls = 0;
    private int last = 0;
    private bool stop = false;
    private object lockObject = new object();
    private Random random = new Random();
    private ManualResetEvent stopEvent = new ManualResetEvent(false);

    public void Start()
    {
        Thread thread1 = new Thread(() =>
        {
            while (!stop)
            {
                lock (lockObject)
                {
                    if (henk != last)
                    {
                        last = henk;
                        Console.WriteLine("Thread 1 has access");
                        if (henk > 5)
                        {
                            cheese++;
                            Console.WriteLine("Henk: " + henk + ", Cheese: " + cheese + ", Calls: " + calls);
                        }
                    }
                        
                }
            }
        });

        Thread thread2 = new Thread(() =>
        {
            Console.WriteLine("Thread 2 has started");
            while (!stop)
            {
                lock (lockObject)
                {
                    Console.WriteLine("Thread 2 has access");
                    henk = random.Next(1, 11);
                    calls++;

                    if (cheese > 9)
                    {
                        stopEvent.Set(); // Signal the other threads to stop
                    }
                }

                Thread.Sleep(1000);
            }
        });

        Thread thread3 = new Thread(() =>
        {
            stopEvent.WaitOne(); // Wait until the signal is received
            Console.WriteLine("Yeet Lasagna");

            lock (lockObject)
            {
                Console.WriteLine("Thread 3 has access");
                stop = true;
            }

            // Stop all threads
            thread1.Join();
            thread2.Join();
        });

        thread1.Start();
        thread2.Start();
        thread3.Start();

        // Wait for threads to finish (in this example, they run indefinitely)
        // You can add logic here to stop the threads based on certain conditions if needed.
    }

    
}
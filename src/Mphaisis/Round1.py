"""
//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    private static final ReadWriteLock obj = new ReadWriteLock();
    private static int num = 0;

    public static void main(String[] args) {


        //read 1
        Thread reader1 = new Thread(() ->
        {
            try {
                obj.lockRead();
                System.out.println("reader 1 reading : " + num);
                Thread.sleep(1000);
                System.out.println("reader 1 completed reading");
                obj.unlockRead();

            } catch (Exception e) {
                e.printStackTrace();
            }
        });
        //read2
        Thread reader2 = new Thread(() ->
        {
            try {
                obj.lockRead();
                System.out.println("reader 2 reading :" +num);
                Thread.sleep(1000);
                System.out.println("reader 2 completed reading");
                obj.unlockRead();

            } catch (Exception e) {
                e.printStackTrace();
            }
        });

        Thread reader3 = new Thread(() ->
        {
            try {
                obj.lockRead();
                System.out.println("reader 3 reading :" +num);
                Thread.sleep(1000);
                System.out.println("reader 3 completed reading");
                obj.unlockRead();

            } catch (Exception e) {
                e.printStackTrace();
            }
        });

        Thread write1 = new Thread(() ->
        {
            try {
                obj.lockWrite();
                num++;
                System.out.println("writer 1 update num :"+num);
                Thread.sleep(1000);
                System.out.println("writer  1 finishes writing ");
                obj.unlockWrite();

            } catch (Exception e) {
                e.printStackTrace();
            }
        });

        Thread write2 = new Thread(() ->
        {
            try {
                obj.lockWrite();
                num++;
                System.out.println("writer 2 update num :"+num);
                Thread.sleep(1000);
                System.out.println("writer 2 finishes writing ");
                obj.unlockWrite();

            } catch (Exception e) {
                e.printStackTrace();
            }
        });

        write1.start();

        reader1.start();
        reader2.start();


        write2.start();


        reader3.start();











    }
        /*

        Implement your own Read-Write Lock (without using ReentrantReadWriteLock)
        (Multiple readers can read simultaneously,
        Only one writer can write at a time, No readers allowed while writing)


         */


}

        class ReadWriteLock{

              private int readers=0;
              private boolean write=false;

              public synchronized void lockRead() throws InterruptedException
              {
                  while(write)
                  {
                      wait();
                  }
                  readers++;
              }

              public synchronized void unlockRead(){
                  readers--;
                  notifyAll();
              }

              public synchronized void lockWrite() throws InterruptedException{
                  while(readers>0 || write)
                  {
                      wait();
                  }
                  write=true;
              }

              public synchronized void unlockWrite()
              {
                  write=false;
                  notifyAll();
              }
        }

second highest salary department wise using sql

config in kafka
consumer lag
admin bases role config in spring security
CQRS . cors, saga, transction managerment in microsrvices, daul write problem
problem you handle in the database

"""
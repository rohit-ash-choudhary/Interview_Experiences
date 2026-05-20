""""
//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) {
        //TIP Press <shortcut actionId="ShowIntentionActions"/> with your caret at the highlighted text
        // to see how IntelliJ IDEA suggests fixing it.
        //System.out.printf("Hello and welcome!");
/*

You are given an array people where people[i] is the weight of the ith person,
and an infinite number of boats where each boat can carry a maximum weight of limit.
Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.

Return the minimum number of boats to carry every given person.


Example 1:

Input: people = [1,2], limit = 3
Output: 1
Explanation: 1 boat (1, 2)
Example 2:

Input: people = [3,2,2,1], limit = 3
Output: 3
Explanation: 3 boats (1, 2), (2) and (3)
Example 3:

Input: people = [3,5,3,4], limit = 5
Output: 4
Explanation: 4 boats (3), (3), (4), (5)

 */

        int[] arr={2,1,3,2};
        int limit=3;
         Main obj=new Main();
       int numofboat=  obj.numberofBoat(arr,limit);
        System.out.println("number of boat  " +numofboat);
    }

    /*

    Example 1:

Input: people = [1,2], limit = 3
Output: 1
Explanation: 1 boat (1, 2)
Example 2:

Input: people = [3,2,2,1], limit = 3
Output: 3
Explanation: 3 boats (1, 2), (2) and (3)
Example 3:

Input: people = [3,5,3,4], limit = 5
Output: 4
Explanation: 4 boats (3), (3), (4), (5)

     */

    public int numberofBoat(int[] arr,int limit)
    {
        int n=arr.length;
        boolean[] used=new boolean[n]; //same of arr
        int number_of_boats=0;  //0
        for (int i = 0; i < n; i++) {
            if(used[i])
            {
                continue;
            }
            //[3,5,3,4]
            used[i]=true; //used first time
            for (int j = n-1; j > i; j--) {
                if(!used[j] && arr[i]+arr[j]<=limit)
                {
                    used[j]=true;
                    break;

                }

            }
            number_of_boats++;
        }

        return number_of_boats;
    }

}


Microservices vs monoliths ,
how app is up or not
how to choose sql or non sql db
how to increase responce type
solid priniciple
how spring works
bean
how enable bean config works
about project
design pattern are you used
how to optimize query
large scale db
how to scale system



"""
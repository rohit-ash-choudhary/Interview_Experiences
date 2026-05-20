"""

Intro

JWT VS OATH 2.0

import java.util.HashSet;
import java.util.List;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) {
        //TIP Press <shortcut actionId="ShowIntentionActions"/> with your caret at the highlighted text
        // to see how IntelliJ IDEA suggests fixing it.
   /*     Given an integer array nums, return true if any
        value appears at least twice in the array,
        and return false if every element is distinct.
        Input: nums = [1, 2, 3, 1]  ,[6,5,6,4]
        Output: true

        Input: nums = [1, 2, 3]
        Output: false */

        int[] arr={1,2,3,1};
        int[] arr2={1,2,3};
        Main obj=new Main();
        boolean result=obj.repeatElementOpti(arr);
        boolean result2=obj.repeatElementOpti(arr2);
        System.out.println("arra   : "+ result);
        System.out.println("array2  :"+result2);

        String s="abcddabac";
        int stringresult= obj.lenlongessuSet(s);
        System.out.println(stringresult);






    }

     //brute  :

  /*  public boolean repeatedElemenr(arr) {
        for(int i=0;i<arr.length();i++)
        {
            int flag=0;
            for(int j=i+1;j<arr.length();i++) {
                if (arr[i] == arr[j]) {
                    flag = 1;
                    break;
                }
            }
        }  /n2
        if(flag==1)
        {
            return  true;

        }

        return false;

    } */
    public   boolean repeatElementOpti(int[] arr)
    {
        HashSet<Integer> set=new HashSet<>();
        for(int num: arr)
        {
            if(set.contains(num))
            {
                return true;
            }
            set.add(num);
        } //n
        return false;
    }


  /*  public int lenlongessub(String str)
    {
        int maxlength=0;
        int i=0;
        for (int i = 0; i <str.length() ; i++) { //1-n
            String temp="";
            for (int j = i; j <str.length() ; j++) { //1-n

                char ch=str.charAt(j);

                if(temp.indexOf(ch)!=-1)  //string not -1// n
                {
                    break;
                }
                temp+=ch;
                maxlength=Math.max(maxlength,temp.length());
            }
        }
        return maxlength;
    }*/

    public int lenlongessuSet(String str)
    {
       //"abcddabac"
        HashSet<Character> setchar=new HashSet<>();
        int maxlength=0;
        int left=0;
        for (int right = 0; right <str.length() ; right++) { //1-n

                char chval=str.charAt(right);

                if(setchar.contains(chval))  //return/a
                {
                    setchar.remove(str.charAt(left));
                    left++;
                }
                setchar.add(chval);
                maxlength=Math.max(maxlength,right-left+1);
            }
        return maxlength;
        }


}

//Hasmap :Hashset :

/*

Given a string, S. Find the length of the longest substring without repeating characters.
Input:
 S = "abcddabac"  #abcd #4 temp=abcd temp=4,
 S= "abcabcdeabdefabc"  #3,5
Output:
 4

Input:
 S = "aaabbbccc"   #ab,bc
Output:
 2
 */




"""
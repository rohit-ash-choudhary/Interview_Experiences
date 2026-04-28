"""

class :

i
2 method :

method a calling method b : method a using @transction annotation in that
if method b throw exception then what method a responce

what if we @componet at place of @repository and @service annotation at place og @componet

array list vs linklist
underlying data structure
hashset

hashamap working(in which hashcollison)

sleep vs wait method

execute service
class loader

memory area in jvm

java 8 to java 17 feature

equals and == method

how handle excpetion in spring app , how to other then @controller advice

where you used the ayschrnoud method in spring boot

sql : give the data from table where employee age is greate then 60:
dob as column no age column present


bean vs component , how you read properties in your spring project
like spring.mail.server.mail

where we testtemplate and httpclient why httpclient is better
if which is better in any one better give functionlity
get a mircoservices desing follow from one to end


why serialize and deserilization used

runtime exception



code :

anagram for spring:
mport java.lang.reflect.Array;
import java.util.*;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) {

        //[[eat, tea, ate], [tan, nat], [bat]]

        String[] str={"eat", "tea", "ate", "tan", "nat", "bat"};

        List<List<String>> output=GroupAna(str);
        System.out.println(output);


    }

    public static List<List<String>> GroupAna(String[] args) {
        Map<String,List<String>> map=new HashMap<>();
        for(String words :args)
        {
            char[] chars=words.toCharArray();
            Arrays.sort(chars);
            String hashkey=new String(chars);

            if(!map.containsKey(hashkey))
            {
                map.put(hashkey,new ArrayList<>());
            }
            map.get(hashkey).add(words);
        }

        return new ArrayList<>(map.values());

    }
}

  aib, bia, iab
select * from employee where dob<sysdate-60*365;

N+1 problem
"""
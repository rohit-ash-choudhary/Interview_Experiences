""""


Write stream code for the person group bases on age by using stream and without stream both
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;
/*
Write stream code for the person group bases on age by using stream and without stream both
*/
//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) {
        //TIP Press <shortcut actionId="ShowIntentionActions"/> with your caret at the highlighted text
        // to see how IntelliJ IDEA suggests fixing it.
        //Person class - name,age ,city ,dob,id, gender
        // list of person - > group by the people bases on age.

        Person p1 = new Person("A", 25, "Delhi", "M");
        Person p2 = new Person("c", 56, "Delhi", "M");
        Person p3 = new Person("d", 34, "Delhi", "M");
        Person p4 = new Person("y", 34, "Delhi", "M");
        Person p5 = new Person("i", 25, "Delhi", "M");
        List<Person> lst = new ArrayList<>();
        lst.add(p1);
        lst.add(p2);
        lst.add(p3);
        lst.add(p4);
        lst.add(p5);
        Map<Integer, List<Person>> grpbyag=new HashMap<>();

        // Map<Integer, List<Person>> grpbyage =lst.stream().collect(Collectors.groupingBy(Person::getAge));
       // System.out.println(grpbyage);
       for(Person p: lst){
           int age=p.getAge();
           if(grpbyag.containsKey(age))
           {
               grpbyag.get(age).add(p);
           }
           else{
               List<Person> listp=new ArrayList<>();
               listp.add(p);
               grpbyag.put(age,listp);
           }
       }
        System.out.println(grpbyag);
    }
}

class  Person{

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Integer getAge() {
        return age;
    }

    public void setAge(Integer age) {
        this.age = age;
    }

    public String getCity() {
        return city;
    }

    public void setCity(String city) {
        this.city = city;
    }

    public String getGender() {
        return gender;
    }

    public void setGender(String gender) {
        this.gender = gender;
    }

    String name;
    Integer age;
    String city;
    String gender;

    public Person(String name, Integer age, String city, String gender) {
        this.name = name;
        this.age = age;
        this.city = city;
        this.gender = gender;
    }

    @Override
    public String toString() {
        return "Person{"+
                "name='"+name + '\'' +
                "age="+age + '\''  +
                "city="+city +'\'' +
                        "gender="+gender +'\'' + '}';

        }
    }

        //user 1 : rate limiter 10 times in 1 min  : payment api

-import java.util.HashMap;
import java.util.Map;

public class Test {

    public static void main(String[] args) {

        //user 1 : rate limiter 10 times in 1 min  : payment api

    }
}

class User{
    int count;

    public User(int count, long starttime, String userid) {
        this.count = count;
        this.starttime = starttime;
        Userid = userid;
    }

    long starttime;
    String Userid;


/*
10-2 --//
20-2
30-1
40-1
50-1
60-1
70-3
 */

}

class RateLimt{

    static final int count_limit=10;
    static final int window=60;

    static Map<String,User> map=new HashMap<>();

    public boolean allowedReq(String UserId) {
        long currentime = System.currentTimeMillis();
        if (!map.containsKey(UserId)) {
            map.put(UserId, new User(1, currentime, UserId));
            return true;
        }


       User userdata = map.get(UserId);
       /*
      currentime= 70
      stating =0
        */
        if (currentime-userdata.starttime<window)
        {
            if(userdata.count<count_limit)
            {
                userdata.count++;
                return  true;
            }
           else{
               return false;
            }
        }else{
            userdata.count=1;
            userdata.starttime=currentime;
            return true;
        }

    }






}

"""
"""

in user object sort based on the age then if age same then sort based on name
package Playlist;

import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;
import java.util.List;

public class test {
    public static void main(String[] args) {
        List<Employee> list=new ArrayList<>();
        Employee e=new Employee(1,"Rahul","Dev");
        Employee e1=new Employee(2,"Karan","Dev");
        Employee e2=new Employee(2,"aman","Dev");
        Employee e3=new Employee(1,"kirat","test");
        list.add(e);
        list.add(e1);
        list.add(e2);
        list.add(e3);

        Collections.sort(list,(emp1,emp2)->
                {
                    if(emp1.id!=emp2.id)
                    {
                        return emp1.id-emp2.id;
                    }
                    else {
                        return emp2.name.compareTo(emp1.name);
                    }
                });

        for(Employee et: list)
        {
            System.out.println(et);
        }
    }
    //shorting based on id if id equal if then name
}

class Employee{
    int id;
    String name;
    String designation;

    public Employee(int id, String name, String designation) {
        this.id = id;
        this.name = name;
        this.designation = designation;
    }

    @Override
    public String toString() {
        return id + " " + name + " " + designation;
    }
}
//rest a - third party -a db - > service b - db>
commit ; service db  ;

differnce between hashmap.sychroud method vs concurentHashmap
comparator and comparable difference
primary vs qualifier internal
how handle transction in hibernate
when a third party service write data to our db/app and then how we can we make sure this this
 sync or correct data that he write and hld and code level
 how much you notic period or serving
"""
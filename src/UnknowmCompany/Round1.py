""""import java.lang.reflect.Array;
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
"""
"""
/*
Find the frequency of elements repeating in this array
 [50,40, 50, 30, 40, 50, 30, 30,10,10]
Display the result as shown below;
30 - 3
50 - 3
10 - 2
40 - 2
 *///TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.

ublic class Main {
    public static void main(String[] args) {

        //Set<Integer> fre_set=new LinkedHashSet<>();
        HashMap<Integer,Integer> map=new HashMap<>();
        int[] arr={50,40, 50, 30, 40, 50, 30, 30,10,10};

        for (int num: arr) {
            map.put(num,map.getOrDefault(num,0)+1);

        }
        List<Map.Entry<Integer,Integer>> list=new ArrayList<>(map.entrySet());

        list.sort((a,b)-> {
                    if (!b.getValue().equals(a.getValue())) {
                        return b.getValue() - a.getValue();
                    }
                        return a.getKey() - b.getKey();

                }
        );


        for (Map.Entry<Integer,Integer> en: list)
        {
            System.out.println(en.getKey()+" -"+en.getValue());
        }

        /*for (int num :fre_set)
        {
            int count=0;
            for (int val:arr)
            {
                if(num==val)
                {
                    count+=1;
                }
            }
            System.out.println(num+ " - "+count);*/
        }



1. sql bases question joins
2. service bases question
3. how approach production issue
4. indepotency key
5. service baseed questions
6. hashmap working
7. immutable class
mostle hld scenrios level questions


#rejected
"""
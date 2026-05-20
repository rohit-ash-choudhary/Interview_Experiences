"""max second salary

off set and basic

emp and demp from two table
forgein key for emp table is depid
    key connection department id

minimum salary of emp
department wise


There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station.
You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique.

Input: gas = [1,2,3,4,5],
cost = [3,4,5,1,2]
Output: 3



total_tank=0;
currnt_tank_fuel=0;
int start_point=0


i to n
diff=gas[i]-cost[i]
total_tank=+diff;
currnt_tank_fuel+=diff

if(currnt_tank_fuel<0)
    {
        start_point=i+i;
currnt_tank_fuel=0;
}


if total_tank>=0:
    return start_point
else :
    -1


    0   -2   -2
    1   -2    -2
    2    -2   -2
    3    +3    3
    4    +3    6

Java 8 migration
Daemon thread
kafka
circuit braker

Migration from java 8 to java 11 """

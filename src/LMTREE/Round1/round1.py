"""


@RestController
@RequestMapping("/employee")
public class EmpController {


    @PostMapping(/create)
    public ResponceEntity<String> createEmployee(@RequestBody Employee emp)
    {

        @Autowrite
                //service class logic to employeeservi

         employeeservice.save(employee);
    }


    @Test
    void testcreareEmployee() throw expcetion {
        Employee emp=new Employee("1","Rohit","Developer");

        employee saveemp=employeeservice.save(employee);

        assertNotNull(saveemp);
        assertEquals("Rohit",saveemp.getName());
        assertEquals("1",saveemp.getId());
        assertEquals("Developer",saveemp.getDepartment());

    }
}
Spring, kafka, monolith microservices , why use interface
islocation level
eager fetching and proxy fetching ,n+1 problem

"""
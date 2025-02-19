#include "Admin.h"

Admin::Admin(string& name, int& salary):Human(name), salary(salary)
{
}

int Admin::getSalary()
{
    return salary;
}

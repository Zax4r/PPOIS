#pragma once
#include "Client.h"
class Admin:public Human
{
private:
	int salary;
public:
	Admin(string& name, int& salary);
	int getSalary();
};


#pragma once
#include"Combined.h"
#include <string>
using namespace std;
class Human
{
private:
	string name;
	int age;
public:
	Human(string name, int age);
	Human() {};
	string GetName();
};
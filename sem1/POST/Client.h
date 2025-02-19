#pragma once
#include "Human.h"
class Client :public Human
{
private:
	string telephone;
	string address;
public:
	Client(string name, int age, string telephone, string address);
	Client() {};
	string GetAddress();
};
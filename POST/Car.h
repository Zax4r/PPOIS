#pragma once
#include <string>
using namespace std;
class Car
{
protected:
	std::string name;
public:
	Car(const std::string& nam);
	virtual std::string GetName();
};


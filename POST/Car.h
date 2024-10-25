#pragma once
#include<string>
#include"PostWorker.h"
using namespace std;
class Car
{
protected:
	string name;
public:
	Car(const string& nam);
	virtual string GetName();
};

class MailCar : public Car
{
private:
	Driver driver;
public:
	MailCar(const string& nam, Driver& dr);
	MailCar() :Car("unnamed_car") {};

};


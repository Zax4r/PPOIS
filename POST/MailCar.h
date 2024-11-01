#pragma once
#include "Car.h"
#include "Driver.h"
class MailCar : public Car
{
private:
	Driver driver;
public:
	MailCar(const string& nam, Driver& dr);
	MailCar() :Car("unnamed_car") {};
};

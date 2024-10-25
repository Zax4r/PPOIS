#include "Car.h"

Car::Car(const string& nam) : name(nam)
{
	
}

string Car::GetName()
{
	return name;
}

MailCar::MailCar(const string& nam, Driver& dr)
	: Car(nam), driver(dr) 
{

}
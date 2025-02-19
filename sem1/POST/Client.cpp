#include "Client.h"

Client::Client(string name = "", int age = 0, string telephone1 = "", string address1 = "") :Human(name, age)
{
	telephone = telephone1;
	address = address1;
}

string Client::GetAddress()
{
	return address;
}
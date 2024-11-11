#include "InternetAddress.h"

InternetAddress::InternetAddress(string address)
{
	this->address = "https:" + address;
}

string InternetAddress::getAddress()
{
	return address;
}

#include "Building.h"

Building::Building(string& address): address(address)
{
}

string Building::getAddress()
{
    return address;
}
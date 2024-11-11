#include "Item.h"

Item::Item(int& id, string& name):id(id),name(name)
{
}

string Item::getName()
{
	return name;
}

int Item::getId()
{
	return id;
}

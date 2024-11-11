#pragma once
#include "Item.h"
class Clothing:public Item
{
private:
	int size;
public:
	Clothing(int& id, string& name, int& size);
	int getSize();
};


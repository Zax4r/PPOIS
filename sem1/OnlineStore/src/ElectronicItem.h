#pragma once
#include "Clothing.h"
class ElectronicItem : Item
{
private:
	bool warranty;
public:
	ElectronicItem(int& id, string& name, bool& warranty);
	bool getWarranty();
};


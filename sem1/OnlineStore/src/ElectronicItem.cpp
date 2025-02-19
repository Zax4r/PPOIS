#include "ElectronicItem.h"

ElectronicItem::ElectronicItem(int& id, string& name, bool& warranty):Item(id,name)
{
	this->warranty = warranty;
}

bool ElectronicItem:: getWarranty()
{
	return warranty;
}

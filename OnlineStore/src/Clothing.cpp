#include "Clothing.h"

Clothing::Clothing(int& id, string& name, int& size):Item(id,name)
{
	this->size = size;
}

int Clothing::getSize()
{
	return size;
}
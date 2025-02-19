#pragma once
#include "Store.h"
class Storage:public Building
{
private:
	vector<Item*> items;
public:
Storage(string& address);
	void addItem(Item* item);
	vector<Item*> getItems();
};


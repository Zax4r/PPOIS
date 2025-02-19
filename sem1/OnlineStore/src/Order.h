#pragma once
#include "ElectronicItem.h"
class Order
{
private:
	vector<Item*> items;
	int id;
public:
	Order(int& id);
	int getId();
	void addItem(Item*& temp);
	void removeItem(int& itemid);
	vector<Item*> getItems();
};


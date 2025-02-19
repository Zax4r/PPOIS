#include "Order.h"

Order::Order(int& id): id(id)
{
}

int Order::getId()
{
	return id;
}

void Order::addItem(Item*& temp)
{
	items.push_back(temp);
}

void Order::removeItem(int& itemid)
{
	for (int i = 0; i < items.size(); i++)
	{
		if (items[i]->getId() == itemid)
			items.erase(items.begin() + i);
	}
}

vector<Item*> Order::getItems()
{
	return items;
}

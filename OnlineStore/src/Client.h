#pragma once
#include "Human.h"
class Client:public Human
{
private:
	vector<Order> orders;
public:
	Client(string& name);
	void addOrder(Order& order);
	vector<Order> getOrders();
	void removeOrder(int id,int itemid);
	void addToOrder(Item* & item,int id);
};


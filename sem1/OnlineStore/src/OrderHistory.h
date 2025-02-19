#pragma once
#include "Storage.h"
class OrderHistory
{
protected:
	vector<Order> orders;
public:
	OrderHistory();
	void addOrder(Order& order);
	vector<Order> getOrders();
};


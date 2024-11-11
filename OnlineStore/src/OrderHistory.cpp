#include "OrderHistory.h"

OrderHistory::OrderHistory()
{
}

void OrderHistory::addOrder(Order &order)
{
	orders.push_back(order);
}

vector<Order> OrderHistory::getOrders()
{
	return orders;
}
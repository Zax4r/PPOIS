#include "Client.h"

Client::Client(string& name):Human(name)
{

}

void Client::addOrder(Order& order)
{
	orders.push_back(order);
}

vector<Order> Client::getOrders()
{
	return orders;
}



void Client::removeOrder(int id,int itemid)
{
	for (int i = 0; i < orders.size(); i++)
	{
		if (orders[i].getId() == id)
		{
			orders[i].removeItem(itemid);
			break;
		}			
	}
}

void Client::addToOrder(Item *&item, int id)
{
	for (int i = 0; i < orders.size(); i++)
	{
		if (orders[i].getId() == id)
		{
			orders[i].addItem(item);
			break;
		}			
	}
}

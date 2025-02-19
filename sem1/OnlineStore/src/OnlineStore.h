#pragma once
#include "InternetAddress.h"
class OnlineStore:public Store
{
private:
	vector<Client> clients;
	Storage storage;
	vector<Review> reviews;
	Admin admin;
	ComplitedOrdersHistory history;
	InternetAddress IntAddr;
public:
	OnlineStore(string name, Storage storage,Admin admin);
	void addClient(Client& client);
	void addReview(Review& review);
	void addItem(Item*& item);
	vector<Review> getReviews();
	vector<Client> getClients();
	vector<Item*> getItems();
};


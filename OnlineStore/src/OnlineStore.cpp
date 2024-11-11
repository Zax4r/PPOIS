#include "OnlineStore.h"

OnlineStore::OnlineStore(string name, Storage storage,Admin admin) :Store(name), storage(storage),admin(admin), IntAddr("home1")
{
	
}

void OnlineStore::addClient(Client& client)
{
	clients.push_back(client);
}

void OnlineStore::addReview(Review& review)
{
	reviews.push_back(review);
}

void OnlineStore::addItem(Item*& item)
{
	storage.addItem(item);
}

vector<Review> OnlineStore::getReviews()
{
    return reviews;
}

vector<Client> OnlineStore::getClients()
{
    return clients;
}

vector<Item *> OnlineStore::getItems()
{
    return storage.getItems();
}

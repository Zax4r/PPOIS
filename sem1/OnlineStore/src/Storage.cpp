#include "Storage.h"

void Storage::addItem(Item* item)
{
    items.push_back(item);
}

vector<Item*> Storage::getItems()
{
    return items;
}

Storage::Storage(string& address):Building(address)
{

}
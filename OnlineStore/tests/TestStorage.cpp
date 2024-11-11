
#include <gtest/gtest.h>
#include "OnlineStore.h"

TEST(StorageTest, AddItems) {
    string name="Storage1";
    Storage storage(name);
    int itemId = 1;
    string itemName = "Test Item";
    Item* item = new Item(itemId, itemName);
    
    storage.addItem(item);
    
    EXPECT_EQ(storage.getItems().size(), 1);
    
    delete item; 
}

TEST(StorageTest, GetItems) {
    string name="Storage1";
    Storage storage(name);
    int itemId = 1;
    string itemName = "Test Item";
    Item* item = new Item(itemId, itemName);
    
    storage.addItem(item);
    
    EXPECT_EQ(storage.getItems()[0]->getId(), itemId);
    
    delete item; 
}
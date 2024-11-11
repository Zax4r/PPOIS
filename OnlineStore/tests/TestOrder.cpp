
#include <gtest/gtest.h>
#include "OnlineStore.h"

TEST(OrderTest, AddItems) {
    int id = 1;
    Order order(id);
    
    int itemId = 2;
    string itemName = "Sample Item";
    Item* item = new Item(itemId, itemName);
    
    order.addItem(item);
    
    EXPECT_EQ(order.getItems().size(), 1);
    
    delete item; 
}

TEST(OrderTest, GetItems) {
    int id = 1;
    Order order(id);
    
    int itemId = 2;
    string itemName = "Sample Item";
    Item* item = new Item(itemId, itemName);
    
    order.addItem(item);
    
    EXPECT_EQ(order.getItems()[0]->getId(), itemId);
    
    delete item; 
}

TEST(OrderTest, RemoveItem) {
    int id = 1;
    Order order(id);
    
    int itemId = 2;
    string itemName = "Sample Item";
    Item* item = new Item(itemId, itemName);
    order.addItem(item);
    
    order.removeItem(itemId);
    
    EXPECT_EQ(order.getItems().size(), 0);
    
    delete item;  
}
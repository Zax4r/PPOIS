#include <gtest/gtest.h>
#include "OnlineStore.h"

TEST(ClientTest, AddOrder) {
    int orderId = 1;
    Order order(orderId);
    string clientName = "Test Client";
    Client client(clientName);
    client.addOrder(order);
    
    EXPECT_EQ(client.getOrders().size(), 1);
}

TEST(ClientTest, RemoveOrder) {
    int orderId = 1;
    Order order(orderId);
    string clientName = "Test Client";
    Client client(clientName);
    client.addOrder(order);
    
    int itemId = 2;
    string itemName = "Test Item";
    Item* item = new Item(itemId, itemName);
    client.addToOrder(item,orderId);
    client.removeOrder(orderId, itemId);
    EXPECT_EQ(client.getOrders()[0].getItems().size(), 0);

    delete item; 
}



TEST(ClientTest, RemoveItemFromOrder) {
    int orderId = 1;
    Order order(orderId);
    string clientName = "Test Client";
    Client client(clientName);
    client.addOrder(order);
    
    int itemId = 2;
    string itemName = "Test Item";
    Item* item = new Item(itemId, itemName);
    client.addToOrder(item,orderId);


    client.removeOrder(orderId, itemId+5);
    
    EXPECT_EQ(client.getOrders()[0].getItems().size(), 1);

    delete item; 
}
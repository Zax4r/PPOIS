
#include <gtest/gtest.h>
#include "OnlineStore.h"

TEST(OnlineStoreTest, AddClient) {
    string name="Storage1";
    string name2="AdminName";
    int salary=100;
    Storage storage(name);
    Admin admin(name2,salary);
    string storeName = "Test Store";
    OnlineStore store(storeName, storage, admin);
    
    string name3="ClientName";
    Client client(name3);
    store.addClient(client);
    EXPECT_EQ(store.getClients().size(),1);

}


TEST(OnlineStoreTest, AddReview) {
    string name="Storage1";
    string name2="AdminName";
    int salary=100;
    Storage storage(name);
    Admin admin(name2,salary);
    string storeName = "Test Store";
    OnlineStore store(storeName, storage, admin);
    
    string name3="ClientName";
    Client client(name3);
    string reviewMessage = "Great store!";
    Review review(reviewMessage, client);
    store.addReview(review);
    EXPECT_EQ(store.getReviews().size(),1);
}

TEST(OnlineStoreTest, AddItem) {
    string name="Storage1";
    string name2="AdminName";
    int salary=100;
    Storage storage(name);
    Admin admin(name2,salary);
    string storeName = "Test Store";
    OnlineStore store(storeName, storage, admin);

    string name3="ItemName";
    int id=52;
    Item* item= new Item(id,name3);
    store.addItem(item);
    EXPECT_EQ(store.getItems().size(),1);
}
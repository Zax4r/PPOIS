#include <gtest/gtest.h>
#include "Review.h"
#include "PostOffice.h"
#include<sstream>

TEST(SendItemTest, Getters) {
    SendItem item("1", "2", "3", "4", 1);
    EXPECT_EQ(item.GetName(), "1");
    EXPECT_EQ(item.GetType(), "2");
    EXPECT_EQ(item.GetRecipient(), "4");
}


TEST(LetterTest, GetterMessage) {
    Letter letter("1", "2", "3", "4", 1, "5");
    EXPECT_EQ(letter.GetMessage(), "5");
}


TEST(PackageTest, getterVolume) {
    Package package("1", "2", "3", "4", 5, 2);
    EXPECT_EQ(package.GetVolume(), 2.0);
}


TEST(CombinedTest, GetterMessage) {
    Combined combined("1", "2", "3", "4", 1, "5", 2);
    EXPECT_EQ(combined.GetMessage(), "5");
    EXPECT_EQ(combined.GetVolume(),2);
}


TEST(ClientTest, GetterAddres) {
    Client client("1", 2, "3", "4");
    EXPECT_EQ(client.GetAddress(), "4");
}


TEST(PostWorkerTest, GetterName) {
    PostWorker worker("1", 2, 3);
    EXPECT_EQ(worker.GetName(), "1");
}

TEST(PostOfficeTest, AddItemAndGetItems) {
    PostOffice postOffice("AAAA");
    SendItem* item = new Letter("daw", "sad", "awd", "asd", 1.0, "aaw");
    postOffice.addItem(item);
    EXPECT_EQ(postOffice.GetItems().size(), 1);
    delete item;
}

TEST(PostOfficeTest, AddReview) {
    PostOffice postOffice("AAAA");
    Client client("1", 25, "2", "3");
    postOffice.AddReview(client);
    EXPECT_EQ(postOffice.GetClients().size(), 1);
}

TEST(PostOfficeTest, AddClientAndGetClients) {
    PostOffice postOffice("AAAA");
    Client client("adad", 52, "asdasd", "asdasd");
    postOffice.addClient(client);
    EXPECT_EQ(postOffice.GetClients().size(), 1);
}

TEST(PostOfficeTest, AddReviewAnotherrClient) {
    PostOffice postOffice("AAAA");
    Client client("1", 25, "2", "3");
    Client client2("4", 25, "5", "6");
    postOffice.AddReview(client);
    postOffice.AddReview(client2);
    EXPECT_EQ(postOffice.GetClients().size(), 2);
}

TEST(PostOfficeTest, GiveAllItems) {
    PostOffice postOffice("AAAA");
    Client client("1", 52, "2", "3");
    Client client2("4", 52, "5", "6");
    postOffice.addClient(client);
    postOffice.addClient(client2);
    Letter letter("1", "2", "3", "4", 1, "5");
    postOffice.GiveAllItems();
    EXPECT_EQ(postOffice.GetItems().size(),0);
}

TEST(PostOfficeTest, CheckStdoutLetter) {
    PostOffice postOffice("AAAA");
    Client client("1", 52, "2", "3");
    Client client2("4", 52, "5", "6");
    postOffice.addClient(client);
    postOffice.addClient(client2);
    postOffice.addItem(new Letter("1", "2", "3", "4", 1, "5"));
    testing::internal::CaptureStdout();
    postOffice.GiveAllItems();
    std::string output = testing::internal::GetCapturedStdout(); 
    EXPECT_NE(output.find("4 Took a Letter. Named 1"), std::string::npos);
}

TEST(PostOfficeTest, CheckStdoutPackage) {
    PostOffice postOffice("AAAA");
    Client client("1", 52, "2", "3");
    Client client2("4", 52, "5", "6");
    postOffice.addClient(client);
    postOffice.addClient(client2);
    postOffice.addItem(new Package("1", "2", "3", "4", 5, 2));
    testing::internal::CaptureStdout();
    postOffice.GiveAllItems();
    std::string output = testing::internal::GetCapturedStdout(); 
    EXPECT_NE(output.find("4 Took a Package. Named 1"), std::string::npos);
}
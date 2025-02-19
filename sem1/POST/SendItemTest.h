#include <gtest/gtest.h>
#include "PostOffice.h"


TEST(SendItemTest, GetterName) {
    SendItem item("1", "2", "3", "4", 1);
    EXPECT_EQ(item.GetName(), "1");
}

TEST(SendItemTest, GetterType) {
    SendItem item("1", "2", "3", "4", 1);
    EXPECT_EQ(item.GetType(), "2");
}

TEST(SendItemTest, GetterRecipient) {
    SendItem item("1", "2", "3", "4", 1);
    EXPECT_EQ(item.GetRecipient(), "4");
}
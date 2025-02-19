#include <gtest/gtest.h>
#include "OnlineStore.h"

TEST(BuildingTest, GetAddress) {
    string address="11";
    Building me(address);
    EXPECT_EQ(me.getAddress(),address);
}
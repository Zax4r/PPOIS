#include <gtest/gtest.h>
#include "PostOffice.h"
#include<sstream>

TEST(ClientTest, GetterAddres) {
    Client client("1", 2, "3", "4");
    EXPECT_EQ(client.GetAddress(), "4");
}

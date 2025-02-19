#include <gtest/gtest.h>
#include "OnlineStore.h"

TEST(AdminTest, getSalary) {
    string name="Vasya";
    int money=12321;
    Admin me(name,money);
    EXPECT_EQ(me.getSalary(),money);
}
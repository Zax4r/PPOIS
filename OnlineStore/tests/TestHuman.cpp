
#include <gtest/gtest.h>
#include "OnlineStore.h"

TEST(HumanTest, getName) {
    string name="Vasya";
    Human me(name);
    EXPECT_EQ(me.getName(),name);
}
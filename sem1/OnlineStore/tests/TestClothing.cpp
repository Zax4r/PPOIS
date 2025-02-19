#include <gtest/gtest.h>
#include "OnlineStore.h"

TEST(ClothingTest, getSize) {
    int id=52,size=25;
    string name="test";
    Clothing cofta(id,name,size);
    EXPECT_EQ(cofta.getSize(),size);
}
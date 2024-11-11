
#include <gtest/gtest.h>
#include "OnlineStore.h"

TEST(ElectronicItemTest, getWarranty) {
    int id=52;
    bool warranty=true;
    string name="test";
    ElectronicItem item(id,name,warranty);
    EXPECT_TRUE(item.getWarranty());
}
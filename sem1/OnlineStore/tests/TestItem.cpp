
#include <gtest/gtest.h>
#include "OnlineStore.h"

TEST(ItemTest, Getters) {
    int id = 1;
    string name = "Test Item";
    Item item(id, name);
    
    EXPECT_EQ(item.getId(), id);
}
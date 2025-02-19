
#include <gtest/gtest.h>
#include "OnlineStore.h"

TEST(OrderHistoryTest, AddOrder) {
    OrderHistory history;
    int orderId = 1;
    Order order(orderId);
    
    history.addOrder(order);
    EXPECT_EQ(history.getOrders().size(),1);
}
#include <gtest/gtest.h>
#include "PostOffice.h"
#include<sstream>

TEST(PostWorkerTest, GetterName) {
    PostWorker worker("1", 2, 3);
    EXPECT_EQ(worker.GetName(), "1");
}

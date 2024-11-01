#include <gtest/gtest.h>
#include "PostOffice.h"
#include<sstream>

TEST(CombinedTest, GetterMessage1) {
    Combined combined("1", "2", "3", "4", 1, "5", 2);
    EXPECT_EQ(combined.GetMessage(), "5");
}

TEST(CombinedTest, GetterVolume) {
    Combined combined("1", "2", "3", "4", 1, "5", 2);
    EXPECT_EQ(combined.GetVolume(),2);
}
#include <gtest/gtest.h>
#include "PostOffice.h"
#include<sstream>

TEST(PackageTest, getterVolume) {
    Package package("1", "2", "3", "4", 5, 2);
    EXPECT_EQ(package.GetVolume(), 2.0);
}

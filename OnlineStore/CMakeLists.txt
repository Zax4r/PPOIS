cmake_minimum_required(VERSION 3.10)
project(OrderManagement)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Укажите директории с исходниками
include_directories(src)

# Найдите Google Test
find_package(GTest REQUIRED)
include_directories(${GTEST_INCLUDE_DIRS})

# Автоматически добавьте все .cpp файлы из директории src
file(GLOB SOURCES src/*.cpp)

# Добавьте исполняемый файл для тестов
file(GLOB TEST_SOURCES tests/*.cpp)
add_executable(runTests ${SOURCES}  ${TEST_SOURCES})

# Линковка с Google Test
target_link_libraries(runTests ${GTEST_LIBRARIES} pthread)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} --coverage")
# Включите тестирование
enable_testing()

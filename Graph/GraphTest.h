#include "Graph.h"
#include <gtest/gtest.h>

TEST(GraphTest, AddVertices) {
    Graph<std::string> graph;

    graph.addVertex("A");

    EXPECT_EQ(graph.vertexCount(), 1); 
}

TEST(GraphTest, AddEdges) {
    Graph<std::string> graph;

    graph.addVertex("A");
    graph.addVertex("B");


    graph.addEdge("A", "B");


    EXPECT_EQ(graph.getedgeCount(), 1);
}

TEST(GraphTest, HasVertexT) {
    Graph<std::string> graph;

    graph.addVertex("A");

    EXPECT_TRUE(graph.hasVertex("A"));
}

TEST(GraphTest, HasVertexF) {
    Graph<std::string> graph;

    graph.addVertex("A");
    EXPECT_FALSE(graph.hasVertex("E")); // Вершина "E" не должна существовать
}

TEST(GraphTest, HasEdgeF) {
    Graph<std::string> graph;

    graph.addVertex("A");
    graph.addVertex("B");
    graph.addEdge("A", "B");

    EXPECT_FALSE(graph.hasEdge("A", "D"));
}

TEST(GraphTest, HasEdgeT) {
    Graph<std::string> graph;

    graph.addVertex("A");
    graph.addVertex("B");
    graph.addEdge("A", "B");

    EXPECT_TRUE(graph.hasEdge("A", "B")); 
}

TEST(GraphTest, RemoveVertex) {
    Graph<std::string> graph;

    graph.addVertex("A");
    graph.removeVertex("A");

    EXPECT_EQ(graph.vertexCount(), 0);
}

TEST(GraphTest, RemoveVertexWEdge) {
    Graph<std::string> graph;

    graph.addVertex("A");
    graph.addVertex("B");

    graph.addEdge("A", "B");

    graph.removeVertex("B");

    EXPECT_EQ(graph.vertexCount(), 1); 
}

TEST(GraphTest, RemoveEdge) {
    Graph<std::string> graph;

    graph.addVertex("A");
    graph.addVertex("B");
    graph.addEdge("A", "B");

    graph.removeEdge("A", "B");

    EXPECT_FALSE(graph.hasEdge("A", "B"));
}

TEST(GraphTest, VertexDegree) {
    Graph<std::string> graph;

    graph.addVertex("A");
    graph.addVertex("B");
    graph.addEdge("A", "B");

    EXPECT_EQ(graph.degree("A"), 1);
}

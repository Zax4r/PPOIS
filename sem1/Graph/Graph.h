#include <vector>
#include <stdexcept>
#include <algorithm>
#include <iterator>
#include <utility>
#include <string>
#include <iostream>
#include <numeric>
using namespace std;

template <typename T>
class Graph {
public:
    using VertexType = T;
    using EdgeType = pair<int, int>; 

private:
     vector<VertexType> vertices;           
     vector< vector<int>> incMatrix;    
    int edgeCount = 0;                        

public:
    int vertexCount() const {
        return vertices.size();
    }


    int getedgeCount() const {
        return edgeCount;
    }

    void addVertex(const VertexType& vertex) {
        vertices.push_back(vertex);

        for (auto& column : incMatrix) {
            column.push_back(0);
        }
    }

   
    bool hasVertex(const VertexType& vertex) const {
        return  find(vertices.begin(), vertices.end(), vertex) != vertices.end();
    }

  
    int getVertexIndex(const VertexType& vertex) const {
        for (int i = 0; i < vertices.size(); i++)
        {
            if (vertices[i] == vertex)
                return i;
           
        }
        return -1;
    }

  
    void addEdge(const VertexType& v1, const VertexType& v2) {
        int idx1 = getVertexIndex(v1);
        int idx2 = getVertexIndex(v2);

        if ((idx1 ==-1 || idx2 == -1))
            return;
        
             vector<int> newEdge(vertices.size(), 0);
            newEdge[idx1] = 1;
            newEdge[idx2] = 1;

            incMatrix.push_back(newEdge);
            ++edgeCount;
        
    }

    bool hasEdge(const VertexType& v1, const VertexType& v2) const {
        int idx1 = getVertexIndex(v1);
        int idx2 = getVertexIndex(v2);
        if ((idx1 == -1 || idx2 == -1))
            return false;

        for (const auto& edge : incMatrix) {
            if (edge[idx1] == 1 && edge[idx2] == 1) {
                return true;
            }
        }
        return false;
    }

    void removeEdge(const VertexType& v1, const VertexType& v2) {
        int idx1 = getVertexIndex(v1);
        int idx2 = getVertexIndex(v2);
        if ((idx1 == -1 || idx2 == -1))
            return;

        for (auto it = incMatrix.begin(); it != incMatrix.end(); it++) {
            if ((*it)[idx1] == 1 && (*it)[idx2] == 1) {
                incMatrix.erase(it);
                --edgeCount;
                return;
            }
        }
    }

    void removeVertex(const VertexType& vertex) {
        int idx = getVertexIndex(vertex);
        if (idx == -1)
            return;

        for (auto& edge : incMatrix) {
            edge.erase(edge.begin() + idx);
        }

        vertices.erase(vertices.begin() + idx);

        auto it = incMatrix.begin();
        while (it != incMatrix.end()) {
            int sum =  accumulate(it->begin(), it->end(), 0);
            if (sum<2) {
                it = incMatrix.erase(it);
                --edgeCount;
            }
            else {
                ++it;
            }
        }
    }

    int degree(const VertexType& vertex) const {
        int idx = getVertexIndex(vertex);
        int degree = 0;
        if (idx == -1)
            return 0;

        for (const auto& edge : incMatrix) {
            if (edge[idx] == 1) {
                ++degree;
            }
        }
        return degree;
    }

    class VertexIterator;

    VertexIterator beginVertices() {
        return VertexIterator(vertices.begin());
    }

    VertexIterator endVertices() {
        return VertexIterator(vertices.end());
    }

    class EdgeIterator ;

    EdgeIterator beginEdges() const {
        return EdgeIterator(0, *this);
    }

    EdgeIterator endEdges() const {
        return EdgeIterator(incMatrix.size(), *this);
    }
};

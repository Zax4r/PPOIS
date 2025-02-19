 #include "VertexIterator.h"
template<typename T>
class Graph<T>::EdgeIterator {
        int currentEdge;
        const Graph& graph;

    public:

        EdgeIterator(int edge, const Graph& g) : currentEdge(edge), graph(g) {}

        EdgeIterator& operator++() {
            currentEdge++;
            return *this;
        }

        EdgeIterator operator++(int) {
            EdgeIterator temp = *this;
            (*this)++;
            return temp;
        }

        EdgeIterator& operator--() {
            currentEdge--;
            return *this;
        }

        EdgeIterator operator--(int) {
            EdgeIterator temp = *this;
            (*this)--;
            return temp;
        }

        EdgeType operator*() const {
            const auto& edge = graph.incMatrix[currentEdge];
            int v1 = 0, v2 = 0;
            bool firstFound = false;

            for (int i = 0; i < edge.size(); ++i) {
                if (edge[i] == 1) {
                    if (!firstFound) {
                        v1 = i;
                        firstFound = true;
                    }
                    else {
                        v2 = i;
                        return { v1,v2 };
                    }
                }
            }
            return { v1, v2 };
        }

        bool operator==(const EdgeIterator& other) const {
            return currentEdge == other.currentEdge;
        }

        bool operator!=(const EdgeIterator& other) const {
            return currentEdge != other.currentEdge;
        }
    };
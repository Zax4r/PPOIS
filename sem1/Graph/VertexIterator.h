 
#include "Graph.h"
template<typename T>
class Graph<T>:: VertexIterator {
        typename  vector<VertexType>::iterator it;

    public:

        VertexIterator(typename  vector<VertexType>::iterator it) : it(it) {}

        VertexIterator& operator++() {
            it++;
            return *this;
        }

        VertexIterator operator++(int) {
            VertexIterator temp = *this;
            (*this)++;
            return temp;
        }

        VertexIterator& operator--() {
            it--;
            return *this;
        }

        VertexIterator operator--(int) {
            VertexIterator temp = *this;
            (*this)--;
            return temp;
        }

        VertexType& operator*() {
            return *it;
        }

        bool operator==(const VertexIterator& other) const {
            return it == other.it;
        }

        bool operator!=(const VertexIterator& other) const {
            return it != other.it;
        }
    };
#include "polygon.hpp"
#include <cmath>
class Triangle : public Polygon
{
  public:
    virtual double area() const
    {
        return m_side_len * m_side_len * sqrt(3) / 2;
    }
};

extern "C" Polygon *create()
{
    return new Triangle;
}

extern "C" void destroy(Polygon *p)
{
    delete p;
}
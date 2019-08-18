#ifndef __POLYGON_HPP__
#define __POLYGON_HPP__

class Polygon
{
  protected:
    double m_side_len;

  public:
    Polygon() : m_side_len(0) {}
    virtual ~Polygon() {}
    void set_side_len(double side_len)
    {
        m_side_len = side_len;
    }

    virtual double area() const = 0;
};

typedef Polygon *create_t();
typedef void destroy_t(Polygon *);

#endif
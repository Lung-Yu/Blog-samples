#pragma once
#include <vector>

using namespace std;

#pragma once
class Neuron
{
public:
	Neuron(int dendritesSize);
	~Neuron();

	void pushInput(double* in);
	void activity();
	double output();
	void correct(int index,double detla);
	double getWeight(int index);
	int dendritySize();

	int WeightSize();

private:
	double _bais;
	double _synapse;
	vector<double> _dendrites;


	double *_signals;
	int _dendritySize;
	const double _arfa = -0.5;
	const double momentum = 1;

	double summation();


};
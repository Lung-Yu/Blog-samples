#pragma once
#include <vector>
#include "Neuron.h"

#pragma once
class Backpropagation
{
public:
	Backpropagation(int inSize,int outSize);
	~Backpropagation();

	void pushInput(double *);
	void setDesires(double *);
	int getOutputSize();
	int getIntputSize();
	void train();
	double* calc();
	void correct();
	double getMSE(double);

private:
	const double LEARN_RATE = 0.5;
	int _inputSize;
	int _outputSize;
	std::vector<Neuron> _hiddenOne;
	std::vector<Neuron> _output;
	double *_singals;
	double *_desires;
	void buildNetwork();
	
};


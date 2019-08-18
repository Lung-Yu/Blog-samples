#include "stdafx.h"
#include "Neuron.h"


Neuron::Neuron(int dendritesSize)
{
	_bais = (rand() % 100) * 0.01 - 0.5;
	_dendritySize = dendritesSize;

	//_dendrites = (double*)malloc(sizeof(double)* _dendritySize);
	_signals = (double*)malloc(sizeof(double)* _dendritySize);

	for (int i = 0; i < _dendritySize; i++){
		//_dendrites[i] = 0.5 * pow(-1, i);
		double val = rand() % 10 - 5;
		_dendrites.push_back(val * 0.1);
	}
}


Neuron::~Neuron()
{
}

void Neuron::activity(){
	double sum = summation();
	_synapse = 1 / (1 + exp(sum * _arfa));	// sigmoid
}

double Neuron::summation(){
	double sum = _bais;
	for (int i = 0; i < _dendritySize; i++){
		sum += _dendrites[i] * _signals[i];
	}
	return sum;
}

void Neuron::pushInput(double* in){
	for (int i = 0; i < _dendritySize; i++){
		_signals[i] = in[i];
	}
}
double Neuron::output(){
	return _synapse;
}
double Neuron::getWeight(int index){
	return _dendrites.at(index);
}

void Neuron::correct(int index, double detla){
	double newVal = _dendrites.at(index) + detla;
	_dendrites[index] = newVal;
}

int Neuron::WeightSize(){
	return sizeof(_dendrites) / sizeof(double);
}

int Neuron::dendritySize(){
	return _dendritySize;
}
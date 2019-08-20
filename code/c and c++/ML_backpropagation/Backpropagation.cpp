#include "stdafx.h"
#include "Backpropagation.h"

#define HIDDEN_ONE 1000

using namespace std;

Backpropagation::Backpropagation(int inSize, int outSize)
{
	_inputSize = inSize;
	_outputSize = outSize;
	buildNetwork();
}

void Backpropagation::train(){
	double mse = 0;
	int count = 0;
	double *output;
	do{
		mse = 0;
		output = calc();

		for (int i = 0; i<getOutputSize(); i++){
			mse = 0.5 * (_desires[i] - *output)* (_desires[i] - *output);
			correct();
		}

		printf("MSE : %lf\n", mse);
	} while (mse > 0.01);
}

double Backpropagation::getMSE(double output){
	double mse = 0;
	for (int i = 0; i<getOutputSize(); i++){
		mse = 0.5 * (_desires[i] - output)* (_desires[i] - output);
		correct();
	}
	return mse;
}

void Backpropagation::correct(){
	double *outError = (double *)malloc(sizeof(double)* _outputSize);
	double hidenError[HIDDEN_ONE];

	for (int i = 0; i < getOutputSize(); i++){
		outError[i] = (_desires[i] - _output[i].output()) * (1 - _output[i].output() * _output[i].output());

		for (int j = 0; j < HIDDEN_ONE; j++){
			hidenError[i] = outError[i] * _hiddenOne[j].getWeight(i) * (1 - _hiddenOne[j].output() * _hiddenOne[j].output());
		}
	}

	for (int i = 0; i < getOutputSize(); i++){
		for (int j = 0; j < HIDDEN_ONE; j++){
			double delta = LEARN_RATE * outError[i] * _output[i].output() + _output[i].getWeight(j);
			_output[i].correct(j, delta);
		}
	}

	for (int i = 0; i < HIDDEN_ONE; i++){
		for (int j = 0; j < getIntputSize(); j++){
			double delta = LEARN_RATE * hidenError[j] * _hiddenOne[i].getWeight(j);
			_hiddenOne[i].correct(j, delta);
		}
	}

	free(outError);
}


double* Backpropagation::calc(){
	double *temp = (double *)malloc(HIDDEN_ONE * sizeof(double));
	for (int i = 0; i < HIDDEN_ONE; i++){
		_hiddenOne.at(i).pushInput(_singals);
		_hiddenOne.at(i).activity();

		temp[i] = _hiddenOne[i].output();
	}

	double *output = (double *)malloc(getOutputSize() * sizeof(double));
	for (int i = 0; i < getOutputSize(); i++){
		_output.at(i).pushInput(temp);
		_hiddenOne.at(i).activity();

		output[i] = _hiddenOne.at(i).output();
	}

	free(temp);

	return output;
}


void Backpropagation::buildNetwork(){
	//build Network
	_hiddenOne.clear();
	//build layer 1
	for (int i = 0; i < HIDDEN_ONE; i++){
		Neuron neuron(getIntputSize());
		_hiddenOne.push_back(neuron);
	}
	//build output layer
	_output.clear();
	for (int i = 0; i < getOutputSize(); i++){
		Neuron neuron(HIDDEN_ONE);
		_output.push_back(neuron);
	}
}
void Backpropagation::setDesires(double *desires){
	_desires = desires;
}
void Backpropagation::pushInput(double *input){
	_singals = input;
}

int Backpropagation::getOutputSize(){
	return _outputSize;
}
int Backpropagation::getIntputSize(){
	return _inputSize;
}
Backpropagation::~Backpropagation()
{
}
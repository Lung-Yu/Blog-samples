#include <Windows.h>

DWORD WINAPI DoStuff(LPVOID lpParameter)
{
	// The new thread will start here
	return 0;
}

int main()
{
	// Create a new thread which will start at the DoStuff function
	HANDLE hThread = CreateThread(
		NULL,    // Thread attributes
		0,       // Stack size (0 = use default)
		DoStuff, // Thread start address
		NULL,    // Parameter to pass to the thread
		0,       // Creation flags
		NULL);   // Thread id
	if (hThread == NULL)
	{
		// Thread creation failed.
		// More details can be retrieved by calling GetLastError()
		return 1;
	}

	// Wait for thread to finish execution
	WaitForSingleObject(hThread, INFINITE);

	// Thread handle must be closed when no longer needed
	CloseHandle(hThread);

	system("pause");

	return 0;
}
#include <iostream>
#include <Windows.h>

#define VK_A 0x41
#define VK_B 0x42
#define VK_E 0x45
#define VK_H 0x48
#define VK_O 0x4F
#define VK_R 0x52
#define VK_S 0x53
#define VK_W 0x57


void post_msg_to_nodepad();

int main(){
	
	post_msg_to_nodepad();
	system("PAUSE");
	return 0;
}

void post_msg_to_nodepad(){
	HWND hWnd = NULL;
	HWND hWndEdit = NULL;

	//hWnd = FindWindow("Notepad", Null);
	hWnd = FindWindow("Notepad", "aa.txt - Notepad");
	if (hWnd == NULL)
	{
		std::cout << "Error: Can't find Notepad, aborting\n" << std::endl;
	}
	hWndEdit = FindWindowEx(hWnd, NULL, "Edit", NULL);
	if (hWndEdit == NULL)
	{
		std::cout << "Error: Can't find Notepad Edit, aborting\n" << std::endl;
	}

	std::cout << "hWnd\t" << hWnd << std::endl;
	std::cout << "hWndEdit\t" << hWndEdit << std::endl;
	//_In_ DWORD idThread,	_In_ UINT Msg,		_In_ WPARAM wParam,		_In_ LPARAM lParam);
	PostMessage(hWndEdit, WM_KEYDOWN, VK_B, 0);
	PostMessage(hWndEdit, WM_KEYDOWN, VK_O, 1);
	PostMessage(hWndEdit, WM_KEYDOWN, VK_B, 1);
	PostMessage(hWndEdit, WM_KEYDOWN, VK_SPACE, 1);
	PostMessage(hWndEdit, WM_KEYDOWN, VK_W, 1);
	PostMessage(hWndEdit, WM_KEYDOWN, VK_A, 1);
	PostMessage(hWndEdit, WM_KEYDOWN, VK_S, 1);
	PostMessage(hWndEdit, WM_KEYDOWN, VK_SPACE, 1);
	PostMessage(hWndEdit, WM_KEYDOWN, VK_H, 1);
	PostMessage(hWndEdit, WM_KEYDOWN, VK_E, 1);
	PostMessage(hWndEdit, WM_KEYDOWN, VK_R, 1);
	PostMessage(hWndEdit, WM_KEYDOWN, VK_E, 1);
}


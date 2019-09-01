#include <iostream>
#include <Windows.h>

#define VK_T 0x54
#define VK_Y 0x59
#define VK_G 0x47
#define VK_R 0x52
#define VK_W 0x57
#define VK_A 0x41
#define VK_S 0x53
#define VK_H 0x48
#define VK_E 0x45
#define VK_R 0x52
#define VK_DOT 0x2E


void post_msg_to_nodepad();
void send_msg_to_nodepad();

int main(){
	//post_msg_to_nodepad();
	send_msg_to_nodepad();
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
	PostMessage(hWndEdit, WM_KEYDOWN, VK_T, 1);
	PostMessage(hWndEdit, WM_KEYDOWN, VK_Y, 1);
	PostMessage(hWndEdit, WM_KEYDOWN, VK_G, 1);
	PostMessage(hWndEdit, WM_KEYDOWN, VK_R, 1);
	PostMessage(hWndEdit, WM_KEYDOWN, VK_SPACE, 1);
	PostMessage(hWndEdit, WM_KEYDOWN, VK_W, 1);
	PostMessage(hWndEdit, WM_KEYDOWN, VK_A, 1);
	PostMessage(hWndEdit, WM_KEYDOWN, VK_S, 1);
	PostMessage(hWndEdit, WM_KEYDOWN, VK_SPACE, 1);
	PostMessage(hWndEdit, WM_KEYDOWN, VK_H, 1);
	PostMessage(hWndEdit, WM_KEYDOWN, VK_E, 1);
	PostMessage(hWndEdit, WM_KEYDOWN, VK_R, 1);
	PostMessage(hWndEdit, WM_KEYDOWN, VK_E, 1);
	PostMessage(hWndEdit, WM_KEYDOWN, VK_DOT, 1);

}


void send_msg_to_nodepad(){
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
	SendMessage(hWndEdit, WM_KEYDOWN, VK_T, 1);
	SendMessage(hWndEdit, WM_KEYDOWN, VK_Y, 1);
	SendMessage(hWndEdit, WM_KEYDOWN, VK_G, 1);
	SendMessage(hWndEdit, WM_KEYDOWN, VK_R, 1);
	SendMessage(hWndEdit, WM_KEYDOWN, VK_SPACE, 1);
	SendMessage(hWndEdit, WM_KEYDOWN, VK_W, 1);
	SendMessage(hWndEdit, WM_KEYDOWN, VK_A, 1);
	SendMessage(hWndEdit, WM_KEYDOWN, VK_S, 1);
	SendMessage(hWndEdit, WM_KEYDOWN, VK_SPACE, 1);
	SendMessage(hWndEdit, WM_KEYDOWN, VK_H, 1);
	SendMessage(hWndEdit, WM_KEYDOWN, VK_E, 1);
	SendMessage(hWndEdit, WM_KEYDOWN, VK_R, 1);
	SendMessage(hWndEdit, WM_KEYDOWN, VK_E, 1);
	SendMessage(hWndEdit, WM_KEYDOWN, VK_DOT, 1);

}



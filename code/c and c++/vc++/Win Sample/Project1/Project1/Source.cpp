#include <windows.h>
int WINAPI WinMain(
	HINSTANCE hInstance,
	HINSTANCE hPrevInstance,
	LPSTR lpCmdLine,
	int nCmdShow
	){
	// 调用API 函数MessageBox
	int nSelect = MessageBox(NULL, TEXT("Lung yu, 第一個C語言 Sample."), TEXT("Welcome"), MB_OKCANCEL);
	if (nSelect == IDOK){
		MessageBox(NULL, TEXT("你點擊了'確認'按鈕"), TEXT("提示1"), MB_OK);
	}
	else{
		MessageBox(NULL, TEXT("你點擊了'取消'按鈕"), TEXT("提示2"), MB_OK);
	}
	return 0;
}
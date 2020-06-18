using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;

namespace SingleProcessSample
{
    public class SingleProcessModule
    {
        [System.Runtime.InteropServices.DllImport("User32.dll")]
        private static extern bool SetForegroundWindow(IntPtr handle);
        [System.Runtime.InteropServices.DllImport("User32.dll")]
        private static extern bool ShowWindow(IntPtr handle, int nCmdShow);
        [System.Runtime.InteropServices.DllImport("User32.dll")]
        private static extern bool IsIconic(IntPtr handle);

        private static SingleProcessModule _instance = null;
        public static SingleProcessModule getInstance()
        {
            if (_instance == null)
                _instance = new SingleProcessModule();
            return _instance;
        }

        private const int SW_RESTORE = 9;
        private string MutexUniqueName;
        private Mutex m = null;

        private SingleProcessModule()
        {
            MutexUniqueName = "TYGR_SINGLE_MUTEX_" + Process.GetCurrentProcess().ProcessName;
        }

        public bool IsCreated()
        {
            Boolean bCreatedNew = false;

            //Create a new mutex using specific mutex name
            m = new Mutex(false, MutexUniqueName, out bCreatedNew);
            GC.Collect();
            if (bCreatedNew)
                return true;

            BringSelfToFront();
            return false;
        }

        private void BringSelfToFront()
        {
            foreach (Process p in Process.GetProcessesByName(Process.GetCurrentProcess().ProcessName))
                BringProcessToFront(p);
        }

        private static void BringProcessToFront(Process process)
        {
            IntPtr handle = process.MainWindowHandle;
            if (IsIconic(handle))
            {
                ShowWindow(handle, SW_RESTORE);
            }

            SetForegroundWindow(handle);
        }
    }
}

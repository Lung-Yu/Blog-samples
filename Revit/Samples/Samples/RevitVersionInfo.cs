using Autodesk.Revit.Attributes;
using Autodesk.Revit.DB;
using Autodesk.Revit.DB.Mechanical;
using Autodesk.Revit.UI;
using Autodesk.Revit.UI.Selection;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Samples
{
    [Transaction(TransactionMode.Manual)]
    class RevitVersionInfo : IExternalCommand
    {
        public Result Execute(ExternalCommandData commandData, ref string message, Autodesk.Revit.DB.ElementSet elements)
        {
            string version = commandData.Application.Application.VersionBuild;
            version += "\n" + commandData.Application.Application.VersionName;
            version += "\n" + commandData.Application.Application.VersionNumber;
            TaskDialog.Show("info", version);
            return Result.Succeeded;
        }
    }
}

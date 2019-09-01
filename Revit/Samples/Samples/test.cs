using Autodesk.Revit.Attributes;
using Autodesk.Revit.DB;
using Autodesk.Revit.UI;
using Autodesk.Revit.UI.Selection;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Samples
{
    [TransactionAttribute(TransactionMode.Manual)]
    class test : IExternalCommand
    {

        public Result Execute(ExternalCommandData commandData, ref string message, Autodesk.Revit.DB.ElementSet elements)
        {
            UIApplication app = commandData.Application;
            Document doc = app.ActiveUIDocument.Document;

            CountElements(doc);

            return Result.Succeeded;
        }

        private void CountElements(Document doc)
        {
            StringBuilder msg = new StringBuilder();
            FilteredElementCollector viewCollector = new FilteredElementCollector(doc, doc.ActiveView.Id);
            viewCollector.OfCategory(BuiltInCategory.OST_Walls);
            msg.AppendLine("Wall within active View:" + viewCollector.ToElementIds().Count);
            FilteredElementCollector docCollector = new FilteredElementCollector(doc);
            docCollector.OfCategory(BuiltInCategory.OST_Walls);
            msg.AppendLine("Wall within Document:" + docCollector.ToElementIds().Count);
            
            TaskDialog.Show("Lung-yu,Tsai", msg.ToString());
        }
    }
}

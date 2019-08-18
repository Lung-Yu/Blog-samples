using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

public partial class _Default : System.Web.UI.Page
{
    protected void Page_Load(object sender, EventArgs e)
    {

    }
    protected void Unnamed_Click(object sender, EventArgs e)
    {
        StringBuilder sb = new StringBuilder();
        sb.Append("Head_1,Head_2\n");
        sb.Append("Row_1,Row_2\n");
        sb.Append("Row_1,Row_2\n");
        sb.Append("Row_1,Row_2\n");
        sb.Append("Row_1,Row_2\n");
        sb.Append("Row_1,Row_2\n");

        byte[] bytes = Encoding.ASCII.GetBytes(sb.ToString());
        downloadFile("sample.csv", bytes);
    }

    private void downloadFile(string filename, byte[] bytes)
    {
        if (bytes != null)
        {
            Response.Clear();
            Response.ContentType = "text/csv";
            Response.AddHeader("Content-Length", bytes.Length.ToString());
            Response.AddHeader("Content-disposition", "attachment; filename=\"" + filename + "" + "\"");
            Response.BinaryWrite(bytes);
            Response.Flush();
            Response.End();
        }
    }
}
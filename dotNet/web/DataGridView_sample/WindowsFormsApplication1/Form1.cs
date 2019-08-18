using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WindowsFormsApplication1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();

            init_grid_view();
        }

        private void init_grid_view()
        {
            DataTable dt = getRealDataSource();

            dataGridView1.DataSource = dt;
            //dataGridView1.AutoResizeColumns(DataGridViewAutoSizeColumnsMode.AllCellsExceptHeader);
        }

        private DataTable getRealDataSource()
        {
            string[] test_array = { "紅茶", "綠茶" };
            int[] test_array2 = { 25, 25};

            DataTable dt = new DataTable();
            dt.Columns.Add("Column1", typeof(string));
            dt.Columns.Add("Column2", typeof(string));
            dt.Columns.Add("Column3", typeof(string));

            for (int i = 0; i < test_array.Length; i++)
            {
                DataRow row = dt.NewRow();
                row["Column1"] = (i % 2 == 0)?true:false;
                row["Column2"] = test_array[i];
                row["Column3"] = test_array2[i];

                dt.Rows.Add(row);
            }
            return dt;
        }
    }
}

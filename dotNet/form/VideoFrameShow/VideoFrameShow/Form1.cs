using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Diagnostics;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace VideoFrameShow
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();

            textBox1.Text = @"D:\Projects\struct box\test_fff\unknown_R_未知_Golden.Dragon_1__0_13010.mp4";
            textBox1.Text = @"D:\Projects\struct box\violation_datas2\7_2__其他_Isuzu_2__0_13450.mp4";    
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string videoPath = textBox1.Text;
            //makeAvi(videoPath, "out.avi", 1);
            int total_count = getFrames(videoPath,-1);
            initCombox(total_count);
        }

        private void initCombox(int count)
        {
            DataTable dt = new DataTable();
            dt.Columns.Add("text", typeof(string));
            dt.Columns.Add("value", typeof(string));

            for(int i = 0; i < count; i++)
            {
                DataRow row = dt.NewRow();
                row["text"] = i;
                row["value"] = i;
                dt.Rows.Add(row);
            }

            comboBox1.DataSource = dt;
            comboBox1.DisplayMember = dt.Columns[0].ToString();
            comboBox1.ValueMember = dt.Columns[1].ToString();
        }

        private Bitmap getFrame(string src_path, int idx)
        {
            int frameCount = 0;

            Accord.Video.FFMPEG.VideoFileReader videoFileReader = new Accord.Video.FFMPEG.VideoFileReader();
            videoFileReader.Open(src_path);
            frameCount = (int)videoFileReader.FrameCount;

            Debug.WriteLine("Frame Count : " + videoFileReader.FrameCount);
            Debug.WriteLine("Frame Rate : " + videoFileReader.FrameRate);
            Debug.WriteLine("Width " + videoFileReader.Width + " ,Height " + videoFileReader.Height);

            if (idx == -1)  idx = (int)(frameCount * 0.4);  // defalut use index

            Bitmap bitmap = videoFileReader.ReadVideoFrame(idx);
            return bitmap;
        }

        private int getFrames(string src_path,int idx)
        {
            int frameCount = 0;

            Accord.Video.FFMPEG.VideoFileReader videoFileReader = new Accord.Video.FFMPEG.VideoFileReader();
            videoFileReader.Open(src_path);
            frameCount =(int) videoFileReader.FrameCount;

            Debug.WriteLine("Frame Count : " + videoFileReader.FrameCount);
            Debug.WriteLine("Frame Rate : " + videoFileReader.FrameRate);
            Debug.WriteLine("Width " + videoFileReader.Width + " ,Height " + videoFileReader.Height);

            if (idx == -1)
                idx = (int)(frameCount * 0.4);


            Bitmap bitmap = videoFileReader.ReadVideoFrame(idx);
            pictureBox1.Image = bitmap;

            videoFileReader.Close();

            return frameCount;
        }

        private void makeAvi(string inputPath, string outputFileName, int fps, string imgType = "*.jpg")
        {
            Accord.Video.FFMPEG.VideoFileWriter vw = new Accord.Video.FFMPEG.VideoFileWriter();

            //286, 270為圖片長寬，一定要與輸入圖片長寬一致，且要為偶數
            vw.Open(outputFileName, 286, 270, fps, Accord.Video.FFMPEG.VideoCodec.MPEG4);

            string[] imgs = System.IO.Directory.GetFiles(inputPath, imgType);
            foreach (string img in imgs)
            {
                using (System.Drawing.Image i = System.Drawing.Image.FromFile(img))
                {
                    vw.WriteVideoFrame(i as Bitmap);
                }
            }
            vw.Close();
        }

        private void comboBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            string videoPath = textBox1.Text;
            //makeAvi(videoPath, "out.avi", 1);
            int total_count = getFrames(videoPath, comboBox1.SelectedIndex);
            //initCombox(total_count);
        }
    }
}

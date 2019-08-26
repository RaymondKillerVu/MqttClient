using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.IO.Ports;
using System.Threading;


namespace WindowsFormsApp1
{
    public partial class Form3 : Form
    {
        string s100, s101, s102;

        private void button1_Click(object sender, EventArgs e)
        {
            ((Form1)this.Owner).serialPort1.WriteLine("$$");
            Thread.Sleep(200);
            DataReceive();
        }

        private void save_Click(object sender, EventArgs e)
        {
            string str;
            double v;
            string vreal;
            bool flag = true;

            // s100
            s100 = this.s100text.Text;
            if (!string.IsNullOrEmpty(realx.Text))
            {
                vreal = this.realx.Text;
                try
                { v = ((Convert.ToDouble(s100)) * 50) / Convert.ToDouble(vreal); }
                catch
                {
                    MessageBox.Show("nhap sai !!!");
                    v = (Convert.ToDouble(s100));
                    flag = false;
                }
            }
            else
                v = (Convert.ToDouble(s100));
            str = "$100=";
            str += v.ToString();
            ((Form1)this.Owner).serialPort1.WriteLine(str);
            this.realx.Clear();
            // s101
            s101 = this.s101text.Text;
            if (!string.IsNullOrEmpty(realy.Text))
            {
                vreal = this.realy.Text;
                try
                { v = ((Convert.ToDouble(s101)) * 50) / Convert.ToDouble(vreal); }
                catch
                {
                    MessageBox.Show("nhap sai !!!");
                    v = (Convert.ToDouble(s101));
                    flag = false;
                }
            }
            else
                v = (Convert.ToDouble(s101));
            str = "$101=";
            str += v.ToString();
            ((Form1)this.Owner).serialPort1.WriteLine(str);
            this.realy.Clear();

            // s102
            s102 = this.s102text.Text;
            if (!string.IsNullOrEmpty(realz.Text))
            {
                vreal = this.realz.Text;
                try
                { v = ((Convert.ToDouble(s102)) * 50) / Convert.ToDouble(vreal); }
                catch
                {
                    MessageBox.Show("nhap sai !!!");
                    v = (Convert.ToDouble(s102));
                    flag = false;
                }
            }
            else
                v = (Convert.ToDouble(s102));
            str = "$102=";
            str += v.ToString();
            ((Form1)this.Owner).serialPort1.WriteLine(str);
            this.realz.Clear();

            if (flag)
                MessageBox.Show("OK");

        }

        private void DataReceive()
        {
            // s100
            int x = ((Form1)this.Owner).InputData.IndexOf("$100=");
            s100 = ((Form1)this.Owner).InputData.Substring(x + 5, 7);
            // s101
            x = ((Form1)this.Owner).InputData.IndexOf("$101=");
            s101 = ((Form1)this.Owner).InputData.Substring(x + 5, 7);
            // s102
            x = ((Form1)this.Owner).InputData.IndexOf("$102=");
            s102 = ((Form1)this.Owner).InputData.Substring(x + 5, 7);


            SetText();
        }

        private void SetText()
        {
            
            this.s100text.Text = s100;
            this.s101text.Text = s101;
            this.s102text.Text = s102;

        }

        private void test_Click(object sender, EventArgs e)
        {
            ((Form1)this.Owner).serialPort1.WriteLine("G00 X50");
        }

        private void button2_Click(object sender, EventArgs e)
        {
            ((Form1)this.Owner).serialPort1.WriteLine("G00 Y50");
        }

        private void button3_Click(object sender, EventArgs e)
        {
            ((Form1)this.Owner).serialPort1.WriteLine("G00 Z50");
        }

        public Form3()
        {
            InitializeComponent();
        }

        private void Form3_Load(object sender, EventArgs e)
        {

        }
    }
}

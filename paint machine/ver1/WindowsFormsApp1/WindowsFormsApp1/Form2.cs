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
    public partial class Form2 : Form
    {
        public Form2()
        {
            InitializeComponent();
        }
         
        delegate void SetTextCallback(string text);
        string s0, s1, s3, s5, s12, s13, s20, s21, s23, s24, s25, s26, s27, s130, s131, s132;

        private void realx_TextChanged(object sender, EventArgs e)
        {

        }

        private void s102text_TextChanged(object sender, EventArgs e)
        {

        }

        private void button3_Click(object sender, EventArgs e)
        {

        }

        private void label3_Click(object sender, EventArgs e)
        {

        }

        private void s101text_TextChanged(object sender, EventArgs e)
        {

        }

        private void button2_Click_1(object sender, EventArgs e)
        {

        }

        private void label17_Click(object sender, EventArgs e)
        {

        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void label16_Click(object sender, EventArgs e)
        {

        }

        private void s27text_TextChanged(object sender, EventArgs e)
        {

        }

        private void label10_Click(object sender, EventArgs e)
        {

        }

        private void s26text_TextChanged(object sender, EventArgs e)
        {

        }

        private void label11_Click(object sender, EventArgs e)
        {

        }

        private void s25text_TextChanged(object sender, EventArgs e)
        {

        }

        private void label12_Click(object sender, EventArgs e)
        {

        }

        private void s24text_TextChanged(object sender, EventArgs e)
        {

        }

        private void label13_Click(object sender, EventArgs e)
        {

        }

        private void s23text_TextChanged(object sender, EventArgs e)
        {

        }

        private void label14_Click(object sender, EventArgs e)
        {

        }

        private void s20text_TextChanged(object sender, EventArgs e)
        {

        }

        private void label15_Click(object sender, EventArgs e)
        {

        }

        private void s13text_TextChanged(object sender, EventArgs e)
        {

        }

        private void label7_Click(object sender, EventArgs e)
        {

        }

        private void s12text_TextChanged(object sender, EventArgs e)
        {

        }

        private void label8_Click(object sender, EventArgs e)
        {

        }

        private void s5text_TextChanged(object sender, EventArgs e)
        {

        }

        private void label9_Click(object sender, EventArgs e)
        {

        }

        private void s3text_TextChanged(object sender, EventArgs e)
        {

        }

        private void label6_Click(object sender, EventArgs e)
        {

        }

        private void s1text_TextChanged(object sender, EventArgs e)
        {

        }

        private void label5_Click(object sender, EventArgs e)
        {

        }

        private void s0text_TextChanged(object sender, EventArgs e)
        {

        }

        private void s21text_TextChanged(object sender, EventArgs e)
        {

        }

        private void realy_TextChanged(object sender, EventArgs e)
        {

        }

        private void realz_TextChanged(object sender, EventArgs e)
        {

        }

        private void label18_Click(object sender, EventArgs e)
        {

        }

        private void Form2_Load(object sender, EventArgs e)
        {

        }

        private void label19_Click(object sender, EventArgs e)
        {

        }

        private void save_Click(object sender, EventArgs e)
        {
            string str;
            bool flag = true;

            // s0
            s0 = this.s0text.Text;
            str = "$0=";
            str += s0;
            ((Form1)this.Owner).serialPort1.WriteLine(str);
            // s1
            s1 = this.s1text.Text;
            str = "$1=";
            str += s1;
            ((Form1)this.Owner).serialPort1.WriteLine(str);
            // s3
            s3 = this.s3text.Text;
            str = "$3=";
            str += s3;
            ((Form1)this.Owner).serialPort1.WriteLine(str);
            // s5
            s5 = this.s5text.Text;
            str = "$5=";
            str += s5;
            ((Form1)this.Owner).serialPort1.WriteLine(str);
            // s12
            s12 = this.s12text.Text;
            str = "$12=";
            str += s12;
            ((Form1)this.Owner).serialPort1.WriteLine(str);
            // s13 
            s13 = this.s13text.Text;
            str = "$13=";
            str += s13;
            ((Form1)this.Owner).serialPort1.WriteLine(str);
            // s20
            s20 = this.s20text.Text;
            str = "$20=";
            str += s20;
            ((Form1)this.Owner).serialPort1.WriteLine(str);
            // s21
            s21 = this.s21text.Text;
            str = "$21=";
            str += s21;
            ((Form1)this.Owner).serialPort1.WriteLine(str);
            // s23
            s23 = this.s23text.Text;
            str = "$23=";
            str += s23;
            ((Form1)this.Owner).serialPort1.WriteLine(str);
            // s24
            s24 = this.s24text.Text;
            str = "$24=";
            str += s24;
            ((Form1)this.Owner).serialPort1.WriteLine(str);
            // s25
            s25 = this.s25text.Text;
            str = "$25=";
            str += s25;
            ((Form1)this.Owner).serialPort1.WriteLine(str);
            // s26
            s26 = this.s26text.Text;
            str = "$26=";
            str += s26;
            ((Form1)this.Owner).serialPort1.WriteLine(str);
            // s27
            s27 = this.s27text.Text;
            str = "$27=";
            str += s27;
            ((Form1)this.Owner).serialPort1.WriteLine(str);
            // s130
            s130 = this.s130text.Text;
            str = "$130=";
            str += s130;
            ((Form1)this.Owner).serialPort1.WriteLine(str);
            // 131
            s27 = this.s131text.Text;
            str = "$131=";
            str += s131;
            ((Form1)this.Owner).serialPort1.WriteLine(str);
            // s132
            s27 = this.s132text.Text;
            str = "$132=";
            str += s132;
            ((Form1)this.Owner).serialPort1.WriteLine(str);


            if (flag)
                MessageBox.Show("OK");
        }

        private void label4_Click(object sender, EventArgs e)
        {

        }

        private void textBox2_TextChanged(object sender, EventArgs e)
        {

        }

        private void DataReceive()
        {

            if (((Form1)this.Owner).InputData != String.Empty)
            {  
                // s0
                int x = ((Form1)this.Owner).InputData.IndexOf("$0=");
                s0=((Form1)this.Owner).InputData.Substring(x + 3, 3);
                
                // s1
                x = ((Form1)this.Owner).InputData.IndexOf("$1=");
                s1 = ((Form1)this.Owner).InputData.Substring(x + 3, 3);
                // s3
                x = ((Form1)this.Owner).InputData.IndexOf("$3=");
                s3 = ((Form1)this.Owner).InputData.Substring(x + 3, 2);
                // s5
                x = ((Form1)this.Owner).InputData.IndexOf("$5=");
                s5 = ((Form1)this.Owner).InputData.Substring(x + 3, 1);
                // s12
                x = ((Form1)this.Owner).InputData.IndexOf("$12=");
                s12 = ((Form1)this.Owner).InputData.Substring(x + 4, 5);
                // s13
                x = ((Form1)this.Owner).InputData.IndexOf("$13=");
                s13 = ((Form1)this.Owner).InputData.Substring(x + 4, 1);
                // s20
                x = ((Form1)this.Owner).InputData.IndexOf("$20=");
                s20 = ((Form1)this.Owner).InputData.Substring(x + 4, 1);
                // s21
                x = ((Form1)this.Owner).InputData.IndexOf("$21=");
                s21 = ((Form1)this.Owner).InputData.Substring(x + 4, 1);
                // s23
                x = ((Form1)this.Owner).InputData.IndexOf("$23=");
                s23 = ((Form1)this.Owner).InputData.Substring(x + 4, 2);
                // s24
                x = ((Form1)this.Owner).InputData.IndexOf("$24=");
                s24 = ((Form1)this.Owner).InputData.Substring(x + 4, 6);
                // s25
                x = ((Form1)this.Owner).InputData.IndexOf("$25=");
                s25 = ((Form1)this.Owner).InputData.Substring(x + 4, 7);
                // s26
                x = ((Form1)this.Owner).InputData.IndexOf("$26=");
                s26 = ((Form1)this.Owner).InputData.Substring(x + 4, 3);
                // s27
                x = ((Form1)this.Owner).InputData.IndexOf("$27=");
                s27 = ((Form1)this.Owner).InputData.Substring(x + 4, 5);
                // s130
                x = ((Form1)this.Owner).InputData.IndexOf("$130=");
                s130 = ((Form1)this.Owner).InputData.Substring(x + 5, 7);
                // s131
                x = ((Form1)this.Owner).InputData.IndexOf("$131=");
                s131 = ((Form1)this.Owner).InputData.Substring(x + 5, 7);
                // s132
                x = ((Form1)this.Owner).InputData.IndexOf("$132=");
                s132 = ((Form1)this.Owner).InputData.Substring(x + 5, 7);


                SetText();
            }
        }

        private void SetText()
        {
            this.s0text.Text = s0;
            this.s1text.Text = s1;
            this.s3text.Text = s3;
            this.s5text.Text = s5;
            this.s12text.Text = s12;
            this.s13text.Text = s13;
            this.s20text.Text = s20;
            this.s21text.Text = s21;
            this.s23text.Text = s23;
            this.s24text.Text = s24;
            this.s25text.Text = s25;
            this.s26text.Text = s26;
            this.s27text.Text = s27;
            this.s130text.Text = s130;
            this.s131text.Text = s131;
            this.s132text.Text = s132;



        }
        private void comboBox1_SelectedIndexChanged(object sender, EventArgs e)
        {

        }

        public void button1_Click(object sender, EventArgs e)
        {
            ((Form1)this.Owner).serialPort1.WriteLine("$$");
            Thread.Sleep(200);
            DataReceive();
        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {
            
        }

        private void button2_Click(object sender, EventArgs e)
        {
            
        }

        private void label2_Click(object sender, EventArgs e)
        {

        }
    }
}

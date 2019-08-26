using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.IO;
using System.IO.Ports;
using System.Xml;
using System.Threading;
using System.Timers;





namespace WindowsFormsApp1
{
    public partial class Form1 : Form
    {
        public string InputData = String.Empty; // Khai báo string buff dùng cho hiển thị dữ liệu sau này.
        delegate void SetTextCallback(string text); // Khai bao delegate SetTextCallBack voi tham so string
       
        Form frm2 = new Form2();
        public Form1()
        {
            InitializeComponent();
            serialPort1.DataReceived += new SerialDataReceivedEventHandler(DataReceive);
            string[] BaudRate = { "1200", "2400", "4800", "9600", "19200", "38400", "57600", "115200" };
            comboBox2.Items.AddRange(BaudRate);// Thiết lập cho comboBox2
            comboBox3.Text = "1";
            string[] speed = { "1", "2", "3", "4", "5" };
            comboBox4.Items.AddRange(speed);
        }

        private void button1_Click(object sender, EventArgs e)
        {
            SetText("left: ");
            string str;
            str = "G91 G0  X-";
            str += comboBox3.Text;
            serialPort1.WriteLine(str);
        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {

        }

        public void button2_Click(object sender, EventArgs e)
        {
            SetText("up: ");
            string str;
            str = "G91 G0  Y";
            str += comboBox3.Text;
            serialPort1.WriteLine(str);
            
        }

        private void textBox2_TextChanged(object sender, EventArgs e)
        {
            textBox2.SelectionStart = textBox2 .TextLength;
            textBox2.ScrollToCaret();
        }

        private void comboBox2_SelectedIndexChanged(object sender, EventArgs e)
        {

        }

        private void Form1_Load(object sender, EventArgs e)
        {
            comboBox1.DataSource = SerialPort.GetPortNames();
            comboBox2.SelectedIndex = 7;
            comboBox4.SelectedIndex = 4;
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            if (!serialPort1.IsOpen)
            {
                tat.Enabled = false;
                mo.Enabled = true;

                up.Enabled = false;
                down.Enabled = false;
                right.Enabled = false;
                left.Enabled = false;
                zup.Enabled = false;
                zdown.Enabled = false;
                camera.Enabled = false;
                file.Enabled = false;
                //send.Enabled = false;
                unlock.Enabled = false;
                resetx.Enabled = false;
                resety.Enabled = false;
                resetz.Enabled = false;
                home.Enabled = false;
                comboBox4.Enabled = false;
                comboBox3.Enabled = false;
                //comboBox2.Enabled = false;
                //comboBox1.Enabled = false;
                button1.Enabled = false;
                button2.Enabled = false;
                button3.Enabled = false;
            }
            else if (serialPort1.IsOpen)
            {
                tat.Enabled = true;
                mo.Enabled = false;

                up.Enabled = true;
                down.Enabled = true;
                right.Enabled = true;
                left.Enabled = true;
                zup.Enabled = true;
                zdown.Enabled = true;
                camera.Enabled = true;
                file.Enabled = true;
                //send.Enabled = true;
                unlock.Enabled = true;
                resetx.Enabled = true;
                resety.Enabled = true;
                resetz.Enabled = true;
                home.Enabled = true;
                comboBox4.Enabled = true;
                comboBox3.Enabled = true;
                comboBox2.Enabled = true;
                comboBox1.Enabled = true;
                button1.Enabled = true;
                button2.Enabled = true;
                button3.Enabled = true;
            }
            if (check)
            {
                send.Enabled = true;
            }
        }

        private void DataReceive(object obj, SerialDataReceivedEventArgs e)
        {
            Thread.Sleep(100);
            InputData = serialPort1.ReadExisting();
            if (InputData != String.Empty)
            {
                SetText(InputData);

                //MessageBox.Show(InputData.ToString());
                if (InputData.ToString().IndexOf("ok") != -1)
                {
                    if (!send.Enabled)
                    {
                        //myTimer.AutoReset = true;
                        //myTimer.Enabled = true;
                        RunThis();
                    }
                }

                if (InputData.ToString().IndexOf("Value < 0") != -1)
                {
                    serialPort1.WriteLine("~");
                }



            }

        }

        private void SetText(string text)
        {
            if (this.textBox2.InvokeRequired)
            {
                SetTextCallback d = new SetTextCallback(SetText); // khởi tạo 1 delegate mới gọi đến SetText
                this.Invoke(d, new object[] { text });
            }
            else
            {
                this.textBox2.Text += text;
               // ((Form2)this.Owner).textBox1.Text += text;
            }
        }
        private void mo_Click(object sender, EventArgs e)
        {
            try
            {
                serialPort1.PortName = comboBox1.Text;
                serialPort1.BaudRate = Convert.ToInt32(comboBox2.Text);
                serialPort1.Open();
                serialPort1.WriteLine("$X");
            }
            catch
            {
                MessageBox.Show("thu lai");
            }
        }

        private void tat_Click(object sender, EventArgs e)
        {
            try
            {
                serialPort1.Close();
            }
            catch
            {
                MessageBox.Show("thu lai");
            }
        }





        private void textBox3_TextChanged(object sender, EventArgs e)
        {

        }
    
        private void textBox3_KeyDown(object sender, KeyEventArgs e)
        {
            if (serialPort1.IsOpen)
            {
                if (e.KeyCode == Keys.Enter)
                {
                    serialPort1.WriteLine(textBox3.Text);
                    textBox3.Clear();
                }
            }
        }

        private void xuong_Click(object sender, EventArgs e)
        {
            SetText("down: ");
            string str;
            str = "G91 G0  Y-";
            str += comboBox3.Text;
            serialPort1.WriteLine(str);
            
        }

        private void phai_Click(object sender, EventArgs e)
        {
            SetText("right: ");
            string str;
            str = "G91 G0  X";
            str += comboBox3.Text;   
            serialPort1.WriteLine(str);
            
        }

        private void file_Click(object sender, EventArgs e)
        {
            OpenFileDialog uploadFileSteam = new OpenFileDialog();
            uploadFileSteam.InitialDirectory = "c:\\";
            uploadFileSteam.Title = "file";
            if (uploadFileSteam.ShowDialog() == DialogResult.OK)
            {
                textBox1.Text = uploadFileSteam.FileName;//đường dẫn của file trong textbox
            }
        }

        string[] lines;
        int i;
        private void send_Click(object sender, EventArgs e)
        {
            lines = File.ReadAllLines(textBox1.Text);            
            flag = false;
            send.Enabled = false;
            RunThis();
            check = false;
            //send.Enabled = true;

        }

     
        //private void RunThis(object source, ElapsedEventArgs e)
        bool flag,check;

        private void RunThis()       {

            if (!flag)
            {
                for (i = 0; i < 5; i++)
                {
                    serialPort1.WriteLine(lines[i]);
                }
                flag = true;

            }

            else
            {
                if (i < lines.Length)
                {
                    serialPort1.WriteLine(lines[i]);
                    i++;
                }
                else
                    check = true;
                    
            }


        }

        private void myTimer_Tick()
        {
            //i++;
            //MessageBox.Show("1");
            //if (i < lines.Length)
            //{
            //    serialPort1.WriteLine(lines[i]);

            //    timer2.Enabled = false;

            //    MessageBox.Show(lines[i]);

            //}
            //else
            //    MessageBox.Show("Done");
            myTimer.Stop();
            myTimer.Enabled = true;

            MessageBox.Show("OK");

        }

        static System.Timers.Timer myTimer = new System.Timers.Timer();
 

        // This is the method to run when the timer is raised.
        public static void TimerEventProcessor(Object myObject,EventArgs myEventArgs)
        {
            myTimer.Stop();
            myTimer.Enabled = true;

            MessageBox.Show("OK");
            //myTimer.Enabled = false; ;


        }

        private void button2_Click_1(object sender, EventArgs e)
        {
            SetText("Zdown: ");
            string str;
            str = "G91 G0  Z-";
            str += comboBox3.Text;
            serialPort1.WriteLine(str);
            //serialPort1.WriteLine("G91 G0 Z-1");
        }

        private void button3_Click(object sender, EventArgs e)
        {
            SetText("unlock: ");
            serialPort1.WriteLine("$X");
        }
        int x = 0;
        
        private void write()
        {
            Thread.Sleep(2000);
            int k = 0;
            bool l=true;

            while (x != 1)
            {
                if (k < 200)
                {
                    if (x==2)
                    {
                        x = 1;
                        MessageBox.Show("camera error");
                    }
                    if (l == true)
                    {
                        Thread.Sleep(30);
                        serialPort1.WriteLine("G91 G0 x0.1");
                        k++;
                    }
                    else
                    {
                        Thread.Sleep(30);
                        serialPort1.WriteLine("G91 G0 x-0.1");
                        k++;
                    }
                }
                else
                {
                    Thread.Sleep(30);
                    serialPort1.WriteLine("G91 G0 y1");
                    k = 0;
                    if (l == true) l = false;
                    else l = true;
                }
               
            }
        }

        private void button5_Click(object sender, EventArgs e)
        {
            SetText("reset x,y: ");
            serialPort1.WriteLine("G10 P0 L20 X0");
            serialPort1.WriteLine("G10 P0 L20 Y0");
        }

        private void settingToolStripMenuItem_Click(object sender, EventArgs e)
        {
           
            Form frm = new Form2();
            frm.Show(this);
            //serialPort1.WriteLine("$$");
        }

        private void resety_Click(object sender, EventArgs e)
        {
            SetText("pause: ");
            serialPort1.WriteLine("!");
        }

        private void resetz_Click(object sender, EventArgs e)
        {
            SetText("reset z: ");
            serialPort1.WriteLine("G10 P0 L20 Z0");
        }

        private void home_Click(object sender, EventArgs e)
        {
            SetText("home: ");
            serialPort1.WriteLine("$H");
        }

        private void calibrationToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Form frm3 = new Form3();
            frm3.Show(this);
        }

        private void button3_Click_1(object sender, EventArgs e)
        {
            serialPort1.Write(new byte[] { 0x18 }, 0, 1);
        }

        private void button1_Click_2(object sender, EventArgs e)
        {
            SetText("resume: ");
            serialPort1.WriteLine("~");
        }

        private void comboBox3_SelectedIndexChanged(object sender, EventArgs e)
        {

        }

        private void menuStrip1_ItemClicked(object sender, ToolStripItemClickedEventArgs e)
        {

        }

        private void comboBox4_SelectedIndexChanged(object sender, EventArgs e)
        {
            if (!mo.Enabled)
            {
                int x;
                x = Convert.ToInt32(this.comboBox4.Text);
                if (x == 1)
                {
                    serialPort1.WriteLine("$110=100");
                    Thread.Sleep(50);
                    serialPort1.WriteLine("$111=100");
                }
                if (x == 2)
                {
                    serialPort1.WriteLine("$110=200");
                    Thread.Sleep(50);
                    serialPort1.WriteLine("$111=200");
                }
                if (x == 3)
                {
                    serialPort1.WriteLine("$110=300");
                    Thread.Sleep(50);
                    serialPort1.WriteLine("$111=300");
                }
                if (x == 4)
                {
                    serialPort1.WriteLine("$110=400");
                    Thread.Sleep(50);
                    serialPort1.WriteLine("$111=400");
                }
                if (x == 5)
                {
                    serialPort1.WriteLine("$110=500");
                    Thread.Sleep(50);
                    serialPort1.WriteLine("$111=500");
                }
            }
        }

        private void button2_Click_2(object sender, EventArgs e)
        {
            send.Enabled = true;
            serialPort1.Write(new byte[] { 0x18 }, 0, 1);
        }

        private void button4_Click(object sender, EventArgs e)
        {
            x = 0;
           serialPort1.WriteLine("G91 G0  Z-55");
            Thread.Sleep(3500);
            Thread workThread = new Thread(write);
            workThread.Start();
            ClassLibrary1.XLA obj = new ClassLibrary1.XLA();
            x = obj.checkingMark();
            
            Thread.Sleep(20);
            serialPort1.WriteLine("G10 P0 L20 X0 Y0 Z0");
            Thread.Sleep(100);
            serialPort1.WriteLine("G10 P0 L20 X18 Y73 Z0");





        }

        private void button1_Click_1(object sender, EventArgs e)
        {
            SetText("Zup: ");
            string str;
            str = "G91 G0  Z";
            str += comboBox3.Text;
            serialPort1.WriteLine(str);
            //serialPort1.WriteLine("G91 G0 Z1");
        }

        private void comboBox1_SelectedIndexChanged(object sender, EventArgs e)
        {

        }

        private void label1_Click(object sender, EventArgs e)
        {
       
        }
    }


    }
    


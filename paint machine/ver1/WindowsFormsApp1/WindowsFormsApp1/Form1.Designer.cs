namespace WindowsFormsApp1
{
    partial class Form1
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.components = new System.ComponentModel.Container();
            this.left = new System.Windows.Forms.Button();
            this.textBox1 = new System.Windows.Forms.TextBox();
            this.textBox2 = new System.Windows.Forms.TextBox();
            this.up = new System.Windows.Forms.Button();
            this.down = new System.Windows.Forms.Button();
            this.right = new System.Windows.Forms.Button();
            this.mo = new System.Windows.Forms.Button();
            this.tat = new System.Windows.Forms.Button();
            this.file = new System.Windows.Forms.Button();
            this.send = new System.Windows.Forms.Button();
            this.timer1 = new System.Windows.Forms.Timer(this.components);
            this.serialPort1 = new System.IO.Ports.SerialPort(this.components);
            this.comboBox1 = new System.Windows.Forms.ComboBox();
            this.comboBox2 = new System.Windows.Forms.ComboBox();
            this.textBox3 = new System.Windows.Forms.TextBox();
            this.timer2 = new System.Windows.Forms.Timer(this.components);
            this.zup = new System.Windows.Forms.Button();
            this.zdown = new System.Windows.Forms.Button();
            this.label1 = new System.Windows.Forms.Label();
            this.unlock = new System.Windows.Forms.Button();
            this.camera = new System.Windows.Forms.Button();
            this.resetx = new System.Windows.Forms.Button();
            this.menuStrip1 = new System.Windows.Forms.MenuStrip();
            this.menuToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.settingToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.calibrationToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.resety = new System.Windows.Forms.Button();
            this.resetz = new System.Windows.Forms.Button();
            this.home = new System.Windows.Forms.Button();
            this.button1 = new System.Windows.Forms.Button();
            this.button2 = new System.Windows.Forms.Button();
            this.button3 = new System.Windows.Forms.Button();
            this.comboBox3 = new System.Windows.Forms.ComboBox();
            this.comboBox4 = new System.Windows.Forms.ComboBox();
            this.label2 = new System.Windows.Forms.Label();
            this.label3 = new System.Windows.Forms.Label();
            this.menuStrip1.SuspendLayout();
            this.SuspendLayout();
            // 
            // left
            // 
            this.left.Location = new System.Drawing.Point(457, 183);
            this.left.Name = "left";
            this.left.Size = new System.Drawing.Size(75, 23);
            this.left.TabIndex = 0;
            this.left.Text = "left";
            this.left.UseVisualStyleBackColor = true;
            this.left.Click += new System.EventHandler(this.button1_Click);
            // 
            // textBox1
            // 
            this.textBox1.Location = new System.Drawing.Point(12, 357);
            this.textBox1.Name = "textBox1";
            this.textBox1.Size = new System.Drawing.Size(776, 20);
            this.textBox1.TabIndex = 1;
            this.textBox1.TextChanged += new System.EventHandler(this.textBox1_TextChanged);
            // 
            // textBox2
            // 
            this.textBox2.Location = new System.Drawing.Point(12, 99);
            this.textBox2.Multiline = true;
            this.textBox2.Name = "textBox2";
            this.textBox2.ReadOnly = true;
            this.textBox2.ScrollBars = System.Windows.Forms.ScrollBars.Vertical;
            this.textBox2.Size = new System.Drawing.Size(439, 223);
            this.textBox2.TabIndex = 2;
            this.textBox2.TextChanged += new System.EventHandler(this.textBox2_TextChanged);
            // 
            // up
            // 
            this.up.Cursor = System.Windows.Forms.Cursors.No;
            this.up.Location = new System.Drawing.Point(527, 146);
            this.up.Name = "up";
            this.up.Size = new System.Drawing.Size(75, 23);
            this.up.TabIndex = 3;
            this.up.Text = "up";
            this.up.UseVisualStyleBackColor = true;
            this.up.Click += new System.EventHandler(this.button2_Click);
            // 
            // down
            // 
            this.down.Location = new System.Drawing.Point(527, 222);
            this.down.Name = "down";
            this.down.Size = new System.Drawing.Size(75, 23);
            this.down.TabIndex = 4;
            this.down.Text = "down";
            this.down.UseVisualStyleBackColor = true;
            this.down.Click += new System.EventHandler(this.xuong_Click);
            // 
            // right
            // 
            this.right.Location = new System.Drawing.Point(600, 183);
            this.right.Name = "right";
            this.right.Size = new System.Drawing.Size(75, 23);
            this.right.TabIndex = 5;
            this.right.Text = "right";
            this.right.UseVisualStyleBackColor = true;
            this.right.Click += new System.EventHandler(this.phai_Click);
            // 
            // mo
            // 
            this.mo.Location = new System.Drawing.Point(297, 37);
            this.mo.Name = "mo";
            this.mo.Size = new System.Drawing.Size(75, 23);
            this.mo.TabIndex = 6;
            this.mo.Text = "open";
            this.mo.UseVisualStyleBackColor = true;
            this.mo.Click += new System.EventHandler(this.mo_Click);
            // 
            // tat
            // 
            this.tat.Location = new System.Drawing.Point(390, 37);
            this.tat.Name = "tat";
            this.tat.Size = new System.Drawing.Size(75, 23);
            this.tat.TabIndex = 7;
            this.tat.Text = "close";
            this.tat.UseVisualStyleBackColor = true;
            this.tat.Click += new System.EventHandler(this.tat_Click);
            // 
            // file
            // 
            this.file.Location = new System.Drawing.Point(12, 397);
            this.file.Name = "file";
            this.file.Size = new System.Drawing.Size(75, 23);
            this.file.TabIndex = 8;
            this.file.Text = "file";
            this.file.UseVisualStyleBackColor = true;
            this.file.Click += new System.EventHandler(this.file_Click);
            // 
            // send
            // 
            this.send.Location = new System.Drawing.Point(100, 397);
            this.send.Name = "send";
            this.send.Size = new System.Drawing.Size(75, 23);
            this.send.TabIndex = 9;
            this.send.Text = "start";
            this.send.UseVisualStyleBackColor = true;
            this.send.Click += new System.EventHandler(this.send_Click);
            // 
            // timer1
            // 
            this.timer1.Enabled = true;
            this.timer1.Tick += new System.EventHandler(this.timer1_Tick);
            // 
            // serialPort1
            // 
            this.serialPort1.BaudRate = 115200;
            this.serialPort1.PortName = "COM4";
            // 
            // comboBox1
            // 
            this.comboBox1.FormattingEnabled = true;
            this.comboBox1.Location = new System.Drawing.Point(490, 39);
            this.comboBox1.Name = "comboBox1";
            this.comboBox1.Size = new System.Drawing.Size(121, 21);
            this.comboBox1.TabIndex = 10;
            this.comboBox1.SelectedIndexChanged += new System.EventHandler(this.comboBox1_SelectedIndexChanged);
            // 
            // comboBox2
            // 
            this.comboBox2.FormattingEnabled = true;
            this.comboBox2.Location = new System.Drawing.Point(636, 39);
            this.comboBox2.Name = "comboBox2";
            this.comboBox2.Size = new System.Drawing.Size(121, 21);
            this.comboBox2.TabIndex = 11;
            this.comboBox2.SelectedIndexChanged += new System.EventHandler(this.comboBox2_SelectedIndexChanged);
            // 
            // textBox3
            // 
            this.textBox3.Location = new System.Drawing.Point(478, 99);
            this.textBox3.Name = "textBox3";
            this.textBox3.Size = new System.Drawing.Size(297, 20);
            this.textBox3.TabIndex = 12;
            this.textBox3.TextChanged += new System.EventHandler(this.textBox3_TextChanged);
            this.textBox3.KeyDown += new System.Windows.Forms.KeyEventHandler(this.textBox3_KeyDown);
            // 
            // timer2
            // 
            this.timer2.Interval = 2000;
            // 
            // zup
            // 
            this.zup.Location = new System.Drawing.Point(700, 146);
            this.zup.Name = "zup";
            this.zup.Size = new System.Drawing.Size(75, 23);
            this.zup.TabIndex = 13;
            this.zup.Text = "Zup";
            this.zup.UseVisualStyleBackColor = true;
            this.zup.Click += new System.EventHandler(this.button1_Click_1);
            // 
            // zdown
            // 
            this.zdown.Location = new System.Drawing.Point(700, 222);
            this.zdown.Name = "zdown";
            this.zdown.Size = new System.Drawing.Size(75, 23);
            this.zdown.TabIndex = 14;
            this.zdown.Text = "Zdown";
            this.zdown.UseVisualStyleBackColor = true;
            this.zdown.Click += new System.EventHandler(this.button2_Click_1);
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(34, 37);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(0, 13);
            this.label1.TabIndex = 15;
            this.label1.Click += new System.EventHandler(this.label1_Click);
            // 
            // unlock
            // 
            this.unlock.Location = new System.Drawing.Point(12, 32);
            this.unlock.Name = "unlock";
            this.unlock.Size = new System.Drawing.Size(75, 23);
            this.unlock.TabIndex = 16;
            this.unlock.Text = "unlock";
            this.unlock.UseVisualStyleBackColor = true;
            this.unlock.Click += new System.EventHandler(this.button3_Click);
            // 
            // camera
            // 
            this.camera.Location = new System.Drawing.Point(490, 316);
            this.camera.Name = "camera";
            this.camera.Size = new System.Drawing.Size(75, 23);
            this.camera.TabIndex = 17;
            this.camera.Text = "camera";
            this.camera.UseVisualStyleBackColor = true;
            this.camera.Click += new System.EventHandler(this.button4_Click);
            // 
            // resetx
            // 
            this.resetx.Location = new System.Drawing.Point(525, 397);
            this.resetx.Name = "resetx";
            this.resetx.Size = new System.Drawing.Size(75, 23);
            this.resetx.TabIndex = 18;
            this.resetx.Text = "reset x,y";
            this.resetx.UseVisualStyleBackColor = true;
            this.resetx.Click += new System.EventHandler(this.button5_Click);
            // 
            // menuStrip1
            // 
            this.menuStrip1.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.menuToolStripMenuItem});
            this.menuStrip1.Location = new System.Drawing.Point(0, 0);
            this.menuStrip1.Name = "menuStrip1";
            this.menuStrip1.Size = new System.Drawing.Size(834, 24);
            this.menuStrip1.TabIndex = 19;
            this.menuStrip1.Text = "menuStrip1";
            this.menuStrip1.ItemClicked += new System.Windows.Forms.ToolStripItemClickedEventHandler(this.menuStrip1_ItemClicked);
            // 
            // menuToolStripMenuItem
            // 
            this.menuToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.settingToolStripMenuItem,
            this.calibrationToolStripMenuItem});
            this.menuToolStripMenuItem.Name = "menuToolStripMenuItem";
            this.menuToolStripMenuItem.Size = new System.Drawing.Size(50, 20);
            this.menuToolStripMenuItem.Text = "Menu";
            // 
            // settingToolStripMenuItem
            // 
            this.settingToolStripMenuItem.Name = "settingToolStripMenuItem";
            this.settingToolStripMenuItem.Size = new System.Drawing.Size(130, 22);
            this.settingToolStripMenuItem.Text = "Setting";
            this.settingToolStripMenuItem.Click += new System.EventHandler(this.settingToolStripMenuItem_Click);
            // 
            // calibrationToolStripMenuItem
            // 
            this.calibrationToolStripMenuItem.Name = "calibrationToolStripMenuItem";
            this.calibrationToolStripMenuItem.Size = new System.Drawing.Size(130, 22);
            this.calibrationToolStripMenuItem.Text = "calibration";
            this.calibrationToolStripMenuItem.Click += new System.EventHandler(this.calibrationToolStripMenuItem_Click);
            // 
            // resety
            // 
            this.resety.Location = new System.Drawing.Point(191, 397);
            this.resety.Name = "resety";
            this.resety.Size = new System.Drawing.Size(75, 23);
            this.resety.TabIndex = 20;
            this.resety.Text = "pause";
            this.resety.UseVisualStyleBackColor = true;
            this.resety.Click += new System.EventHandler(this.resety_Click);
            // 
            // resetz
            // 
            this.resetz.Location = new System.Drawing.Point(616, 397);
            this.resetz.Name = "resetz";
            this.resetz.Size = new System.Drawing.Size(75, 23);
            this.resetz.TabIndex = 21;
            this.resetz.Text = "reset z";
            this.resetz.UseVisualStyleBackColor = true;
            this.resetz.Click += new System.EventHandler(this.resetz_Click);
            // 
            // home
            // 
            this.home.Location = new System.Drawing.Point(100, 32);
            this.home.Name = "home";
            this.home.Size = new System.Drawing.Size(75, 23);
            this.home.TabIndex = 22;
            this.home.Text = "home";
            this.home.UseVisualStyleBackColor = true;
            this.home.Click += new System.EventHandler(this.home_Click);
            // 
            // button1
            // 
            this.button1.Location = new System.Drawing.Point(283, 397);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(75, 23);
            this.button1.TabIndex = 23;
            this.button1.Text = "resume";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click_2);
            // 
            // button2
            // 
            this.button2.Location = new System.Drawing.Point(376, 397);
            this.button2.Name = "button2";
            this.button2.Size = new System.Drawing.Size(75, 23);
            this.button2.TabIndex = 24;
            this.button2.Text = "cancel";
            this.button2.UseVisualStyleBackColor = true;
            this.button2.Click += new System.EventHandler(this.button2_Click_2);
            // 
            // button3
            // 
            this.button3.Location = new System.Drawing.Point(191, 32);
            this.button3.Name = "button3";
            this.button3.Size = new System.Drawing.Size(75, 23);
            this.button3.TabIndex = 25;
            this.button3.Text = "soft reset";
            this.button3.UseVisualStyleBackColor = true;
            this.button3.Click += new System.EventHandler(this.button3_Click_1);
            // 
            // comboBox3
            // 
            this.comboBox3.FormattingEnabled = true;
            this.comboBox3.Location = new System.Drawing.Point(654, 272);
            this.comboBox3.Name = "comboBox3";
            this.comboBox3.Size = new System.Drawing.Size(121, 21);
            this.comboBox3.TabIndex = 26;
            this.comboBox3.SelectedIndexChanged += new System.EventHandler(this.comboBox3_SelectedIndexChanged);
            // 
            // comboBox4
            // 
            this.comboBox4.FormattingEnabled = true;
            this.comboBox4.Location = new System.Drawing.Point(654, 316);
            this.comboBox4.Name = "comboBox4";
            this.comboBox4.Size = new System.Drawing.Size(121, 21);
            this.comboBox4.TabIndex = 27;
            this.comboBox4.SelectedIndexChanged += new System.EventHandler(this.comboBox4_SelectedIndexChanged);
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(597, 280);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(52, 13);
            this.label2.TabIndex = 28;
            this.label2.Text = "step (mm)";
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(597, 316);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(36, 13);
            this.label3.TabIndex = 29;
            this.label3.Text = "speed";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(834, 450);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.comboBox4);
            this.Controls.Add(this.comboBox3);
            this.Controls.Add(this.button3);
            this.Controls.Add(this.button2);
            this.Controls.Add(this.button1);
            this.Controls.Add(this.home);
            this.Controls.Add(this.resetz);
            this.Controls.Add(this.resety);
            this.Controls.Add(this.resetx);
            this.Controls.Add(this.camera);
            this.Controls.Add(this.unlock);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.zdown);
            this.Controls.Add(this.zup);
            this.Controls.Add(this.textBox3);
            this.Controls.Add(this.comboBox2);
            this.Controls.Add(this.comboBox1);
            this.Controls.Add(this.send);
            this.Controls.Add(this.file);
            this.Controls.Add(this.tat);
            this.Controls.Add(this.mo);
            this.Controls.Add(this.right);
            this.Controls.Add(this.down);
            this.Controls.Add(this.up);
            this.Controls.Add(this.textBox2);
            this.Controls.Add(this.textBox1);
            this.Controls.Add(this.left);
            this.Controls.Add(this.menuStrip1);
            this.MainMenuStrip = this.menuStrip1;
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.menuStrip1.ResumeLayout(false);
            this.menuStrip1.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button left;
        private System.Windows.Forms.TextBox textBox1;
        private System.Windows.Forms.Button up;
        private System.Windows.Forms.Button down;
        private System.Windows.Forms.Button right;
        private System.Windows.Forms.Button mo;
        private System.Windows.Forms.Button tat;
        private System.Windows.Forms.Button file;
        private System.Windows.Forms.Button send;
        private System.Windows.Forms.ComboBox comboBox1;
        private System.Windows.Forms.ComboBox comboBox2;
        private System.Windows.Forms.TextBox textBox3;
        private System.Windows.Forms.Timer timer2;
        private System.Windows.Forms.Button zup;
        private System.Windows.Forms.Button zdown;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Button unlock;
        private System.Windows.Forms.Button camera;
        private System.Windows.Forms.Button resetx;
        private System.Windows.Forms.MenuStrip menuStrip1;
        private System.Windows.Forms.ToolStripMenuItem menuToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem settingToolStripMenuItem;
        public System.IO.Ports.SerialPort serialPort1;
        public System.Windows.Forms.Timer timer1;
        public System.Windows.Forms.TextBox textBox2;
        private System.Windows.Forms.Button resety;
        private System.Windows.Forms.Button resetz;
        private System.Windows.Forms.Button home;
        private System.Windows.Forms.ToolStripMenuItem calibrationToolStripMenuItem;
        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.Button button2;
        private System.Windows.Forms.Button button3;
        private System.Windows.Forms.ComboBox comboBox3;
        private System.Windows.Forms.ComboBox comboBox4;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label label3;
    }
}


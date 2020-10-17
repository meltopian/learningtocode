Public Class Form1
	Private Sub Label1_Click(sender As Object, e As EventArgs) Handles Label1.Click

	End Sub

	Private Sub Button1_Click(sender As Object, e As EventArgs) Handles Button1.Click
		Label1.Text = "YOU PUSHED IT!!!!"

	End Sub

	Private Sub Button2_Click(sender As Object, e As EventArgs) Handles Button2.Click
		Label1.Text = "OK but you just pushed it though"
	End Sub

	Private Sub Button3_Click(sender As Object, e As EventArgs) Handles Button3.Click
		Label1.Visible = False
	End Sub

	Private Sub Button4_Click(sender As Object, e As EventArgs) Handles Button4.Click
		Label1.Visible = True
	End Sub

	Private Sub Button5_Click(sender As Object, e As EventArgs) Handles Button5.Click
		Label1.Text = "I'mma gettin' angry"
		Label1.ForeColor = Color.Black
		Label1.BackColor = Color.Red
	End Sub

	Private Sub TextBox1_TextChanged(sender As Object, e As EventArgs) Handles TextBox1.TextChanged

	End Sub

	Private Sub Button6_Click(sender As Object, e As EventArgs) Handles Button6.Click
		TextBox2.Text = TextBox1.Text + "is copied"
	End Sub

	Private Sub Form1_Load(sender As Object, e As EventArgs) Handles MyBase.Load

	End Sub

	Private Sub Button7_Click(sender As Object, e As EventArgs) Handles Button7.Click
		CheckBox1.Checked = True
		CheckBox2.Checked = True
	End Sub
End Class

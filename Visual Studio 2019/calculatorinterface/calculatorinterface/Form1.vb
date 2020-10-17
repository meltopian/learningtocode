Imports System.Windows.Forms.VisualStyles

Public Class Form1
	Private Sub Button13_Click(sender As Object, e As EventArgs) Handles ClearButton.Click
		TextBox1.Clear()
	End Sub

	Private Sub Button1_Click(sender As Object, e As EventArgs) Handles ThreeButton.Click
		TextBox1.AppendText("3")
	End Sub

	Private Sub SevenButton_Click(sender As Object, e As EventArgs) Handles SevenButton.Click
		TextBox1.AppendText("7")
	End Sub

	Private Sub EightButton_Click(sender As Object, e As EventArgs) Handles EightButton.Click
		TextBox1.AppendText("8")
	End Sub

	Private Sub NineButton_Click(sender As Object, e As EventArgs) Handles NineButton.Click
		TextBox1.AppendText("9")
	End Sub

	Private Sub FourButton_Click(sender As Object, e As EventArgs) Handles FourButton.Click
		TextBox1.AppendText("4")
	End Sub

	Private Sub FiveButton_Click(sender As Object, e As EventArgs) Handles FiveButton.Click
		TextBox1.AppendText("5")
	End Sub

	Private Sub SixButton_Click(sender As Object, e As EventArgs) Handles SixButton.Click
		TextBox1.AppendText("6")
	End Sub

	Private Sub OneButton_Click(sender As Object, e As EventArgs) Handles OneButton.Click
		TextBox1.AppendText("1")
	End Sub

	Private Sub Button1_Click_1(sender As Object, e As EventArgs) Handles ZeroButton.Click
		TextBox1.AppendText("0")
	End Sub

	Private Sub TwoButton_Click(sender As Object, e As EventArgs) Handles TwoButton.Click
		TextBox1.AppendText("2")
	End Sub

	Private Sub PlusButton_Click(sender As Object, e As EventArgs) Handles PlusButton.Click
		TextBox1.AppendText(" + ")
	End Sub


	Private Sub EqualButton_Click(sender As Object, e As EventArgs) Handles EqualButton.Click
		Dim numbersinput As String
		'Dim firstpart As Integer
		'Dim secondpart As String
		'Dim thirdpart As Integer
		'Dim answer As Integer

		numbersinput(2) = "1 + 1"
		numbersinput = TextBox1.Text

		'answer = Val(numbersinput & "69")
		Dim line_split() = numbersinput.Split(" ")

		'Const numbersinput As String = "1,+,1"

		'If Something(1) = +
		'	something = Console.ReadLine()
		'TextBox1_TextChanged(Val(TextBox1.Text) + Val(TextBox2.Text))
		'Dim line_split() = csv_line_test.Split(",")
		'Console.WriteLine(numbersinput)

		'to use float numbers use "As Double" instead of "As Integer")
		'TextBox1.Text = answer
		Console.WriteLine(line_split)



	End Sub

	Private Sub MinusButton_Click(sender As Object, e As EventArgs) Handles MinusButton.Click
		TextBox1.AppendText(" - ")
	End Sub

	Private Sub TextBox1_TextChanged(sender As Object, e As EventArgs) Handles TextBox1.TextChanged

	End Sub

	Private Sub Label1_Click(sender As Object, e As EventArgs) Handles Label1.Click

	End Sub
End Class

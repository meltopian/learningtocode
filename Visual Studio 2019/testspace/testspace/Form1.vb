Public Class Form1
    Private Sub Button1_Click(sender As Object, e As EventArgs) Handles Button1.Click
        Const csv_line_test As String = "Jane,09/09/1989,Female,Blue"
        Dim line_split() = csv_line_test.Split(",")
    End Sub
End Class

# File Dialog

## Description

This sample demonstrates the use of the FileDialog object. The only requirement to run this sample is to have Inventor open.

## Code Samples

* [VBA](#VBA)
* [C#](#C#)

```
Public Sub TestFileDialog()
    ' Create a new FileDialog object.
    Dim oFileDlg As FileDialog
    Call ThisApplication.CreateFileDialog(oFileDlg)

    ' Define the filter to select part and assembly files or any file.
    oFileDlg.Filter = "Inventor Files (*.iam;*.ipt)|*.iam;*.ipt|All Files (*.*)|*.*"

    ' Define the part and assembly files filter to be the default filter.
    oFileDlg.FilterIndex = 1

    ' Set the title for the dialog.
    oFileDlg.DialogTitle = "Open File Test"

    ' Set the initial directory that will be displayed in the dialog.
    oFileDlg.InitialDirectory = "C:\Temp"

    ' Set the flag so an error will be raised if the user clicks the Cancel button.
    oFileDlg.CancelError = True

    ' Show the open dialog.  The same procedure is also used for the Save dialog.
    ' The commented code can be used for the Save dialog.
    On Error Resume Next
    oFileDlg.ShowOpen
'    oFileDlg.ShowSave

    ' If an error was raised, the user clicked cancel, otherwise display the filename.
    If Err Then
        MsgBox "User cancelled out of dialog"
    ElseIf oFileDlg.FileName <> "" Then
        MsgBox "File " & oFileDlg.FileName & " was selected."
    End If
End Sub
```

The first line sets the oApp variable to ThisApplication - this should be appropriately changed.

```
public void TestFileDialog()
{
    Application oApp = ThisApplication;

    // Create a new FileDialog object.
    FileDialog oFileDlg;
    oApp.CreateFileDialog(out(oFileDlg));

    // Define the filter to select part and assembly files or any file.
    oFileDlg.Filter = "Inventor Files (*.iam;*.ipt)|*.iam;*.ipt|All Files (*.*)|*.*";

    // Define the part and assembly files filter to be the default filter.
    oFileDlg.FilterIndex = 1;

    // Set the title for the dialog.
    oFileDlg.DialogTitle = "Open File Test";

    // Set the initial directory that will be displayed in the dialog.
    oFileDlg.InitialDirectory = "C:/Temp";

    // Set the flag so an error will not be raised if the user clicks the Cancel button.
    oFileDlg.CancelError = false;

    // Show the open dialog.  The same procedure is also used for the Save dialog.
    // The commented code can be used for the Save dialog.
    oFileDlg.ShowOpen();
    // oFileDlg.ShowSave();

    System.Windows.Forms.MessageBox.Show("File " + oFileDlg.FileName + " was selected.", "Selected file");
}
```

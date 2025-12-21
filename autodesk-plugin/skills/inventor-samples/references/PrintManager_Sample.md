# Printing - Part or Assembly

## Description

This sample demonstrates how to print a Part or Assembly document.

## Code Samples

* [VBA](#VBA)

|  |
| --- |
| Copy Code |

```
Public Sub PrintPartOrAssembly()
    ' Set a reference to the print manager object of the active document.
    Dim oPrintMgr As PrintManager
    Set oPrintMgr = ThisApplication.ActiveDocument.PrintManager

    ' Get the name of the printer that will be used.
    If MsgBox("Using printer """ & oPrintMgr.Printer & """  Do you want to continue?", vbYesNo + vbQuestion) = vbNo Then
        ' Change to another printer.
        Dim sPrinterName As String
        sPrinterName = InputBox("Enter name of new printer:", "New Printer")
        If sPrinterName = "" Then
            Exit Sub
        Else
            oPrintMgr.Printer = sPrinterName
        End If
    End If

    ' Set to print in color.
    oPrintMgr.ColorMode = kPrintColorPalette

    ' Set to print two copies.
    oPrintMgr.NumberOfCopies = 2

    ' Set to print using portrait orientation.
    oPrintMgr.Orientation = kPortraitOrientation

    ' Set the paper size.
    oPrintMgr.PaperSize = kPaperSize11x17

    ' Submit the print.
    oPrintMgr.SubmitPrint

    ' Change the number of copies to 1.
    oPrintMgr.NumberOfCopies = 1

    ' Change the paper size to a custom size.  The units are in centimeters.
    oPrintMgr.PaperSize = kPaperSizeCustom
    oPrintMgr.PaperHeight = 15
    oPrintMgr.PaperWidth = 10

    ' Submit the print.
    oPrintMgr.SubmitPrint
End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
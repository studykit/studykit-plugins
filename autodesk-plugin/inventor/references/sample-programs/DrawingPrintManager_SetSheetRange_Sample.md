# Printing - Drawing Print

## Description

This sample demonstrates how to print a drawing, setting specifics such as sheet range.

## Code Samples

* [VBA](#VBA)

|  |
| --- |
| Copy Code |

```
Public Sub PrintDrawing()
    ' Set a reference to the print manager object of the active document.
    ' This will fail if a drawing document is not active.
    Dim oPrintMgr As DrawingPrintManager
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

    ' Set to print all sheets.
    oPrintMgr.PrintRange = kPrintAllSheets

    ' Set to print full scale.
    oPrintMgr.ScaleMode = kPrintFullScale

    ' Submit the print.
    oPrintMgr.SubmitPrint

    ' Change the number of copies to 1.
    oPrintMgr.NumberOfCopies = 1

    ' Change the paper size to a custom size.  The units are in centimeters.
    oPrintMgr.PaperSize = kPaperSizeCustom
    oPrintMgr.PaperHeight = 15
    oPrintMgr.PaperWidth = 10

    ' Get and set the current sheet range.
    Dim iFromSheet As Long
    Dim iToSheet As Long
    Call oPrintMgr.GetSheetRange(iFromSheet, iToSheet)

    MsgBox "Current sheet range is " & iFromSheet & " to " & iToSheet & Chr(13) & _
            "Setting to print sheets 1-2."

    ' Change the print range to print sheets 1 through 2.
    oPrintMgr.PrintRange = kPrintSheetRange
    Call oPrintMgr.SetSheetRange(1, 2)

    ' Submit the print.
    oPrintMgr.SubmitPrint
End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
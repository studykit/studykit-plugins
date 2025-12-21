# Printing - All Sheets in Drawing

## Description

This sample demonstrates how to print all sheets in a drawing document and set some of the DrawingPrintManager properties.

## Code Samples

* [VBA](#VBA)

|  |
| --- |
| Copy Code |

```
Public Sub PlotAllSheetsInDrawing()
    'Print all sheets in drawing document
    'Get the active document and check whether it's drawing document
    If ThisApplication.ActiveDocument.DocumentType = kDrawingDocumentObject Then

        Dim oDrgDoc As DrawingDocument
        Set oDrgDoc = ThisApplication.ActiveDocument

        ' Set reference to drawing print manager
        ' DrawingPrintManager has more options than PrintManager
        ' as it's specific to drawing document
        Dim oDrgPrintMgr As DrawingPrintManager
        Set oDrgPrintMgr = oDrgDoc.PrintManager
        ' Set the printer name
        ' comment this line to use default printer or assign another one
        oDrgPrintMgr.Printer = "HP LaserJet 4000 Series PCL 6"

        'Set the paper size , scale and orientation
        oDrgPrintMgr.ScaleMode = kPrintBestFitScale
        oDrgPrintMgr.PaperSize = kPaperSizeA4
        oDrgPrintMgr.PrintRange = kPrintAllSheets
        oDrgPrintMgr.Orientation = kLandscapeOrientation
        oDrgPrintMgr.SubmitPrint
    End If
End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
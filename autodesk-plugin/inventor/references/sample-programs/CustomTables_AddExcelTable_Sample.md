# Create a drawing Excel Table

## Description

This sample demonstrates the creation of a table based on an Excel file in a drawing.

## Code Samples

* [VBA](#VBA)

Change the location of the source Excel file in the code below before running the sample.

|  |
| --- |
| Copy Code |

```
Public Sub CreateDrawingExcelTable()
    ' Set a reference to the active drawing document
    Dim oDrawDoc As DrawingDocument
    Set oDrawDoc = ThisApplication.ActiveDocument

    ' Set a reference to the active sheet
    Dim oActiveSheet As Sheet
    Set oActiveSheet = oDrawDoc.ActiveSheet

    ' Create the placement point for the table
    Dim oPoint As Point2d
    Set oPoint = ThisApplication.TransientGeometry.CreatePoint2d(25, 25)

    ' Create the table by specifying the source Excel file
    ' This assumes that the first row in the Excel sheet specifies the column headers
    ' You can specify a different row using the last argument of the AddExcelTable method
    Dim oExcelTable As CustomTable
    Set oExcelTable = oActiveSheet.CustomTables.AddExcelTable("C:\Temp\test.xls", oPoint, "Excel Table")
End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
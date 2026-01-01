# Create a Bend Table

## Description

This sample demonstrates the creation of a bend table in a drawing from a sheet metal part.

## Code Samples

* [VBA](#VBA)

Change the location of the source part in the code below before running the sample.

```
Public Sub CreateBendTable()
    ' Set a reference to the active drawing document
    Dim oDrawDoc As DrawingDocument
    Set oDrawDoc = ThisApplication.ActiveDocument

    ' Set a reference to the active sheet
    Dim oActiveSheet As Sheet
    Set oActiveSheet = oDrawDoc.ActiveSheet

    ' Create the placement point for the table
    Dim oPoint As Point2d
    Set oPoint = ThisApplication.TransientGeometry.CreatePoint2d(25, 25)

    ' Specify the columns - this can be specified in any combination/order
    Dim strColumns(1 To 5) As String
    strColumns(1) = "BEND ID"
    strColumns(2) = "BEND RADIUS"
    strColumns(3) = "BEND ANGLE"
    strColumns(4) = "BEND KFACTOR"
    strColumns(5) = "BEND DIRECTION"

    ' Create the bend table by specifying the source sheet metal file
    Dim oBendTable As CustomTable
    Set oBendTable = oActiveSheet.CustomTables.AddBendTable("C:\Temp\SheetMetal.ipt", oPoint, "Bend Table", strColumns)
End Sub
```

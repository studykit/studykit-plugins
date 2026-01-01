# Custom Table - create

## Description

This sample demonstrates how to create a custom table.

## Code Samples

* [VBA](#VBA)

```
Public Sub CreateCustomTable()
    ' Set a reference to the drawing document.
    ' This assumes a drawing document is active.
    Dim oDrawDoc As DrawingDocument
    Set oDrawDoc = ThisApplication.ActiveDocument

    ' Set a reference to the active sheet.
    Dim oSheet As Sheet
    Set oSheet = oDrawDoc.ActiveSheet

    ' Set the column titles
    Dim oTitles(1 To 3) As String
    oTitles(1) = "Part Number"
    oTitles(2) = "Quantity"
    oTitles(3) = "Material"

    ' Set the contents of the custom table (contents are set row-wise)
    Dim oContents(1 To 9) As String
    oContents(1) = "1"
    oContents(2) = "1"
    oContents(3) = "Brass"
    oContents(4) = "2"
    oContents(5) = "2"
    oContents(6) = "Aluminium"
    oContents(7) = "3"
    oContents(8) = "1"
    oContents(9) = "Steel"

    ' Set the column widths (defaults to the column title width if not specified)
    Dim oColumnWidths(1 To 3) As Double
    oColumnWidths(1) = 2.5
    oColumnWidths(2) = 2.5
    oColumnWidths(3) = 4

    ' Create the custom table
    Dim oCustomTable As CustomTable
    Set oCustomTable = oSheet.CustomTables.Add("My Table", ThisApplication.TransientGeometry.CreatePoint2d(15, 15), _
                                        3, 3, oTitles, oContents, oColumnWidths)

    ' Change the 3rd column to be left justified.
    oCustomTable.Columns.Item(3).ValueHorizontalJustification = kAlignTextLeft

    ' Create a table format object
    Dim oFormat As TableFormat
    Set oFormat = oSheet.CustomTables.CreateTableFormat

    ' Set inside line color to red.
    oFormat.InsideLineColor = ThisApplication.TransientObjects.CreateColor(255, 0, 0)

    ' Set outside line weight.
    oFormat.OutsideLineWeight = 0.1

    ' Modify the table formats
    oCustomTable.OverrideFormat = oFormat
End Sub
```

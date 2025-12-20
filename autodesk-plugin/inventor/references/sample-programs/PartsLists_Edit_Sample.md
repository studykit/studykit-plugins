# Parts List Edit

## Description

This sample illustrates editing the contents of the parts list.

## Code Samples

* [VBA](#VBA)

To run this sample have a sheet active that contains a parts list.

|  |
| --- |
| Copy Code |

```
Public Sub PartListEdit()
    ' Set a reference to the drawing document.
    ' This assumes a drawing document is active.
    Dim oDrawDoc As DrawingDocument
    Set oDrawDoc = ThisApplication.ActiveDocument

    ' Set a reference to the first parts list on the active sheet.
    ' This assumes that a parts list is on the active sheet.
    Dim oPartList As PartsList
    Set oPartList = oDrawDoc.ActiveSheet.PartsLists.Item(1)

    ' Iterate through the contents of the parts list.
    Dim i As Long
    For i = 1 To oPartList.PartsListRows.Count
        ' Get the current row.
        Dim oRow As PartsListRow
        Set oRow = oPartList.PartsListRows.Item(i)

        ' Iterate through each column in the row.
        Dim j As Long
        For j = 1 To oPartList.PartsListColumns.Count
            ' Get the current cell.
            Dim oCell As PartsListCell
            Set oCell = oRow.Item(j)

            ' Check that the column isn't the quantity column.
            If oPartList.PartsListColumns.Item(j).Title  "QTY" Then
                ' Change the current value in the part list.
                oCell.Value = i & "," & j
            End If
        Next
    Next

    ' This changes a specific column by name.
    Dim ItemNumber As Long
    ItemNumber = oPartList.PartsListRows.Count
    For i = 1 To oPartList.PartsListRows.Count
        Set oCell = oPartList.PartsListRows.Item(i).Item("ITEM")
        oCell.Value = ItemNumber
        ItemNumber = ItemNumber - 1
    Next
End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
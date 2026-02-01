# Parts List Query

## Description

This sample illustrates querying the contents of the parts list.

## Code Samples

* [VBA](#VBA)

To run this sample have a sheet active that contains a parts list.

```
Public Sub PartListQuery()
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

            ' Display the value of the current cell.
            Debug.Print "Row: " & i & ", Column: " & oPartList.PartsListColumns.Item(j).Title & " = "; oCell.Value
        Next
    Next
End Sub
```

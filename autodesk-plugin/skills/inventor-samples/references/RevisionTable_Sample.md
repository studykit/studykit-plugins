# Query revision table

## Description

This sample illustrates querying the contents of the revision table.

## Code Samples

* [VBA](#VBA)

To run this sample have a sheet active that contains a revision table.

```
Public Sub RevisionTableQuery()
    ' Set a reference to the drawing document.
    ' This assumes a drawing document is active.
    Dim oDrawDoc As DrawingDocument
    Set oDrawDoc = ThisApplication.ActiveDocument

    ' Set a reference to the first revision table on the active sheet.
    ' This assumes that a revision table is on the active sheet.
    Dim oRevTable As RevisionTable
    Set oRevTable = oDrawDoc.ActiveSheet.RevisionTables.Item(1)

    ' Iterate through the contents of the revision table.
    Dim i As Long
    For i = 1 To oRevTable.RevisionTableRows.Count
        ' Get the current row.
        Dim oRow As RevisionTableRow
        Set oRow = oRevTable.RevisionTableRows.Item(i)

        ' Iterate through each column in the row.
        Dim j As Long
        For j = 1 To oRevTable.RevisionTableColumns.Count
            ' Get the current cell.
            Dim oCell As RevisionTableCell
            Set oCell = oRow.Item(j)

            ' Display the value of the current cell.
            Debug.Print "Row: " & i & ", Column: " & oRevTable.RevisionTableColumns.Item(j).Title & " = "; oCell.Text
        Next
    Next
End Sub
```

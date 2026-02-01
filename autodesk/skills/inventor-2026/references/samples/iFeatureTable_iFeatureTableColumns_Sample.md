# Changing row of table driven iFeature

## Description

This program demonstrates the edit of a table driven iFeature to change which row of the table is being used to drive the iFeature.

## Code Samples

* [VBA](#VBA)

```
Public Sub EditTableDriveniFeature()
    ' Get the part document and component definition of the active document.
    Dim oPartDoc As PartDocument
    Set oPartDoc = ThisApplication.ActiveDocument
    If Err Then
        MsgBox "A part must be active."
        Exit Sub
    End If

    Dim oFeatures As PartFeatures
    Set oFeatures = oPartDoc.ComponentDefinition.Features

    ' Get the first iFeature assuming that it is table-driven.
    Dim oiFeature As iFeature
    Set oiFeature = oFeatures.iFeatures.Item(1)

    ' Check to see if the first iFeature is table-driven.
    If Not oiFeature.iFeatureDefinition.IsTableDriven Then
        MsgBox "The first iFeature in the part is not table-driven."
        Exit Sub
    End If

    '** Look through the table to find the row where "Size" is "3".
    Dim oTable As iFeatureTable
    Set oTable = oiFeature.iFeatureDefinition.iFeatureTable

    ' Find the "Size" column.
    Dim oColumn As iFeatureTableColumn
    Dim bFoundSize As Boolean
    bFoundSize = False
    For Each oColumn In oTable.iFeatureTableColumns
        If oColumn.DisplayHeading = "Size" Then
            bFoundSize = True
            Exit For
        End If
    Next

    If Not bFoundSize Then
        MsgBox "The column ""Size"" was not found."
        Exit Sub
    End If

    ' Find the row in the "Size" column with the value of "3"
    Dim oCell As iFeatureTableCell
    bFoundSize = False
    For Each oCell In oColumn
        If oCell.Value = "3" Then
            bFoundSize = True
            Exit For
        End If
    Next

    If Not bFoundSize Then
        MsgBox "The cell with value ""3"" was not found."
        Exit Sub
    End If

    oiFeature.iFeatureDefinition.ActiveTableRow = oCell.Row
End Sub
```

# Creating Stacked Text

## Description

This sample demonstrates the creation of stacked text and text with superscript & subscript.

## Code Samples

* [VBA](#VBA)

|  |
| --- |
| Copy Code |

```
Public Sub StackedText()
    ' Set a reference to the active drawing document
    Dim oDrawDoc As DrawingDocument
    Set oDrawDoc = ThisApplication.ActiveDocument

    ' Set a reference to the active sheet
    Dim oActiveSheet As Sheet
    Set oActiveSheet = oDrawDoc.ActiveSheet

    ' Create the placement point for the text
    Dim oPoint As Point2d
    Set oPoint = ThisApplication.TransientGeometry.CreatePoint2d(25, 25)

    ' Define horizontally stacked text
    Dim strHorizontalStack As String
    strHorizontalStack = "11/2"

    ' Define diagonally stacked text
    Dim strDiagonalStack As String
    strDiagonalStack = "11#2"

    ' Define text with subscript
    Dim strSubscript As String
    strSubscript = "H^2SO^4"

    ' Define text with superscript
    Dim strSuperscript As String
    strSuperscript = "x2^ + y2^ = z2^"

    Dim strText As String
    strText = strHorizontalStack & "" & strDiagonalStack & "" & strSubscript & "" & strSuperscript

    Dim oGeneralNote As GeneralNote
    Set oGeneralNote = oActiveSheet.DrawingNotes.GeneralNotes.AddFitted(oPoint, strText)
End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
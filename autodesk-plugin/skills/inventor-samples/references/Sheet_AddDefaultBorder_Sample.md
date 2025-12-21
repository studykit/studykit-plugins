# Border Insert

## Description

This sample illustrates inserting a default border.

## Code Samples

* [VBA](#VBA)

```
Public Sub InsertDefaultBorder()
    ' Set a reference to the drawing document.
    ' This assumes a drawing document is active.
    Dim oDrawDoc As DrawingDocument
    Set oDrawDoc = ThisApplication.ActiveDocument

    Dim oSheet As Sheet
    Set oSheet = oDrawDoc.ActiveSheet

    ' Check to see if the sheet already has a border and delete it if it does.
    If Not oSheet.Border Is Nothing Then
        oSheet.Border.Delete
    End If

    ' Define the values to use as input for the border creation.
    Dim HorizontalZoneCount As Long
    HorizontalZoneCount = 15

    Dim HorizontalZoneLabelMode As BorderLabelModeEnum
    HorizontalZoneLabelMode = kBorderLabelModeNumeric

    Dim VerticalZoneCount As Long
    VerticalZoneCount = 10

    Dim VerticalZoneLabelMode As BorderLabelModeEnum
    VerticalZoneLabelMode = kBorderLabelModeAlphabetical

    Dim LabelFromBottomRight As Boolean
    LabelFromBottomRight = False

    Dim DelimitByLines As Boolean
    DelimitByLines = False

    Dim CenterMarks As Boolean
    CenterMarks = False

    Dim TopMargin As Double
    TopMargin = 5

    Dim BottomMargin As Double
    BottomMargin = 3

    Dim LeftMargin As Double
    LeftMargin = 1

    Dim RightMargin As Double
    RightMargin = 2

    Dim BorderLineWidth As Double
    BorderLineWidth = 0.1

    Dim TextLabelHeight As Double
    TextLabelHeight = 1.5

    Dim Font As String
    Font = "Courier New"

    ' Add the border to the sheet.  This sets all of the values, but any of them
    ' can be left out and it will default to an appropriate value.
    Dim oBorder As DefaultBorder
    Set oBorder = oSheet.AddDefaultBorder(HorizontalZoneCount, HorizontalZoneLabelMode, _
                                          VerticalZoneCount, VerticalZoneLabelMode, _
                                          LabelFromBottomRight, DelimitByLines, _
                                          CenterMarks, TopMargin, BottomMargin, _
                                          LeftMargin, RightMargin, BorderLineWidth, _
                                          TextLabelHeight, Font)
End Sub
```

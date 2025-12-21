# Add a general note

## Description

This sample illustrates creating text (general note) in a sheet.

## Code Samples

* [VBA](#VBA)

Before running this sample, open a drawing document.

```
Public Sub SheetTextAdd()
    ' Set a reference to the drawing document.
    ' This assumes a drawing document is active.
    Dim oDrawDoc As DrawingDocument
    Set oDrawDoc = ThisApplication.ActiveDocument

    ' Set a reference to the active sheet.
    Dim oActiveSheet As Sheet
    Set oActiveSheet = oDrawDoc.ActiveSheet

    ' Set a reference to the GeneralNotes object
    Dim oGeneralNotes As GeneralNotes
    Set oGeneralNotes = oActiveSheet.DrawingNotes.GeneralNotes

    Dim oTG As TransientGeometry
    Set oTG = ThisApplication.TransientGeometry

    ' Create text with simple string as input. Since this doesn't use
    ' any text overrides, it will default to the active text style.
    Dim sText As String
    sText = "Drawing Notes"

    Dim oGeneralNote As GeneralNote
    Set oGeneralNote = oGeneralNotes.AddFitted(oTG.CreatePoint2d(3, 18), sText)

    ' Create text using various overrides.
    sText = "Notice: All holes larger than 0.500 n are to be lubricated."
    Set oGeneralNote = oGeneralNotes.AddFitted(oTG.CreatePoint2d(3, 16), sText)

    ' Create a set of notes that are numbered and aligned along the left.
    Dim dYCoord As Double
    dYCoord = 14
    Dim dYOffset As Double
    Dim oStyle As TextStyle
    Set oStyle = oGeneralNotes.Item(1).TextStyle
    dYOffset = oStyle.FontSize * 1.5

    ' Simple single line text.
    Set oGeneralNote = oGeneralNotes.AddFitted(oTG.CreatePoint2d(3, dYCoord), "1.")
    sText = "This is note 1."
    Set oGeneralNote = oGeneralNotes.AddFitted(oTG.CreatePoint2d(4, dYCoord), sText)

    ' Two line text. The two lines are defined using the  tag within the text string.
    dYCoord = dYCoord - (oGeneralNote.FittedTextHeight + 0.5)
    Set oGeneralNote = oGeneralNotes.AddFitted(oTG.CreatePoint2d(3, dYCoord), "2.")
    sText = "This is note 2,  which contains two lines."
    Set oGeneralNote = oGeneralNotes.AddFitted(oTG.CreatePoint2d(4, dYCoord), sText)

    ' Single line of text.
    dYCoord = dYCoord - (oGeneralNote.FittedTextHeight + 0.5)
    Set oGeneralNote = oGeneralNotes.AddFitted(oTG.CreatePoint2d(3, dYCoord), "3.")
    sText = "This is note 3."
    Set oGeneralNote = oGeneralNotes.AddFitted(oTG.CreatePoint2d(4, dYCoord), sText)

    ' Three lines of text.
    dYCoord = dYCoord - (oGeneralNote.FittedTextHeight + 0.5)
    Set oGeneralNote = oGeneralNotes.AddFitted(oTG.CreatePoint2d(3, dYCoord), "4.")
    sText = "This is note 4,  which contains  several lines."
    Set oGeneralNote = oGeneralNotes.AddFitted(oTG.CreatePoint2d(4, dYCoord), sText)

    dYCoord = dYCoord - (oGeneralNote.FittedTextHeight + 0.5)
    Set oGeneralNote = oGeneralNotes.AddFitted(oTG.CreatePoint2d(3, dYCoord), "5.")

    sText = "Here is the last and final line of text."
    Set oGeneralNote = oGeneralNotes.AddFitted(oTG.CreatePoint2d(4, dYCoord), sText)
End Sub
```

# Bullet and Numbering List

## Description

This sample demonstrates how to create bullets and numbering list in a drawing note.

## Code Samples

* [VBA](#VBA)

```
Sub DrawingNoteBulletAndNumberingListSample()
    Dim oDoc As DrawingDocument
    Set oDoc = ThisApplication.Documents.Add(kDrawingDocumentObject)

    Dim oPosition As Point2d
    Set oPosition = ThisApplication.TransientGeometry.CreatePoint2d(12, 12)

    Dim sFormattedText As String
    sFormattedText = "<Bullet>Line1</Bullet><Bullet>Line2</Bullet><Bullet>Line3</Bullet><Numbering Format='a'>Number1</Numbering><Numbering Format='a'>Number2</Numbering><Numbering Format='a'>Number<StyleOverride Strikethrough='True'>5</StyleOverride>3</Numbering>"

    Dim oNote As DrawingNote
    Set oNote = oDoc.Sheets(1).DrawingNotes.GeneralNotes.AddFitted(oPosition, sFormattedText)

    Debug.Print oNote.Text
    Debug.Print oNote.FormattedText
End Sub
```

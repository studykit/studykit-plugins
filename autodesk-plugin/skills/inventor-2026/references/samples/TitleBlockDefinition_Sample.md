# Title Block Definition Create and Insert

## Description

This sample illustrates creating a new title block definition object and inserting it into the active sheet. This sample consists of two subs. The first demonstrates the creation of a title block definition and the second inserts it into the active sheet.

## Code Samples

* [VBA](#VBA)

To run the sample have a drawing document open and run the CreateTitleBlockDefinition Sub. After this you can run the InsertTitleBlockOnSheet to insert the title block into the active sheet.

```
Public Sub CreateTitleBlockDefinition()
    ' Set a reference to the drawing document.
    ' This assumes a drawing document is active.
    Dim oDrawDoc As DrawingDocument
    Set oDrawDoc = ThisApplication.ActiveDocument

    ' Create the new title block defintion.
    Dim oTitleBlockDef As TitleBlockDefinition
    Set oTitleBlockDef = oDrawDoc.TitleBlockDefinitions.Add("Sample Title Block")

    ' Open the title block definition's sketch for edit.  This is done by calling the Edit
    ' method of the TitleBlockDefinition to obtain a DrawingSketch.  This actually creates
    ' a copy of the title block definition's and opens it for edit.
    Dim oSketch As DrawingSketch
    Call oTitleBlockDef.Edit(oSketch)

    Dim oTG As TransientGeometry
    Set oTG = ThisApplication.TransientGeometry

    ' Use the functionality of the sketch to add title block graphics.
    Call oSketch.SketchLines.AddAsTwoPointRectangle(oTG.CreatePoint2d(0, 0), oTG.CreatePoint2d(9, 3))
    Call oSketch.SketchLines.AddByTwoPoints(oTG.CreatePoint2d(0, 1.5), oTG.CreatePoint2d(9, 1.5))
    Call oSketch.SketchLines.AddByTwoPoints(oTG.CreatePoint2d(0, 2.25), oTG.CreatePoint2d(9, 2.25))
    Call oSketch.SketchLines.AddByTwoPoints(oTG.CreatePoint2d(4.5, 1.5), oTG.CreatePoint2d(4.5, 2.25))
    Call oSketch.SketchLines.AddByTwoPoints(oTG.CreatePoint2d(3, 2.25), oTG.CreatePoint2d(3, 3))
    Call oSketch.SketchLines.AddByTwoPoints(oTG.CreatePoint2d(6, 2.25), oTG.CreatePoint2d(6, 3))

    ' Add some static text to the title block.
    Dim sText As String
    sText = "TITLE BLOCK"
    Dim oTextBox As TextBox
    Set oTextBox = oSketch.TextBoxes.AddFitted(oTG.CreatePoint2d(4.5, 0.75), sText)
    oTextBox.VerticalJustification = kAlignTextMiddle
    oTextBox.HorizontalJustification = kAlignTextCenter

    sText = "Static Text"
    Set oTextBox = oSketch.TextBoxes.AddByRectangle(oTG.CreatePoint2d(0, 1.5), oTG.CreatePoint2d(4.5, 2.25), sText)
    oTextBox.VerticalJustification = kAlignTextMiddle
    oTextBox.HorizontalJustification = kAlignTextCenter

    ' Add some prompted text fields.
    sText = "<Prompt>Enter text 1</Prompt>"
    Set oTextBox = oSketch.TextBoxes.AddByRectangle(oTG.CreatePoint2d(4.5, 1.5), oTG.CreatePoint2d(9, 2.25), sText)
    oTextBox.VerticalJustification = kAlignTextMiddle
    oTextBox.HorizontalJustification = kAlignTextCenter

     sText = "<Prompt>Enter text 2</Prompt>"
    Set oTextBox = oSketch.TextBoxes.AddByRectangle(oTG.CreatePoint2d(0, 2.25), oTG.CreatePoint2d(3, 3), sText)
    oTextBox.VerticalJustification = kAlignTextMiddle
    oTextBox.HorizontalJustification = kAlignTextCenter

    ' Add some property text.
    ' Add the property value of Author from the drawing
    sText = "<Property Document='drawing' FormatID='{F29F85E0-4FF9-1068-AB91-08002B27B3D9}' PropertyID='4' />"
    Set oTextBox = oSketch.TextBoxes.AddByRectangle(oTG.CreatePoint2d(3, 2.25), oTG.CreatePoint2d(6, 3), sText)
    oTextBox.VerticalJustification = kAlignTextMiddle
    oTextBox.HorizontalJustification = kAlignTextCenter

    ' Add the property value of Subject from the drawing
    sText = "<Property Document='drawing' FormatID='{F29F85E0-4FF9-1068-AB91-08002B27B3D9}' PropertyID='3' />"
    Set oTextBox = oSketch.TextBoxes.AddByRectangle(oTG.CreatePoint2d(6, 2.25), oTG.CreatePoint2d(9, 3), sText)
    oTextBox.VerticalJustification = kAlignTextMiddle
    oTextBox.HorizontalJustification = kAlignTextCenter

    Call oTitleBlockDef.ExitEdit(True)
End Sub

Public Sub InsertTitleBlockOnSheet()
    ' Set a reference to the drawing document.
    ' This assumes a drawing document is active.
    Dim oDrawDoc As DrawingDocument
    Set oDrawDoc = ThisApplication.ActiveDocument

    ' Obtain a reference to the desired border defintion.
    Dim oTitleBlockDef As TitleBlockDefinition
    Set oTitleBlockDef = oDrawDoc.TitleBlockDefinitions.Item("Sample Title Block")

    Dim oSheet As Sheet
    Set oSheet = oDrawDoc.ActiveSheet

    ' Check to see if the sheet already has a title block and delete it if it does.
    If Not oSheet.TitleBlock Is Nothing Then
        oSheet.TitleBlock.Delete
    End If

    ' This title block definition contains one prompted string input.  An array
    ' must be input that contains the strings for the prompted strings.
    Dim sPromptStrings(1 To 2) As String
    sPromptStrings(1) = "String 1"
    sPromptStrings(2) = "String 2"

    ' Add an instance of the title block definition to the sheet.
    Dim oTitleBlock As TitleBlock
    Set oTitleBlock = oSheet.AddTitleBlock(oTitleBlockDef, , sPromptStrings)
End Sub
```

# Border Create and Insert

## Description

This sample illustrates creating a new border definition object and using it for a sheet.

## Code Samples

* [VBA](#VBA)

This sample consists of two sub procedures. The first creates the border definition. The second inserts it into the active sheet. To run the sample have a drawing document open and run the CreateBorderDefinition sub first. After that you can run the InsertBorderOnSheet sub.

```
Public Sub CreateBorderDefinition()
    ' Set a reference to the drawing document.
    ' This assumes a drawing document is active.
    Dim oDrawDoc As DrawingDocument
    Set oDrawDoc = ThisApplication.ActiveDocument

    ' Create the new borderdefinition.
    Dim oBorderDef As BorderDefinition
    Set oBorderDef = oDrawDoc.BorderDefinitions.Add("Sample Border")

    ' Open the border definition's sketch for edit.  This is done by calling the Edit
    ' method of the BorderDefinition to obtain a DrawingSketch.  This actually creates
    ' a copy of the border definition's and opens it for edit.
    Dim oSketch As DrawingSketch
    Call oBorderDef.Edit(oSketch)

    Dim oTG As TransientGeometry
    Set oTG = ThisApplication.TransientGeometry

    ' Use the functionality of the sketch to add geometry.
    Call oSketch.SketchLines.AddAsTwoPointRectangle(oTG.CreatePoint2d(2, 2), oTG.CreatePoint2d(25.94, 19.59))
    Call oSketch.SketchLines.AddByTwoPoints(oTG.CreatePoint2d(0, 10.795), oTG.CreatePoint2d(2, 10.795))
    Call oSketch.SketchLines.AddByTwoPoints(oTG.CreatePoint2d(13.97, 0), oTG.CreatePoint2d(13.97, 2))
    Call oSketch.SketchLines.AddByTwoPoints(oTG.CreatePoint2d(25.94, 10.795), oTG.CreatePoint2d(27.94, 10.795))
    Call oSketch.SketchLines.AddByTwoPoints(oTG.CreatePoint2d(13.97, 19.59), oTG.CreatePoint2d(13.97, 21.59))

    ' Add some text to the border.
    Dim oTextBox As TextBox
    Set oTextBox = oSketch.TextBoxes.AddFitted(oTG.CreatePoint2d(2, 1), "Here is a sample string")
    oTextBox.VerticalJustification = kAlignTextMiddle

    ' Add some prompted text to the border.
    Set oTextBox = oSketch.TextBoxes.AddFitted(oTG.CreatePoint2d(2, 20.59), "Enter designers name:")
    oTextBox.VerticalJustification = kAlignTextMiddle

    Call oBorderDef.ExitEdit(True)
End Sub

Public Sub InsertCustomBorderOnSheet()
    ' Set a reference to the drawing document.
    ' This assumes a drawing document is active.
    Dim oDrawDoc As DrawingDocument
    Set oDrawDoc = ThisApplication.ActiveDocument

    ' Obtain a reference to the desired border definition.
    Dim oBorderDef As BorderDefinition
    Set oBorderDef = oDrawDoc.BorderDefinitions.Item("Sample Border")

    Dim oSheet As Sheet
    Set oSheet = oDrawDoc.ActiveSheet

    ' Check to see if the sheet already has a border and delete it if it does.
    If Not oSheet.Border Is Nothing Then
        oSheet.Border.Delete
    End If

    ' This border definition contains one prompted string input.  An array
    ' must be input that contains the strings for the prompted strings.
    Dim sPromptStrings(1 To 1) As String
    sPromptStrings(1) = "This is the input for the prompted text."

    ' Add an instance of the border definition to the sheet.
    Dim oBorder As Border
    Set oBorder = oSheet.AddBorder(oBorderDef, sPromptStrings)
End Sub
```

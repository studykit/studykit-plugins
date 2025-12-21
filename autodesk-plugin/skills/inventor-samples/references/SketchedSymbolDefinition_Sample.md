# Create SketchedSymbol Definition

## Description

This sample illustrates creating a new sketched symbol definition object and inserting it into the active sheet.

## Code Samples

* [VBA](#VBA)

This sample consists of two subs. The first demonstrates the creation of a sketched symbol definition and the second inserts it into the active sheet. To run the sample have a drawing document open and run the CreateSketchedSymbolDefinition Sub. After this you can run the InsertSketchedSymbolOnSheet to insert the sketched symbol into the active sheet. The insertion sub demonstrates the use of the insertion point in the symbol's definition while inserting the symbol.

|  |
| --- |
| Copy Code |

```
Public Sub CreateSketchedSymbolDefinition()
    ' Set a reference to the drawing document.
    ' This assumes a drawing document is active.
    Dim oDrawDoc As DrawingDocument
    Set oDrawDoc = ThisApplication.ActiveDocument

    ' Create the new sketched symbol definition.
    Dim oSketchedSymbolDef As SketchedSymbolDefinition
    Set oSketchedSymbolDef = oDrawDoc.SketchedSymbolDefinitions.Add("Circular Callout")

    ' Open the sketched symbol definition's sketch for edit. This is done by calling the Edit
    ' method of the SketchedSymbolDefinition to obtain a DrawingSketch. This actually creates
    ' a copy of the sketched symbol definition's and opens it for edit.
    Dim oSketch As DrawingSketch
    Call oSketchedSymbolDef.Edit(oSketch)

    Dim oTG As TransientGeometry
    Set oTG = ThisApplication.TransientGeometry

    ' Use the functionality of the sketch to add sketched symbol graphics.
    Dim oSketchLine As SketchLine
    Set oSketchLine = oSketch.SketchLines.AddByTwoPoints(oTG.CreatePoint2d(0, 0), oTG.CreatePoint2d(20, 0))

    Dim oSketchCircle As SketchCircle
    Set oSketchCircle = oSketch.SketchCircles.AddByCenterRadius(oTG.CreatePoint2d(22, 0), 2)

    Call oSketch.GeometricConstraints.AddCoincident(oSketchLine.EndSketchPoint, oSketchCircle)

    ' Make the starting point of the sketch line the insertion point
    oSketchLine.StartSketchPoint.InsertionPoint = True

    ' Add a prompted text field at the center of the sketch circle.
    Dim sText As String
    sText = "<Prompt>Enter text 1</Prompt>"
    Dim oTextBox As TextBox
    Set oTextBox = oSketch.TextBoxes.AddFitted(oTG.CreatePoint2d(22, 0), sText)
    oTextBox.VerticalJustification = kAlignTextMiddle
    oTextBox.HorizontalJustification = kAlignTextCenter

    Call oSketchedSymbolDef.ExitEdit(True)
End Sub

Public Sub InsertSketchedSymbolOnSheet()
    ' Set a reference to the drawing document.
    ' This assumes a drawing document is active.
    Dim oDrawDoc As DrawingDocument
    Set oDrawDoc = ThisApplication.ActiveDocument

    ' Obtain a reference to the desired sketched symbol definition.
    Dim oSketchedSymbolDef As SketchedSymbolDefinition
    Set oSketchedSymbolDef = oDrawDoc.SketchedSymbolDefinitions.Item("Circular Callout")

    Dim oSheet As Sheet
    Set oSheet = oDrawDoc.ActiveSheet

    ' This sketched symbol definition contains one prompted string input. An array
    ' must be input that contains the strings for the prompted strings.
    Dim sPromptStrings(0) As String
    sPromptStrings(0) = "A"

    Dim oTG As TransientGeometry
    Set oTG = ThisApplication.TransientGeometry

    ' Add an instance of the sketched symbol definition to the sheet.
    ' Rotate the instance by 45 degrees and scale by .75 when adding.
    ' The symbol will be inserted at (0,0) on the sheet. Since the
    ' start point of the line was marked as the insertion point, the
    ' start point should end up at (0,0).
    Dim oSketchedSymbol As SketchedSymbol
    Set oSketchedSymbol = oSheet.SketchedSymbols.Add(oSketchedSymbolDef, oTG.CreatePoint2d(0, 0), (3.14159 / 4), 0.75, sPromptStrings)
End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
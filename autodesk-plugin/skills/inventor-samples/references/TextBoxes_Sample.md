# Sketch Text Add

## Description

This sample illustrates creating text in a sketch.

## Code Samples

* [VBA](#VBA)

Before running this sample, open a drawing document.

```
Public Sub SketchTextAdd()
    ' Set a reference to the drawing document.
    ' This assumes a drawing document is active.
    Dim oDrawDoc As DrawingDocument
    Set oDrawDoc = ThisApplication.ActiveDocument

    ' Create a new sketch on the active sheet.
    Dim oSketch As DrawingSketch
    Set oSketch = oDrawDoc.ActiveSheet.Sketches.Add

    ' Open the sketch for edit so the text boxes can be created.
    ' This is only required for drawing sketches, not part.
    oSketch.Edit

    Dim oTG As TransientGeometry
    Set oTG = ThisApplication.TransientGeometry

    ' Create text with simple string as input.  Since this doesn't use
    ' any text overrides, it will default to the active text style.
    Dim sText As String
    sText = "Drawing Notes"
    Dim oTextBox As TextBox
    Set oTextBox = oSketch.TextBoxes.AddFitted(oTG.CreatePoint2d(3, 18), sText)

    ' Create text using various overrides.
    sText = "Notice: All holes larger than 0.500 n are to be lubricated."
    Set oTextBox = oSketch.TextBoxes.AddFitted(oTG.CreatePoint2d(3, 16), sText)

    ' Create a set of notes that are numbered and aligned along the left.
    Dim dYCoord As Double
    dYCoord = 14
    Dim dYOffset As Double
    Dim oStyle As TextStyle
    Set oStyle = oSketch.TextBoxes.Item(1).Style
    dYOffset = oStyle.FontSize * 1.5

    ' Simple single line text.
    Set oTextBox = oSketch.TextBoxes.AddFitted(oTG.CreatePoint2d(3, dYCoord), "1.")
    sText = "This is note 1."
    Set oTextBox = oSketch.TextBoxes.AddFitted(oTG.CreatePoint2d(4, dYCoord), sText)

    ' Two line text.  The two lines are defined using the  tag within the text string.
    dYCoord = dYCoord - (oTextBox.FittedTextHeight + 0.5)
    Set oTextBox = oSketch.TextBoxes.AddFitted(oTG.CreatePoint2d(3, dYCoord), "2.")
    sText = "This is note 2,  which contains two lines."
    Set oTextBox = oSketch.TextBoxes.AddFitted(oTG.CreatePoint2d(4, dYCoord), sText)

    ' Single line of text.
    dYCoord = dYCoord - (oTextBox.FittedTextHeight + 0.5)
    Set oTextBox = oSketch.TextBoxes.AddFitted(oTG.CreatePoint2d(3, dYCoord), "3.")
    sText = "This is note 3."
    Set oTextBox = oSketch.TextBoxes.AddFitted(oTG.CreatePoint2d(4, dYCoord), sText)

    ' Three lines of text.
    dYCoord = dYCoord - (oTextBox.FittedTextHeight + 0.5)
    Set oTextBox = oSketch.TextBoxes.AddFitted(oTG.CreatePoint2d(3, dYCoord), "4.")
    sText = "This is note 4,  which contains  several lines."
    Set oTextBox = oSketch.TextBoxes.AddFitted(oTG.CreatePoint2d(4, dYCoord), sText)

    ' The number of this line of text will have a triangle around it.
    dYCoord = dYCoord - (oTextBox.FittedTextHeight + 0.5)
    Set oTextBox = oSketch.TextBoxes.AddFitted(oTG.CreatePoint2d(3, dYCoord), "5")

    ' Draw a triangle that fits around a text box.
    Dim Points(1 To 3) As Point2d
    Call CalculateTriangle(oTextBox, Points)

    Dim oLines(1 To 3) As SketchLine
    Set oLines(1) = oSketch.SketchLines.AddByTwoPoints(Points(1), Points(2))
    Set oLines(2) = oSketch.SketchLines.AddByTwoPoints(oLines(1).EndSketchPoint, Points(3))
    Set oLines(3) = oSketch.SketchLines.AddByTwoPoints(oLines(2).EndSketchPoint, oLines(1).StartSketchPoint)

    sText = "Here is the last and final line of text."
    Set oTextBox = oSketch.TextBoxes.AddFitted(oTG.CreatePoint2d(4, dYCoord), sText)

    ' Exit the sketch from the edit environment.
    oSketch.ExitEdit
End Sub

' Function to calcuate the three points of a triangle that fits tightly around the input text box.
Private Sub CalculateTriangle(TextBox As TextBox, Points() As Point2d)
    ' Get the top-left corner of the text box.
    Dim dLeft As Double
    Dim dTop As Double
    Call GetCorner(TextBox, dLeft, dTop)

    Dim oTG As TransientGeometry
    Set oTG = ThisApplication.TransientGeometry

    ' Determine the top point of the triangle.
    Set Points(1) = oTG.CreatePoint2d(dLeft + (TextBox.Width / 2), dTop + ((TextBox.Width / 2) * Tan(1.0471975511966)))

    ' Determine the bottom-left corner point of the triangle.
    Dim dY As Double
    dY = (Points(1).Y - dTop) + (1.125 * TextBox.height)
    Set Points(2) = oTG.CreatePoint2d(Points(1).X - (dY / Tan(1.0471975511966)), Points(1).Y - dY)

    ' Determine the bottom right corner point of the triangle
    Set Points(3) = oTG.CreatePoint2d(Points(1).X + (dY / Tan(1.0471975511966)), Points(2).Y)
End Sub

' Function to determine the top left corner of the input text box.
Private Sub GetCorner(TextBox As TextBox, Left As Double, Top As Double)
    ' Determine the top left corner of the text box by accounting
    ' for the justifications.
    Select Case TextBox.HorizontalJustification
        Case kAlignTextLeft
            Left = TextBox.Origin.X
        Case kAlignTextCenter
            Left = TextBox.Origin.X - (TextBox.Width / 2)
        Case kAlignTextRight
            Left = TextBox.Origin.X - TextBox.Width
    End Select

    Select Case TextBox.VerticalJustification
        Case kAlignTextUpper
            Top = TextBox.Origin.Y
        Case kAlignTextMiddle
            Top = TextBox.Origin.Y + (TextBox.height / 2)
        Case kAlignTextLower
            Top = TextBox.Origin.Y + TextBox.height
    End Select
End Sub
```

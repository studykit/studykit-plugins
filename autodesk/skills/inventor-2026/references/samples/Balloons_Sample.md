# Balloons - edit

## Description

This sample demonstrates the editing of balloons in a drawing.

## Code Samples

* [VBA](#VBA)

To run this sample, open a drawing document with the active sheet that has several balloons (including attached balloons) placed on it. This sample modifies the type and values of all the balloons.

```
Public Sub EditBalloons()
    ' Set a reference to the drawing document.
    ' This assumes a drawing document is active.
    Dim oDrawDoc As DrawingDocument
    Set oDrawDoc = ThisApplication.ActiveDocument

    'Set a reference to the active sheet.
    Dim oSheet As Sheet
    Set oSheet = oDrawDoc.ActiveSheet

    Dim BalloonCount As Long
    BalloonCount = 1

    Dim oBalloon As Balloon

    ' Iterate over each balloon on the sheet.
    For Each oBalloon In oSheet.Balloons

        ' Change the balloon type
        oBalloon.SetBalloonType (kHexagonBalloonType)

        ' Change balloon placement direction so all the attached
        ' balloons are placed to the right of the previous ones.
        oBalloon.PlacementDirection = kBottomDirection

        Dim ValueSetCount As Long
        ValueSetCount = 1

        Dim oBalloonValueSet As BalloonValueSet

        ' Iterate over each value set (attached balloons) in a balloon.
        For Each oBalloonValueSet In oBalloon.BalloonValueSets

            ' Change the override value.
            oBalloonValueSet.OverrideValue = "Balloon" & BalloonCount & ": ValueSet" & ValueSetCount
            ValueSetCount = ValueSetCount + 1
        Next
        BalloonCount = BalloonCount + 1
    Next
End Sub
```

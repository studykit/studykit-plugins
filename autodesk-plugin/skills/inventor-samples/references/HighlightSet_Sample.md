# Highlight Feature Faces

## Description

This sample highlights the faces of an extrusion, revolution, or hole feature. It differentiates the faces on the start cap, end cap, and side faces by highlighting them in different colors. The HighlightFeatureFaces sub highlights the feature faces. Since the highlight set objects are declared outside of this sub, the highlighting remains after the sub has finished executing. Use the ClearHighlight sub to clear the highlighting that does so by releasing the HighlightSet objects.

## Code Samples

* [VBA](#VBA)

```
Private oStartHLSet As HighlightSet
Private oEndHLSet As HighlightSet
Private oSideHLSet As HighlightSet

Public Sub HighlightFeatureFaces()
    ' Get the first item in the select set. This assumes it is a feature.
    If ThisApplication.ActiveDocument.SelectSet.Count > 0 Then
        Dim oFeature As PartFeature
        Set oFeature = ThisApplication.ActiveDocument.SelectSet.Item(1)
    Else
        MsgBox "You must select a feature."
        Exit Sub
    End If

    ' Check to see that it's an extrusion, revolution or hole feature.
    If oFeature.Type  kExtrudeFeatureObject And _
       oFeature.Type  kRevolveFeatureObject And _
       oFeature.Type  kHoleFeatureObject Then
        MsgBox "You must select an extrusion, revolution, or hole."
        Exit Sub
    End If

    ' Create a new highlight set for the start face(s).
    Set oStartHLSet = ThisApplication.ActiveDocument.CreateHighlightSet

    ' Change the highlight color for the set to red.
    Dim oRed As Color
    Set oRed = ThisApplication.TransientObjects.CreateColor(255, 0, 0)

    ' Set the opacity
    oRed.Opacity = 0.8

    oStartHLSet.Color = oRed

    ' Add all start faces to the highlightset. Skip holes because
    ' they don't support the StartFaces property.
    If oFeature.Type  kHoleFeatureObject Then
        Dim oFace As Face
        For Each oFace In oFeature.StartFaces
            oStartHLSet.AddItem oFace
        Next
    End If

    ' Create a new highlight set for the end face(s).
    Set oEndHLSet = ThisApplication.ActiveDocument.CreateHighlightSet

    ' Change the highlight color for the set to green.
    Dim oGreen As Color
    Set oGreen = ThisApplication.TransientObjects.CreateColor(0, 255, 0)

    oEndHLSet.Color = oGreen

    ' Add all end faces to the highlightset.
    For Each oFace In oFeature.EndFaces
        oEndHLSet.AddItem oFace
    Next

    ' Create a new highlight set for the side face(s).
    Set oSideHLSet = ThisApplication.ActiveDocument.CreateHighlightSet

    ' Change the highlight color for the set to blue.
    Dim oBlue As Color
    Set oBlue = ThisApplication.TransientObjects.CreateColor(0, 0, 255)

    oSideHLSet.Color = oBlue

    ' Add all end faces to the highlightset.
    For Each oFace In oFeature.SideFaces
        oSideHLSet.AddItem oFace
    Next

    MsgBox "Start faces are displayed in red." & Chr(13) & _
            "End faces are displayed in green." & Chr(13) & _
            "Side faces are displayed in blue.", vbOKOnly + vbInformation
End Sub

Public Sub ClearHighlight()

    ' Release the highlight set objects to clear highlighting.
    ' Alternatively, HighlightSet.Delete or HighlightSet.Clear
    ' can also be used to clear the highlighting.

    Set oStartHLSet = Nothing
    Set oEndHLSet = Nothing
    Set oSideHLSet = Nothing
End Sub
```

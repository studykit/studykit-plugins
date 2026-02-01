# Move Feature Creation

## Description

Demonstrates the creation of a Move feature.

## Code Samples

* [VBA](#VBA)

To use this sample a part must be active.

```
Public Sub MoveFeatureCreationSample()
    ' Get the active part document.
    Dim oDoc As PartDocument
    Set oDoc = ThisApplication.ActiveDocument

    If oDoc Is Nothing Then
        MsgBox "No part document!" & vbCrLf & "Please open a part with solids in it for this sample to run.", vbCritical, "Autodesk Inventor"
        Exit Sub
    End If

    Dim oCompDef As PartComponentDefinition
    Set oCompDef = oDoc.ComponentDefinition

    If oCompDef.SurfaceBodies.Count = 0 Then
        MsgBox "No solids to move!" & vbCrLf & "Please open a part with solids in it for this sample to run.", vbCritical, "Autodesk Inventor"
        Exit Sub
    End If

    Dim oBodies As ObjectCollection
    Set oBodies = ThisApplication.TransientObjects.CreateObjectCollection

    ' Specify a body to move.
    oBodies.Add oCompDef.SurfaceBodies(1)

    ' Create a MoveFeatureDefinition.
    Dim oMoveDef As MoveDefinition
    Set oMoveDef = oCompDef.Features.MoveFeatures.CreateMoveDefinition(oBodies)

    ' Set the move operations onto the bodies.
    Dim oFreeDrag As FreeDragMoveOperation
    Set oFreeDrag = oMoveDef.AddFreeDrag(1, 1, 1)

    Dim oMoveAlongRay As MoveAlongRayMoveOperation
    Set oMoveAlongRay = oMoveDef.AddMoveAlongRay(oCompDef.WorkAxes(2), True, 2)

    Dim oRotateAboutAxis As RotateAboutLineMoveOperation
    Set oRotateAboutAxis = oMoveDef.AddRotateAboutAxis(oCompDef.WorkAxes(3), True, 0.5)

    ' Create the move feature.
    Dim oMoveFeature As MoveFeature
    Set oMoveFeature = oCompDef.Features.MoveFeatures.Add(oMoveDef)
End Sub
```

# Add a punch tool feature

## Description

This program demonstrates the creation of a punch tool feature. It uses one of the punch features that's delivered with Inventor. It assumes you already have an existing sheet metal part and have selected a face to place the punch feature on. The selected face should be large so there is room for the punch features.

## Code Samples

* [VBA](#VBA)

```
Public Sub PlacePunchFeature()
    ' Get the active sheet metal document and component
    ' definition of the active document.
    On Error Resume Next
    Dim oPartDoc As PartDocument
    Set oPartDoc = ThisApplication.ActiveDocument
    If Err Then
        MsgBox "A part must be active."
        Exit Sub
    End If
    Dim oSMDef As SheetMetalComponentDefinition
    Set oSMDef = oPartDoc.ComponentDefinition

    ' Get the selected face that will be used for the creation
    ' of the sketch that will contain the sketch points.
    Dim oFace As Face
    Set oFace = oPartDoc.SelectSet.Item(1)
    If Err Then
        MsgBox "A planar face must be selected."
        Exit Sub
    End If
    On Error GoTo 0

    If oFace.SurfaceType  kPlaneSurface Then
        MsgBox "A planar face must be selected."
        Exit Sub
    End If

    ' Create a sketch on the selected face.
    Dim oSketch As PlanarSketch
    Set oSketch = oSMDef.Sketches.Add(oFace)

    ' Create some points on the sketch.  The model will need to
    ' be of a size that these points lie on the model.
    Dim oPoints As ObjectCollection
    Set oPoints = ThisApplication.TransientObjects.CreateObjectCollection

    Dim oTG As TransientGeometry
    Set oTG = ThisApplication.TransientGeometry

    Dim oPoint As SketchPoint
    Set oPoint = oSketch.SketchPoints.Add(oTG.CreatePoint2d(2, 2), True)
    Call oPoints.Add(oPoint)

    Set oPoint = oSketch.SketchPoints.Add(oTG.CreatePoint2d(8, 3), True)
    Call oPoints.Add(oPoint)

    Set oPoint = oSketch.SketchPoints.Add(oTG.CreatePoint2d(2, 10), False)
    Call oPoints.Add(oPoint)
    Dim oSMFeatures As SheetMetalFeatures
    Set oSMFeatures = oSMDef.Features

    ' Create an iFeatureDefinition object for a punch tool.
    Dim oiFeatureDef As iFeatureDefinition
    Set oiFeatureDef = oSMFeatures.PunchToolFeatures.CreateiFeatureDefinition( _
        "C:\Program Files\Autodesk\Inventor 2010\Catalog\Punches\keyhole.ide")

    ' Set the input.
    Dim oInput As iFeatureInput
    For Each oInput In oiFeatureDef.iFeatureInputs
        Dim oParamInput As iFeatureParameterInput
        Select Case oInput.Name
            Case "Length"
                Set oParamInput = oInput
                oParamInput.Expression = "1 in"
            Case "Hole_Diameter"
                Set oParamInput = oInput
                oParamInput.Expression = "0.5 in"
            Case "Slot_Width"
                Set oParamInput = oInput
                oParamInput.Expression = "0.3875 in"
            Case "Fillet"
                Set oParamInput = oInput
                oParamInput.Expression = "0.0625 in"
            Case "Thickness"
                Set oParamInput = oInput
                oParamInput.Expression = "0.125 in"
        End Select
    Next

    ' Create the iFeature at a 45 degree angle.
    Dim oPunchTool As PunchToolFeature
    Set oPunchTool = oSMFeatures.PunchToolFeatures.Add(oPoints, oiFeatureDef, 3.14159265358979 / 4)
End Sub
```

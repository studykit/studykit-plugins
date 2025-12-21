# Placement of a standard iFeature

## Description

This program demonstrates the placement of a standard iFeature in a part.

## Code Samples

* [VBA](#VBA)

A part must be open and a planar face within that part selected. The iFeature used is delivered as a sample with Inventor.

|  |
| --- |
| Copy Code |

```
Public Sub PlaceiFeature()
    ' Get the part document and component definition of the active document.
    On Error Resume Next
    Dim oPartDoc As PartDocument
    Set oPartDoc = ThisApplication.ActiveDocument
    If Err Then
        MsgBox "A part must be active."
        Exit Sub
    End If

    Dim oPartDef As PartComponentDefinition
    Set oPartDef = oPartDoc.ComponentDefinition

    ' Get the selected face to use as input for the iFeature.
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

    Dim oFeatures As PartFeatures
    Set oFeatures = oPartDef.Features

    ' Create an iFeatureDefinition object.
    Dim oiFeatureDef As iFeatureDefinition
    Set oiFeatureDef = oFeatures.iFeatures.CreateiFeatureDefinition( _
"C:\Program Files\Autodesk\Inventor 2010\Catalog\Slots\End_mill_curved.ide")

    ' Set the input.
    Dim oInput As iFeatureInput
    For Each oInput In oiFeatureDef.iFeatureInputs
        Dim oParamInput As iFeatureParameterInput
        Select Case oInput.Name
            Case "Sketch Plane"
                Dim oPlaneInput As iFeatureSketchPlaneInput
                Set oPlaneInput = oInput
                oPlaneInput.PlaneInput = oFace
            Case "Diameter"
                Set oParamInput = oInput
                oParamInput.Expression = "1 in"
            Case "Depth"
                Set oParamInput = oInput
                oParamInput.Expression = "0.5 in"
        End Select
    Next

    ' Create the iFeature.
    Dim oiFeature As iFeature
    Set oiFeature = oFeatures.iFeatures.Add(oiFeatureDef)
End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
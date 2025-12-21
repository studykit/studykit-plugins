# Sketch profile control

## Description

This sample demonstrates the usage of the Profiles API to control the shape of the profile. The sample creates three concntric circles and creates an extrusion of the region between the inner circles.

## Code Samples

* [VBA](#VBA)

|  |
| --- |
| Copy Code |

```
Public Sub SketchProfileControl()
    ' Create a new part document, using the default part template.
    Dim oPartDoc As PartDocument
    Set oPartDoc = ThisApplication.Documents.Add(kPartDocumentObject, _
    ThisApplication.FileManager.GetTemplateFile(kPartDocumentObject))

    ' Set a reference to the component definition.
    Dim oCompDef As PartComponentDefinition
    Set oCompDef = oPartDoc.ComponentDefinition

    ' Create a new sketch on the X-Y work plane. Since it's being created on
    ' one of the base workplanes we know the orientation it will be created in
    ' and don't need to worry about controlling it. Because of this we also
    ' know the origin of the sketch plane will be at (0,0,0) in model space.
    Dim oSketch As PlanarSketch
    Set oSketch = oCompDef.Sketches.Add(oCompDef.WorkPlanes(3))

    ' Set a reference to the transient geometry object.
    Dim oTransGeom As TransientGeometry
    Set oTransGeom = ThisApplication.TransientGeometry

    ' Draw 3 concentric circles.

    Dim oCircle1 As SketchCircle
    Set oCircle1 = oSketch.SketchCircles.AddByCenterRadius( _
    oTransGeom.CreatePoint2d(5, 5), 6)

    Dim oCircle2 As SketchCircle
    Set oCircle2 = oSketch.SketchCircles.AddByCenterRadius( _
    oTransGeom.CreatePoint2d(5, 5), 4)

    Dim oCircle3 As SketchCircle
    Set oCircle3 = oSketch.SketchCircles.AddByCenterRadius( _
    oTransGeom.CreatePoint2d(5, 5), 2)

    ' Create a profile.
    Dim oProfile As Profile
    Set oProfile = oSketch.Profiles.AddForSolid

    ' Modify the profile: the returned profile consists of 3
    ' paths each corresponding to a sketch circle. The desired
    ' result is that the innermost path removes material and the
    ' second path adds material. The outermost path is not needed
    ' and is hence deleted.
    Dim oProfPath As ProfilePath
    For Each oProfPath In oProfile
      If oProfPath.Item(1).SketchEntity Is oCircle3 Then
        oProfPath.AddsMaterial = False
      ElseIf oProfPath.Item(1).SketchEntity Is oCircle2 Then
        oProfPath.AddsMaterial = False
      Else
        oProfPath.Delete
      End If
    Next

    ' Create a base extrusion 1cm thick.
    Dim oExtrudeDef As ExtrudeDefinition
    Set oExtrudeDef = oCompDef.Features.ExtrudeFeatures.CreateExtrudeDefinition(oProfile, kJoinOperation)
    Call oExtrudeDef.SetDistanceExtent(1, kNegativeExtentDirection)
    Dim oExtrude As ExtrudeFeature
    Set oExtrude = oCompDef.Features.ExtrudeFeatures.Add(oExtrudeDef)

    'Make the sketch visible for better visualization
    oSketch.Visible = True
End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
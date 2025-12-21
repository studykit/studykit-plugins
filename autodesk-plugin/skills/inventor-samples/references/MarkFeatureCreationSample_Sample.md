# Mark feature creation sample

## Description

This sample demonstrates how to create a mark feature in part document.

## Code Samples

* [VBA](#VBA)
* [VBA](#VBA)

This sample demonstrates how to create a mark feature in part document.

|  |
| --- |
| Copy Code |

```
Sub MarkFeatureSample()
    ' Create a new part document.
    Dim oPartDoc As PartDocument
    Set oPartDoc = ThisApplication.Documents.Add(kPartDocumentObject)

    ' Set a reference to the component definition.
    Dim oCompDef As PartComponentDefinition
    Set oCompDef = oPartDoc.ComponentDefinition

    ' Create a new sketch on the X-Y work plane.
    Dim oSketch As PlanarSketch
    Set oSketch = oCompDef.Sketches.Add(oCompDef.WorkPlanes(3))

    ' Set a reference to the transient geometry object.
    Dim oTransGeom As TransientGeometry
    Set oTransGeom = ThisApplication.TransientGeometry

    ' Draw a 4cm x 3cm rectangle with the corner at (0,0)
    Dim oRectangleLines As SketchEntitiesEnumerator
    Set oRectangleLines = oSketch.SketchLines.AddAsTwoPointRectangle( _
    oTransGeom.CreatePoint2d(0, 0), _
    oTransGeom.CreatePoint2d(4, 3))

    ' Create a profile.
    Dim oProfile As Profile
    Set oProfile = oSketch.Profiles.AddForSolid

    ' Create a base extrusion 1cm thick.
    Dim oExtrudeDef As ExtrudeDefinition
    Set oExtrudeDef = oCompDef.Features.ExtrudeFeatures.CreateExtrudeDefinition(oProfile, kJoinOperation)
    Call oExtrudeDef.SetDistanceExtent(1, kNegativeExtentDirection)
    Dim oExtrude1 As ExtrudeFeature
    Set oExtrude1 = oCompDef.Features.ExtrudeFeatures.Add(oExtrudeDef)

    ' Get the top face of the extrusion to use for creating the new sketch.
    Dim oFrontFace As Face
    Set oFrontFace = oExtrude1.StartFaces.Item(1)

    ' Create a new sketch on this face
    Set oSketch = oCompDef.Sketches.AddWithOrientation(oFrontFace, _
    oCompDef.WorkAxes.Item(1), True, True, oCompDef.WorkPoints(1))

    ' Determine where in sketch space the point (0.5,0.5,0) is.
    Dim oCorner As Point2d
    Set oCorner = oSketch.ModelToSketchSpace(oTransGeom.CreatePoint(0.5, 0.5, 0))

    ' Create the interior 3cm x 2cm rectangle for the pocket.
    Set oRectangleLines = oSketch.SketchLines.AddAsTwoPointRectangle( _
    oCorner, oTransGeom.CreatePoint2d(oCorner.X + 3, oCorner.Y + 2))

    Dim oGeometries As ObjectCollection
    Set oGeometries = ThisApplication.TransientObjects.CreateObjectCollection

    Dim i As Long
    For i = 1 To oRectangleLines.Count
        oGeometries.Add oRectangleLines(i)
    Next

    Dim oMarkFeatures As MarkFeatures
    Set oMarkFeatures = oCompDef.Features.MarkFeatures

    ' Get a mark style.
    Dim oMarkStyle As MarkStyle
    Set oMarkStyle = oPartDoc.MarkStyles.Item(1)

    ' Create mark definition.
    Dim oMarkDef As MarkDefinition
    Set oMarkDef = oMarkFeatures.CreateMarkDefinition(oGeometries, oMarkStyle)

    ' Create a mark feature.
    Dim oMark As MarkFeature
    Set oMark = oMarkFeatures.Add(oMarkDef)
End Sub
```

This sample demonstrates how to create a mark feature in part document.

|  |
| --- |
| Copy Code |

```
Sub MarkFeatureSample()
    ' Create a new part document.
    Dim oPartDoc As PartDocument
    Set oPartDoc = ThisApplication.Documents.Add(kPartDocumentObject)

    ' Set a reference to the component definition.
    Dim oCompDef As PartComponentDefinition
    Set oCompDef = oPartDoc.ComponentDefinition

    ' Create a new sketch on the X-Y work plane.
    Dim oSketch As PlanarSketch
    Set oSketch = oCompDef.Sketches.Add(oCompDef.WorkPlanes(3))

    ' Set a reference to the transient geometry object.
    Dim oTransGeom As TransientGeometry
    Set oTransGeom = ThisApplication.TransientGeometry

    ' Draw a 4cm x 3cm rectangle with the corner at (0,0)
    Dim oRectangleLines As SketchEntitiesEnumerator
    Set oRectangleLines = oSketch.SketchLines.AddAsTwoPointRectangle( _
    oTransGeom.CreatePoint2d(0, 0), _
    oTransGeom.CreatePoint2d(4, 3))

    ' Create a profile.
    Dim oProfile As Profile
    Set oProfile = oSketch.Profiles.AddForSolid

    ' Create a base extrusion 1cm thick.
    Dim oExtrudeDef As ExtrudeDefinition
    Set oExtrudeDef = oCompDef.Features.ExtrudeFeatures.CreateExtrudeDefinition(oProfile, kJoinOperation)
    Call oExtrudeDef.SetDistanceExtent(1, kNegativeExtentDirection)
    Dim oExtrude1 As ExtrudeFeature
    Set oExtrude1 = oCompDef.Features.ExtrudeFeatures.Add(oExtrudeDef)

    ' Get the top face of the extrusion to use for creating the new sketch.
    Dim oFrontFace As Face
    Set oFrontFace = oExtrude1.StartFaces.Item(1)

    ' Create a new sketch on this face
    Set oSketch = oCompDef.Sketches.AddWithOrientation(oFrontFace, _
    oCompDef.WorkAxes.Item(1), True, True, oCompDef.WorkPoints(1))

    ' Determine where in sketch space the point (0.5,0.5,0) is.
    Dim oCorner As Point2d
    Set oCorner = oSketch.ModelToSketchSpace(oTransGeom.CreatePoint(0.5, 0.5, 0))

    ' Create the interior 3cm x 2cm rectangle for the pocket.
    Set oRectangleLines = oSketch.SketchLines.AddAsTwoPointRectangle( _
    oCorner, oTransGeom.CreatePoint2d(oCorner.X + 3, oCorner.Y + 2))

    Dim oGeometries As ObjectCollection
    Set oGeometries = ThisApplication.TransientObjects.CreateObjectCollection

    Dim i As Long
    For i = 1 To oRectangleLines.Count
        oGeometries.Add oRectangleLines(i)
    Next

    Dim oMarkFeatures As MarkFeatures
    Set oMarkFeatures = oCompDef.Features.MarkFeatures

    ' Get a mark style.
    Dim oMarkStyle As MarkStyle
    Set oMarkStyle = oPartDoc.MarkStyles.Item(1)

    ' Create mark definition.
    Dim oMarkDef As MarkDefinition
    Set oMarkDef = oMarkFeatures.CreateMarkDefinition(oGeometries, oMarkStyle)

    ' Create a mark feature.
    Dim oMark As MarkFeature
    Set oMark = oMarkFeatures.Add(oMarkDef)
End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
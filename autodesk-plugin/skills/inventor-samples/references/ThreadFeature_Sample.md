# Thread Feature Create

## Description

This sample demonstrates the creation of a thread feature. It creates a cylinder in a new part document and creates a thread feature on the cylinder.

## Code Samples

* [VBA](#VBA)

```
Public Sub ThreadSample()
    ' Create a new part document, using the default part template.
    Dim oPartDoc As PartDocument
    Set oPartDoc = ThisApplication.Documents.Add(kPartDocumentObject, _
                 ThisApplication.FileManager.GetTemplateFile(kPartDocumentObject))

    ' Set a reference to the component definition.
    Dim oCompDef As PartComponentDefinition
    Set oCompDef = oPartDoc.ComponentDefinition

    ' Create a new sketch on the X-Y work plane.
    Dim oSketch As PlanarSketch
    Set oSketch = oCompDef.Sketches.Add(oCompDef.WorkPlanes.Item(3))

    ' Create a sketch circle.  (The radius is for 1 5/8 inch diameter shaft.)
    Dim oCircle As SketchCircle
    Set oCircle = oSketch.SketchCircles.AddByCenterRadius( _
                    ThisApplication.TransientGeometry.CreatePoint2d(0, 0), 4.1275 / 2)

    Dim oProfile As Profile
    Set oProfile = oSketch.Profiles.AddForSolid

    ' Extrude the circle to create a cylinder.
    Dim oExtrudeDef As ExtrudeDefinition
    Set oExtrudeDef = oCompDef.Features.ExtrudeFeatures.CreateExtrudeDefinition(oProfile, kJoinOperation)
    Call oExtrudeDef.SetDistanceExtent(5, kPositiveExtentDirection)
    Dim oExtrude As ExtrudeFeature
    Set oExtrude = oCompDef.Features.ExtrudeFeatures.Add(oExtrudeDef)

    oSketch.Visible = False

    ' Set a reference to the ThreadFeatures collection object.
    Dim oThreadFeatures As ThreadFeatures
    Set oThreadFeatures = oCompDef.Features.ThreadFeatures

    ' Define all of the thread information.
    Dim oThreadInfo As ThreadInfo
    Set oThreadInfo = oThreadFeatures.CreateStandardThreadInfo( _
                        False, True, "ANSI Unified Screw Threads", _
                        "1 5/8-6 UN", "2A")

    ' Get the face the thread will be applied to.
    Dim oFace As Face
    Set oFace = oExtrude.SideFaces.Item(1)

    ' Get the edge the thread extent will be measured from.
    Dim oEdge As Edge
    Set oEdge = oExtrude.EndFaces.Item(1).Edges.Item(1)

    ' Create the thread feature.
    Dim oThreadFeature As ThreadFeature
    Set oThreadFeature = oThreadFeatures.Add(oFace, oEdge, oThreadInfo, _
                                                False, False, "2 cm", 0)
End Sub
```

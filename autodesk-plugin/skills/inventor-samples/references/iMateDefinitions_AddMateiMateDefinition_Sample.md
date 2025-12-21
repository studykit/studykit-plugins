# Add iMate Definition

## Description

Add iMate definitions using AddMateiMateDefinition and AddInsertiMateDefinition.

## Code Samples

* [VBA](#VBA)

|  |
| --- |
| Copy Code |

```
Public Sub CreateiMateDefinitionSample()
    ' Create a new part document, using the default part template.
    Dim oPartDoc As PartDocument
    Set oPartDoc = ThisApplication.Documents.Add(kPartDocumentObject, _
                ThisApplication.FileManager.GetTemplateFile(kPartDocumentObject))

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
    Set oExtrudeDef = oCompDef.Features.ExtrudeFeatures.CreateExtrudeDefinition(oProfile, kNewBodyOperation)
    Call oExtrudeDef.SetDistanceExtent(1, kNegativeExtentDirection)
    Dim oExtrude1 As ExtrudeFeature
    Set oExtrude1 = oCompDef.Features.ExtrudeFeatures.Add(oExtrudeDef)

    ' Get the top face of the extrusion to use for creating the new sketch.
    Dim oFrontFace As Face
    Set oFrontFace = oExtrude1.StartFaces.Item(1)

    ' Create a new sketch on this face, but use the method that allows you to
    ' control the orientation and orgin of the new sketch.
    Set oSketch = oCompDef.Sketches.AddWithOrientation(oFrontFace, _
                    oCompDef.WorkAxes.Item(1), True, True, oCompDef.WorkPoints(1))

    ' Create a sketch circle with the center at (2, 1.5).
    Dim oCircle As SketchCircle
    Set oCircle = oSketch.SketchCircles.AddByCenterRadius(oTransGeom.CreatePoint2d(2, 1.5), 0.5)

    ' Create a profile.
    Set oProfile = oSketch.Profiles.AddForSolid

    ' Create the second extrude (a hole).
    Dim oExtrude2 As ExtrudeFeature
    Set oExtrude2 = oCompDef.Features.ExtrudeFeatures.AddByThroughAllExtent( _
                        oProfile, kNegativeExtentDirection, kCutOperation)

    ' Create a mate iMateDefinition on a side face of the first extrude.
    Dim oMateiMateDefinition As MateiMateDefinition
    Set oMateiMateDefinition = oCompDef.iMateDefinitions.AddMateiMateDefinition( _
                        oExtrude1.SideFaces.Item(1), 0, , , "MateA")

    ' Create a match list of names to use for the next iMateDefinition.
    Dim strMatchList(2) As String
    strMatchList(0) = "InsertA"
    strMatchList(1) = "InsertB"
    strMatchList(2) = "InsertC"

    ' Create an insert iMateDefinition on the cylindrical face of the second extrude.
    Dim oInsertiMateDefinition As InsertiMateDefinition
    Set oInsertiMateDefinition = oCompDef.iMateDefinitions.AddInsertiMateDefinition( _
                        oExtrude2.SideFaces.Item(1), False, 0, , "InsertA", strMatchList)
End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
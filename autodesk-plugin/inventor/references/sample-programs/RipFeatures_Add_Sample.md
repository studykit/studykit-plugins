# Create sheet metal rip feature

## Description

This sample demonstrates the creation of a rip sheet metal feature.

## Code Samples

* [VBA](#VBA)

|  |
| --- |
| Copy Code |

```
Public Sub RipFeatureCreation()
    ' Create a new sheet metal document, using the default sheet metal template.
    Dim oSheetMetalDoc As PartDocument
    Set oSheetMetalDoc = ThisApplication.Documents.Add(kPartDocumentObject, _
                 ThisApplication.FileManager.GetTemplateFile(kPartDocumentObject, , , "{9C464203-9BAE-11D3-8BAD-0060B0CE6BB4}"))

    ' Set a reference to the component definition.
    Dim oCompDef As SheetMetalComponentDefinition
    Set oCompDef = oSheetMetalDoc.ComponentDefinition

    ' Set a reference to the sheet metal features collection.
    Dim oSheetMetalFeatures As SheetMetalFeatures
    Set oSheetMetalFeatures = oCompDef.Features

    ' Create a new sketch on the X-Y work plane.
    Dim oSketch As PlanarSketch
    Set oSketch = oCompDef.Sketches.Add(oCompDef.WorkPlanes.Item(3))

    ' Set a reference to the transient geometry object.
    Dim oTransGeom As TransientGeometry
    Set oTransGeom = ThisApplication.TransientGeometry

    ' Draw a 4cm x 2cm rectangle with the corner at (0,0)
    Call oSketch.SketchLines.AddAsTwoPointRectangle( _
                                oTransGeom.CreatePoint2d(0, 0), _
                                oTransGeom.CreatePoint2d(4, 2))

    Dim oSketchLines As ObjectCollection
    Set oSketchLines = ThisApplication.TransientObjects.CreateObjectCollection

    oSketchLines.Add oSketch.SketchLines(1)

    Call oSketch.OffsetSketchEntitiesUsingDistance(oSketchLines, oCompDef.Thickness.Value, True, True)

    ' Create a profile.
    Dim oProfile As Profile
    Set oProfile = oSketch.Profiles.AddForSolid

    ' Create an extrude feature.
    Dim oExtrudeDef As ExtrudeDefinition
    Set oExtrudeDef = oCompDef.Features.ExtrudeFeatures.CreateExtrudeDefinition(oProfile, kNewBodyOperation)
    Call oExtrudeDef.SetDistanceExtent("1 in", kPositiveExtentDirection)
    Dim oExtrude As ExtrudeFeature
    Set oExtrude = oCompDef.Features.ExtrudeFeatures.Add(oExtrudeDef)

    ' Create bends at all concave edges.
    Dim oEdgeColl As EdgeCollection
    Set oEdgeColl = oExtrude.SurfaceBodies(1).ConcaveEdges

    Dim oBendEdge As Edge
    For Each oBendEdge In oEdgeColl

        Dim oTempColl As EdgeCollection
        Set oTempColl = ThisApplication.TransientObjects.CreateEdgeCollection

        oTempColl.Add oBendEdge

        Dim oBendDef As BendDefinition
        Set oBendDef = oSheetMetalFeatures.BendFeatures.CreateBendDefinition(oTempColl)

        Dim oBendFeature As BendFeature
        Set oBendFeature = oSheetMetalFeatures.BendFeatures.Add(oBendDef)

    Next

    ' Get the first side face of the extrude
    Dim oSideFace As Face
    Set oSideFace = oExtrude.SideFaces.Item(1)

    ' Get any edge on the face that is parallel to the sketch plane
    Dim oEdge As Edge
    For Each oEdge In oSideFace.Edges

        Dim oLineSeg As LineSegment
        Set oLineSeg = oEdge.Geometry

        Dim oLine As Line
        Set oLine = oTransGeom.CreateLine(oLineSeg.StartPoint, oLineSeg.Direction.AsVector)

        If oSketch.PlanarEntityGeometry.IsParallelTo(oLine) Then
            Exit For
        End If
    Next

    ' Create a workpoint at the edge mid-point
    Dim oWorkPoint As WorkPoint
    Set oWorkPoint = oCompDef.WorkPoints.AddByMidPoint(oEdge)

    ' Create a single point type rip feature
    Dim oRipDef As RipDefinition
    Set oRipDef = oSheetMetalFeatures.RipFeatures.CreateRipDefinition(oSideFace)

    Call oRipDef.SetSinglePointRipType(oSideFace, oWorkPoint, oCompDef.GapSize.Value, kSymmetricExtentDirection)

    Dim oRipFeature As RipFeature
    Set oRipFeature = oSheetMetalFeatures.RipFeatures.Add(oRipDef)

    ThisApplication.ActiveView.GoHome
End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
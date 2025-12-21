# Sketch from Face Silhouette

## Description

This sample creates a cylindrical solid, creates a new sketch plane and creates some new sketch lines from the actual edges and the apparent (silhouette) edges of the cylinder.

## Code Samples

* [VBA](#VBA)

```
Public Sub SilhouetteSample()
    ' Create a new part document using the default part template.
    Dim oPartDoc As PartDocument
    Set oPartDoc = ThisApplication.Documents.Add(kPartDocumentObject, _
                ThisApplication.FileManager.GetTemplateFile(kPartDocumentObject))

    ' Set a reference to the part component definition.
    ' This assumes that a part document is active.
    Dim oCompDef As PartComponentDefinition
    Set oCompDef = oPartDoc.ComponentDefinition

    ' Create a new sketch on the X-Y work plane.
    Dim oSketch1 As PlanarSketch
    Set oSketch1 = oCompDef.Sketches.Add(oCompDef.WorkPlanes.Item(3))

    ' Set a reference to the transient geometry object.
    Dim oTransGeom As TransientGeometry
    Set oTransGeom = ThisApplication.TransientGeometry

    ' Draw a circle on the sketch.
    Dim oCircle As SketchCircle
    Set oCircle = oSketch1.SketchCircles.AddByCenterRadius( _
                                oTransGeom.CreatePoint2d(0, 0), 2)

    ' Create a profile.
    Dim oProfile As Profile
    Set oProfile = oSketch1.Profiles.AddForSolid

    ' Create a solid extrusion.
    Dim oExtrudeDef As ExtrudeDefinition
    Set oExtrudeDef = oCompDef.Features.ExtrudeFeatures.CreateExtrudeDefinition(oProfile, kNewBodyOperation)
    Call oExtrudeDef.SetDistanceExtent(3, kSymmetricExtentDirection)
    Dim oExtrusion As ExtrudeFeature
    Set oExtrusion = oCompDef.Features.ExtrudeFeatures.Add(oExtrudeDef)

    ' Create another sketch on the Y-Z plane.
    Dim oSketch2 As PlanarSketch
    Set oSketch2 = oCompDef.Sketches.Add(oCompDef.WorkPlanes(1))

    ' Get the cylindrical face of the solid.
    Dim oCylinder As Face
    Set oCylinder = oExtrusion.SideFaces.Item(1)

    ' Create a sketch line using the silhouette of the cylinder.  The proximity
    ' point determines which of the two silhouette edges will be used.
    Dim oSilhouetteCurve As SketchEntity
    Set oSilhouetteCurve = oSketch2.AddBySilhouette(oCylinder, _
                                    oTransGeom.CreatePoint(0, -1, 0))

    ' Create another sketch line from the silhouette on the
    ' other side of the cylinder.
    Set oSilhouetteCurve = oSketch2.AddBySilhouette(oCylinder, _
                                    oTransGeom.CreatePoint(0, 1, 0))

    ' Create sketch lines from the ends of the cylinder.  This takes
    ' advantage of the fact that a cylinder only has two edges.
    Dim oEndLine As SketchEntity
    Set oEndLine = oSketch2.AddByProjectingEntity( _
                            oExtrusion.StartFaces.Item(1).Edges.Item(1))
    Set oEndLine = oSketch2.AddByProjectingEntity( _
                            oExtrusion.EndFaces.Item(1).Edges.Item(1))
End Sub
```

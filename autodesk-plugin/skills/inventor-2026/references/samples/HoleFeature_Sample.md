# Hole Feature - Through holes (RegularAndTapped)

## Description

This sample demonstrates the creation of through holes, both regular and tapped.

## Code Samples

* [VBA](#VBA)

```
Public Sub HoleSample()
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

    ' Set a reference to the transient geometry object.
    Dim oTransGeom As TransientGeometry
    Set oTransGeom = ThisApplication.TransientGeometry

    ' Create a rectangle on the sketch.
    Call oSketch.SketchLines.AddAsTwoPointRectangle( _
                                        oTransGeom.CreatePoint2d(0, 0), _
                                        oTransGeom.CreatePoint2d(6, 4))

    ' Create the profile.
    Dim oProfile As Profile
    Set oProfile = oSketch.Profiles.AddForSolid

    ' Create an extrusion.
    Dim oExtrudeDef As ExtrudeDefinition
    Set oExtrudeDef = oCompDef.Features.ExtrudeFeatures.CreateExtrudeDefinition(oProfile, kJoinOperation)
    Call oExtrudeDef.SetDistanceExtent("2 cm", kNegativeExtentDirection)
    Dim oExtrude As ExtrudeFeature
    Set oExtrude = oCompDef.Features.ExtrudeFeatures.Add(oExtrudeDef)

    ' Create a new sketch to contain the points that define the hole centers.
    Set oSketch = oCompDef.Sketches.Add(oCompDef.WorkPlanes.Item(3))

    ' Create an object collection for the hole center points.
    Dim oHoleCenters As ObjectCollection
    Set oHoleCenters = ThisApplication.TransientObjects.CreateObjectCollection

    ' Add two points as hole centers.
    oHoleCenters.Add oSketch.SketchPoints.Add(oTransGeom.CreatePoint2d(1, 1))
    oHoleCenters.Add oSketch.SketchPoints.Add(oTransGeom.CreatePoint2d(5, 1))

    ' Create the hole feature.
    Call oCompDef.Features.HoleFeatures.AddDrilledByThroughAllExtent( _
                            oHoleCenters, "1 cm", kPositiveExtentDirection)

    ' Define tap information.

    Dim oHoleTapInfo As HoleTapInfo
    Set oHoleTapInfo = oCompDef.Features.HoleFeatures.CreateTapInfo( _
                            True, "ANSI Unified Screw Threads", _
                            "7/16-14 UNC", "1B", False, "1 cm")

    ' Create a new sketch for the tapped hole centers.
    Set oSketch = oCompDef.Sketches.Add(oCompDef.WorkPlanes.Item(3))

    ' Create a new object collection for the hole center points.
    Set oHoleCenters = ThisApplication.TransientObjects.CreateObjectCollection

    ' Add two points as hole centers.
    oHoleCenters.Add oSketch.SketchPoints.Add(oTransGeom.CreatePoint2d(1, 3))
    oHoleCenters.Add oSketch.SketchPoints.Add(oTransGeom.CreatePoint2d(5, 3))

    ' Create the hole feature.
    Call oCompDef.Features.HoleFeatures.AddDrilledByThroughAllExtent( _
                            oHoleCenters, oHoleTapInfo, kPositiveExtentDirection)
End Sub
```

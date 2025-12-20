# Loft Feature With Non-Planar Section

## Description

This sample demonstrates the creation of a loft feature. It uses two sections for the loft, one is from a 2d sketch and the other is a non-planar section from a 3d sketch. Because one of the sketches isn't planar, a surface is created instead of a solid.

## Code Samples

* [VBA](#VBA)

|  |
| --- |
| Copy Code |

```
Public Sub CreateNonPlanarSectionLoft()
    ' Create a new part document, using the default part template.
    Dim oPartDoc As PartDocument
    Set oPartDoc = ThisApplication.Documents.Add(kPartDocumentObject, _
                ThisApplication.FileManager.GetTemplateFile(kPartDocumentObject))

    Dim oCompDef As PartComponentDefinition
    Set oCompDef = oPartDoc.ComponentDefinition

    Dim oTG As TransientGeometry
    Set oTG = ThisApplication.TransientGeometry

    ' Create a 2d sketch to use as one section.
    Dim oSketch As PlanarSketch
    Set oSketch = oCompDef.Sketches.Add(oCompDef.WorkPlanes.Item(3))
    Call oSketch.SketchCircles.AddByCenterRadius(oTG.CreatePoint2d(0, 0), 5)

    ' Create the profile to use as the section.
    Dim oProfile1 As Profile
    Set oProfile1 = oSketch.Profiles.AddForSolid

    ' Create a 3d sketch to use as the second section.
    Dim oSketch3d As Sketch3D
    Set oSketch3d = oCompDef.Sketches3D.Add

    Dim oWPs(1 To 6) As WorkPoint
    Set oWPs(1) = oCompDef.WorkPoints.AddFixed(oTG.CreatePoint(-8, 6, 10))
    Set oWPs(2) = oCompDef.WorkPoints.AddFixed(oTG.CreatePoint(-8, -6, 10))
    Set oWPs(3) = oCompDef.WorkPoints.AddFixed(oTG.CreatePoint(0, -4, 8))
    Set oWPs(4) = oCompDef.WorkPoints.AddFixed(oTG.CreatePoint(8, -6, 10))
    Set oWPs(5) = oCompDef.WorkPoints.AddFixed(oTG.CreatePoint(8, 6, 10))
    Set oWPs(6) = oCompDef.WorkPoints.AddFixed(oTG.CreatePoint(0, 4, 8))
    Dim oStartLine3d As SketchLine3D
    Set oStartLine3d = oSketch3d.SketchLines3D.AddByTwoPoints(oWPs(1), oWPs(2), True, 2)
    Dim oLine3d As SketchLine3D
    Set oLine3d = oSketch3d.SketchLines3D.AddByTwoPoints(oStartLine3d.EndSketchPoint, oWPs(3), True, 2)
    Set oLine3d = oSketch3d.SketchLines3D.AddByTwoPoints(oLine3d.EndSketchPoint, oWPs(4), True, 2)
    Set oLine3d = oSketch3d.SketchLines3D.AddByTwoPoints(oLine3d.EndSketchPoint, oWPs(5), True, 2)
    Set oLine3d = oSketch3d.SketchLines3D.AddByTwoPoints(oLine3d.EndSketchPoint, oWPs(6), True, 2)
    Set oLine3d = oSketch3d.SketchLines3D.AddByTwoPoints(oLine3d.EndSketchPoint, oStartLine3d.StartSketchPoint, True, 2)

    ' Create a 3d profile to use as the section. Even though this section
    ' is closed the AddOpen method must be used because it is non-planar.
    Dim oProfile2 As Profile3D
    Set oProfile2 = oSketch3d.Profiles3D.AddOpen

    ' Create an object collection for the sections.
    Dim oSections As ObjectCollection
    Set oSections = ThisApplication.TransientObjects.CreateObjectCollection
    Call oSections.Add(oProfile1)
    Call oSections.Add(oProfile2)

    ' Create the loft definition. Because one of the ends isn't planar,
    ' a surface must be created instead of a solid.
    Dim oLoftDefinition As LoftDefinition
    Set oLoftDefinition = oCompDef.Features.LoftFeatures.CreateLoftDefinition(oSections, kSurfaceOperation)

    ' Create the loft feature.
    Call oCompDef.Features.LoftFeatures.Add(oLoftDefinition)
End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
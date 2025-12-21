# Create primitive BRep

## Description

This sample demonstrates the creation of primitive (solid) BRep.

## Code Samples

* [VBA](#VBA)

|  |
| --- |
| Copy Code |

```
Public Sub CreateBRep()
    ' Create a new part document, using the default part template.
    Dim oPartDoc As PartDocument
    Set oPartDoc = ThisApplication.Documents.Add(kPartDocumentObject, _
                ThisApplication.FileManager.GetTemplateFile(kPartDocumentObject))

    ' Set a reference to the component definition.
    Dim oCompDef As PartComponentDefinition
    Set oCompDef = oPartDoc.ComponentDefinition

    ' Set a reference to the TransientBRep object.
    Dim oTransientBRep As TransientBRep
    Set oTransientBRep = ThisApplication.TransientBRep

    ' Create a range box that will define the extents of a block.
    Dim oBox As Box
    Set oBox = ThisApplication.TransientGeometry.CreateBox

    ' Expand in all directions by 1 cm.
    oBox.Expand 1

    ' Create the block.
    Dim oBody As SurfaceBody
    Set oBody = oTransientBRep.CreateSolidBlock(oBox)

    ' Create bottom and top points for a cylinder.
    Dim oBottomPt As Point
    Set oBottomPt = ThisApplication.TransientGeometry.CreatePoint(0, 1, 0)

    Dim oTopPt As Point
    Set oTopPt = ThisApplication.TransientGeometry.CreatePoint(0, 3, 0)

    ' Create the cylinder body.
    Dim oCylinder As SurfaceBody
    Set oCylinder = oTransientBRep.CreateSolidCylinderCone(oBottomPt, oTopPt, 0.5, 0.5, 0.5)

    ' Boolean the bodies; "oBody" will return the result
    Call oTransientBRep.DoBoolean(oBody, oCylinder, kBooleanTypeUnion)

    ' Create a base feature with the result body.
    Dim oBaseFeature As NonParametricBaseFeature
    Set oBaseFeature = oCompDef.Features.NonParametricBaseFeatures.Add(oBody)
End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
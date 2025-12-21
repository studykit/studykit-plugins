# Extrude sketch text

## Description

This sample demonstrates the creation of an extrude feature from sketch text.

## Code Samples

* [VBA](#VBA)

|  |
| --- |
| Copy Code |

```
Public Sub ExtrudeSketchText()
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

    ' Create a text box at (0,0)
    Dim oTextBox As TextBox
    Set oTextBox = oSketch.TextBoxes.AddFitted(oTransGeom.CreatePoint2d(0, 0), "Inventor")

    ' Add the text box to an object collection
    Dim oPaths As ObjectCollection
    Set oPaths = ThisApplication.TransientObjects.CreateObjectCollection
    oPaths.Add oTextBox

    ' Create a profile. Calling the AddForSolid method without any
    ' arguments will result in a profile containing all possible
    ' paths in the sketch. By passing in the text box, the profile
    ' is restricted to the input text path.
    Dim oProfile As Profile
    Set oProfile = oSketch.Profiles.AddForSolid(False, oPaths)

    ' Extrude the text.
    Dim oExtrudeDef As ExtrudeDefinition
    Set oExtrudeDef = oCompDef.Features.ExtrudeFeatures.CreateExtrudeDefinition(oProfile, kJoinOperation)
    Call oExtrudeDef.SetDistanceExtent(0.25, kNegativeExtentDirection)
    Dim oExtrude As ExtrudeFeature
    Set oExtrude = oCompDef.Features.ExtrudeFeatures.Add(oExtrudeDef)
End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
# UCS by transformation matrix

## Description

This sample demonstrates the creation of a user coordinate system (UCS) by specifying a transformation matrix.

## Code Samples

* [VBA](#VBA)

|  |
| --- |
| Copy Code |

```
Sub CreateUCSByTransformationMatrix()
    ' Create a new part document
    Dim oDoc As PartDocument
    Set oDoc = ThisApplication.Documents.Add(DocumentTypeEnum.kPartDocumentObject)

    ' Set a reference to the PartComponentDefinition object
    Dim oCompDef As PartComponentDefinition
    Set oCompDef = oDoc.ComponentDefinition

    Dim oTG As TransientGeometry
    Set oTG = ThisApplication.TransientGeometry

    ' Create an identity matrix
    Dim oMatrix As Matrix
    Set oMatrix = oTG.CreateMatrix

    ' Rotate about Z-Axis by 45 degrees
    Call oMatrix.SetToRotation(3.14159 / 4, oTG.CreateVector(0, 0, 1), oTG.CreatePoint(0, 0, 0))

    ' Translate the origin to (2, 2, 2)
    Dim oTranslationMatrix As Matrix
    Set oTranslationMatrix = oTG.CreateMatrix
    Call oTranslationMatrix.SetTranslation(oTG.CreateVector(2, 2, 2))

    Call oMatrix.TransformBy(oTranslationMatrix)

    ' Create an empty definition object
    Dim oUCSDef As UserCoordinateSystemDefinition
    Set oUCSDef = oCompDef.UserCoordinateSystems.CreateDefinition

    ' Set it to be based on the defined matrix
    oUCSDef.Transformation = oMatrix

    ' Create the UCS
    Dim oUCS As UserCoordinateSystem
    Set oUCS = oCompDef.UserCoordinateSystems.Add(oUCSDef)
End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
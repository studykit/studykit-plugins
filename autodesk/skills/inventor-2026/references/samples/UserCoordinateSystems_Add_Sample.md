# UCS by three points

## Description

This sample demonstrates the creation of a User Coordinate System (UCS) based on 3 points that define the origin, x-direction and y-direction for the UCS.

## Code Samples

* [VBA](#VBA)

```
Sub CreateUCSBy3Points()
    ' Create a new part document
    Dim oDoc As PartDocument
    Set oDoc = ThisApplication.Documents.Add(DocumentTypeEnum.kPartDocumentObject)

    ' Set a reference to the PartComponentDefinition object
    Dim oCompDef As PartComponentDefinition
    Set oCompDef = oDoc.ComponentDefinition

    Dim oTG As TransientGeometry
    Set oTG = ThisApplication.TransientGeometry

    ' Create 3 workpoints to define the origin, x-direction and y-direction points
    Dim oWorkPoint1 As WorkPoint
    Set oWorkPoint1 = oCompDef.WorkPoints.AddFixed(oTG.CreatePoint(2, 0, 0))

    Dim oWorkPoint2 As WorkPoint
    Set oWorkPoint2 = oCompDef.WorkPoints.AddFixed(oTG.CreatePoint(4, 0, 0))

    Dim oWorkPoint3 As WorkPoint
    Set oWorkPoint3 = oCompDef.WorkPoints.AddFixed(oTG.CreatePoint(2, 2, 0))

    ' Create an empty definition object
    Dim oUCSDef As UserCoordinateSystemDefinition
    Set oUCSDef = oCompDef.UserCoordinateSystems.CreateDefinition

    ' Set it to be based on the 3 points
    Call oUCSDef.SetByThreePoints(oWorkPoint1, oWorkPoint2, oWorkPoint3)

    ' Create the UCS
    Dim oUCS As UserCoordinateSystem
    Set oUCS = oCompDef.UserCoordinateSystems.Add(oUCSDef)
End Sub
```

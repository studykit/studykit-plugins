# Create planar AssemblyJoint with offset to origins

## Description

This sample demonstrates how to create a planar AssemblyJoint with offset to the OriginOne and OriginTwo.

## Code Samples

* [VBA](#VBA)

Create a part with some solid and make sure there are linear edges in it, save it as C:\Temp\Part1.ipt or you need to edit the VBA code to change the paths to make it work.

|  |
| --- |
| Copy Code |

```
Sub CreateAssemblyJointWithOffsetSample()
    Dim oDoc As AssemblyDocument
    Set oDoc = ThisApplication.Documents.Add(kAssemblyDocumentObject)

    Dim oCompDef As AssemblyComponentDefinition
    Set oCompDef = oDoc.ComponentDefinition

    Dim oMatrix As Matrix
    Set oMatrix = ThisApplication.TransientGeometry.CreateMatrix

    Dim oOccu1 As ComponentOccurrence
    Dim oOccu2 As ComponentOccurrence
    ' Create two occurrences for adding assembly joint, make sure the sample Part1 has linear edge in it.
    Set oOccu1 = oCompDef.Occurrences.Add("C:\Temp\Part1.ipt", oMatrix)
    oMatrix.SetTranslation ThisApplication.TransientGeometry.CreateVector(20, 20, 20)
    Set oOccu2 = oCompDef.Occurrences.Add("C:\Temp\Part1.ipt", oMatrix)

    ' Create two GeometryIntent objects for creating assembly joint.
    Dim oOriginOne As GeometryIntent, oOriginTwo As GeometryIntent
    Dim oEdge As Edge
    For Each oEdge In oOccu1.SurfaceBodies(1).Edges
        If oEdge.GeometryType = kLineSegmentCurve Then
            Set oOriginOne = oCompDef.CreateGeometryIntent(oEdge, kMidPointIntent)
            Exit For
        End If
    Next

    For Each oEdge In oOccu2.SurfaceBodies(1).Edges
        If oEdge.GeometryType = kLineSegmentCurve Then
            Set oOriginTwo = oCompDef.CreateGeometryIntent(oEdge, kMidPointIntent)
            Exit For
        End If
    Next

    ' Create AssemblyJointDefinition
    Dim oJointDef As AssemblyJointDefinition
    Set oJointDef = oCompDef.Joints.CreateAssemblyJointDefinition(kPlanarJointType, oOriginOne, oOriginTwo)

    Call oJointDef.SetOriginOneAsOffset(5, 5)
    Call oJointDef.SetOriginTwoAsOffset(2, 2)

    Debug.Print oJointDef.OriginOneDefinitionType = kOffsetOriginDefinitionType

    ' Create assembly joint.
    Dim oJoint As AssemblyJoint
    Set oJoint = oCompDef.Joints.Add(oJointDef)
End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
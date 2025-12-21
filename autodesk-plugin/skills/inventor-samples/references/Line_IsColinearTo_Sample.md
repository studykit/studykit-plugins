# Is cylindrical face interior or exterior?

## Description

This sample shows how to determine whether the selected cylindircal face is an exterior face or an interior (hollow) face.

## Code Samples

* [VBA](#VBA)

Before running the sample, select a cylindrical face.

|  |
| --- |
| Copy Code |

```
Public Sub IsCylindricalFaceInterior()
    Dim oDoc As Document
    Set oDoc = ThisApplication.ActiveDocument

    If Not Typeof oDoc.SelectSet(1) Is Face Then
        MsgBox "A face must be selected."
        Exit Sub
    End If

    Dim oFace As Face
    Set oFace = oDoc.SelectSet(1)

    If Not oFace.SurfaceType = kCylinderSurface Then
        MsgBox "A cylindrical face must be selected."
        Exit Sub
    End If

    Dim oCylinder As Cylinder
    Set oCylinder = oFace.Geometry

    Dim params(1) As Double
    params(0) = 0.5
    params(1) = 0.5

    ' Get point on surface at param .5,.5
    Dim points(2) As Double
    Call oFace.Evaluator.GetPointAtParam(params, points)

    ' Create point object
    Dim oPoint As point
    Set oPoint = ThisApplication.TransientGeometry.CreatePoint(points(0), points(1), points(2))

    ' Get normal at this point
    Dim normals(2) As Double
    Call oFace.Evaluator.GetNormal(params, normals)

    ' Create normal vector object
    Dim oNormal As Vector
    Set oNormal = ThisApplication.TransientGeometry.CreateVector(normals(0), normals(1), normals(2))

    ' Scale vector by radius of the cylinder
    oNormal.ScaleBy oCylinder.Radius

    ' Find the sampler point on the normal by adding the
    ' scaled normal vector to the point at .5,.5 param.
    Dim oSamplePoint As point
    Set oSamplePoint = oPoint

    oSamplePoint.TranslateBy oNormal

    ' Check if the sample point lies on the cylinder axis.
    ' If it does, we have a hollow face.

    ' Create a line describing the cylinder axis
    Dim oAxisLine As Line
    Set oAxisLine = ThisApplication.TransientGeometry.CreateLine _
        (oCylinder.BasePoint, oCylinder.AxisVector.AsVector)

    'Create a line parallel to the axis passing thru the sample point.
    Dim oSampleLine As Line
    Set oSampleLine = ThisApplication.TransientGeometry.CreateLine _
        (oSamplePoint, oCylinder.AxisVector.AsVector)

    If oSampleLine.IsColinearTo(oAxisLine) Then
        MsgBox "Interior face."
    Else
        MsgBox "Exterior face."
    End If
End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
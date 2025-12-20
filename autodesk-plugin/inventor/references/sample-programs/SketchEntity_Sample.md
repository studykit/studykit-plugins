# Sketch Display Entities

## Description

This sample demonstrates the query functionality available for sketch entities.

## Code Samples

* [VBA](#VBA)

To use this sample, select a sketch entity that you want to query. Run the program and it will display information about the selected entity in the immediate window.

|  |
| --- |
| Copy Code |

```
Public Sub SketchEntities()
    ' Get the first item in the select set.  This assumes
    ' something is selected and that it's a sketch entity.
    Dim oSketchEnt As SketchEntity
    Set oSketchEnt = ThisApplication.ActiveDocument.SelectSet.Item(1)

    ' Set a reference to the transient geometry object.
    Dim oTransGeom As TransientGeometry
    Set oTransGeom = ThisApplication.TransientGeometry

    ' Display type specific information.
    Select Case oSketchEnt.Type
        Case kSketchArcObject
            Dim oArc As SketchArc
            Set oArc = oSketchEnt
            Debug.Print "Sketch Arc selected."
            Debug.Print "  Center Point: " & oArc.CenterSketchPoint.Geometry.X & _
                            ", " & oArc.CenterSketchPoint.Geometry.Y
            Debug.Print "  Start Point: " & oArc.StartSketchPoint.Geometry.X & _
                            ", " & oArc.StartSketchPoint.Geometry.Y
            Debug.Print "  End Point: " & oArc.EndSketchPoint.Geometry.X & _
                            ", " & oArc.EndSketchPoint.Geometry.Y
            Debug.Print "  Start Angle: " & oArc.StartAngle
            Debug.Print "  Sweep Angle: " & oArc.SweepAngle
            Debug.Print "  Radius: " & oArc.Radius
            Debug.Print "  Length: " & oArc.Length
        Case kSketchCircleObject
            Dim oCircle As SketchCircle
            Set oCircle = oSketchEnt
            Debug.Print "Sketch Circle selected."
            Debug.Print "  Center Point: " & oCircle.CenterSketchPoint.Geometry.X & _
                            ", " & oCircle.CenterSketchPoint.Geometry.Y
            Debug.Print "  Radius: " & oCircle.Radius
            Debug.Print "  Area: " & oCircle.Area

            ' Change the radius
            oCircle.Radius = oCircle.Radius * 1.5
        Case kSketchEllipseObject
            Dim oEllipse As SketchEllipse
            Set oEllipse = oSketchEnt
            Debug.Print "Sketch Ellipse selected."
            Debug.Print "  Center Point: " & oEllipse.CenterSketchPoint.Geometry.X & _
                            ", " & oEllipse.CenterSketchPoint.Geometry.Y
            Debug.Print "  Major Axis Vecotr: " & oEllipse.MajorAxisVector.X & _
                            ", " & oEllipse.MajorAxisVector.Y
            Debug.Print "  Major Radius: " & oEllipse.MajorRadius
            Debug.Print "  Minor Radius: " & oEllipse.MinorRadius
            Debug.Print "  Area: " & oEllipse.Area

            ' Modify the ellipse
            oEllipse.MajorAxisVector = oTransGeom.CreateUnitVector2d(1, 1)
            oEllipse.MajorRadius = oEllipse.MajorRadius / 2
            oEllipse.MinorRadius = oEllipse.MinorRadius * 2
        Case kSketchEllipticalArcObject
            Dim oEllipticalArc As SketchEllipticalArc
            Set oEllipticalArc = oSketchEnt
            Debug.Print "Sketch Elliptical Arc selected."
            Debug.Print "  Center Point: " & oEllipticalArc.CenterSketchPoint.Geometry.X & _
                            ", " & oEllipticalArc.CenterSketchPoint.Geometry.Y
            Debug.Print "  Major Axis Vector: " & oEllipticalArc.MajorAxisVector.X & _
                            ", " & oEllipticalArc.MajorAxisVector.Y
            Debug.Print "  Major Radius: " & oEllipticalArc.MajorRadius
            Debug.Print "  Minor Radius: " & oEllipticalArc.MinorRadius
            Debug.Print "  Start Angle: " & oEllipticalArc.StartAngle
            Debug.Print "  Sweep Angle: " & oEllipticalArc.SweepAngle
            Debug.Print "  Length: " & oEllipticalArc.Length

            ' Modify the elliptical arc.
            oEllipticalArc.MajorAxisVector = oTransGeom.CreateUnitVector2d(1, 1)
            oEllipticalArc.MajorRadius = oEllipticalArc.MajorRadius / 2
            oEllipticalArc.MinorRadius = oEllipticalArc.MinorRadius * 2
        Case kSketchLineObject
            Dim oLine As SketchLine
            Set oLine = oSketchEnt
            Debug.Print "Sketch Line selected."
            Debug.Print "  Start Point: " & oLine.StartSketchPoint.Geometry.X & _
                            ", " & oLine.StartSketchPoint.Geometry.Y
            Debug.Print "  End Point: " & oLine.EndSketchPoint.Geometry.X & _
                            ", " & oLine.EndSketchPoint.Geometry.Y
            Debug.Print "  Length: " & oLine.Length
            Debug.Print "  Centerline: " & oLine.Centerline

            ' Toggle the centerline property.
            If oLine.Centerline Then
                oLine.Centerline = False
            Else
                oLine.Centerline = True
            End If
        Case kSketchPointObject
            Dim oPoint As SketchPoint
            Set oPoint = oSketchEnt
            Debug.Print "Sketch Point selected."
            Debug.Print "  Position: " & oPoint.Geometry.X & _
                            ", " & oPoint.Geometry.Y
            Debug.Print "  Hole Center: " & oPoint.HoleCenter

            ' Toggle the hole center property.
            If oPoint.HoleCenter Then
                oPoint.HoleCenter = False
            Else
                oPoint.HoleCenter = True
            End If
        Case kSketchSplineObject
            Dim oSpline As SketchSpline
            Set oSpline = oSketchEnt
            Debug.Print "Sketch Spline selected."
            Debug.Print "  Length: " & oSpline.Length
            Debug.Print "  Closed: " & oSpline.Closed
            Debug.Print "  Fit Points (" & oSpline.FitPointCount & ")"
            Dim i As Long
            For i = 1 To oSpline.FitPointCount
                Debug.Print "    Fit Point " & i & ": " & oSpline.FitPoint(i).Geometry.X & _
                            ", " & oSpline.FitPoint(i).Geometry.Y
            Next
    End Select

    ' Call the generic sketch entity methods.
    Debug.Print "  Constraint count: " & oSketchEnt.Constraints.Count
    Debug.Print "  Construction: " & oSketchEnt.Construction
    Debug.Print "  Range: (" & oSketchEnt.RangeBox.MinPoint.X & ", " & _
                            oSketchEnt.RangeBox.MinPoint.Y & ") - (" & _
                            oSketchEnt.RangeBox.MaxPoint.X & ", " & _
                            oSketchEnt.RangeBox.MaxPoint.Y & ")"
    Debug.Print "  Reference: " & oSketchEnt.Reference
    If oSketchEnt.Reference Then
        Debug.Print "  Referenced Entity: " & TypeName(oSketchEnt.ReferencedEntity)
    End If
End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
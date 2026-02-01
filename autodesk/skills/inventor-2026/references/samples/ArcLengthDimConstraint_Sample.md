# Creates an Arc Length Dimension Constraint

## Description

Demonstrates creating an arc length dimension constraint.

## Code Samples

* [VBA](#VBA)

To use this sample a part must be active.

```
Public Sub ArcLengthDimConstraintSample()
    ' Get the active part document.
    Dim partDoc As PartDocument
    Set partDoc = ThisApplication.ActiveDocument
    Dim partDef As PartComponentDefinition
    Set partDef = partDoc.ComponentDefinition

    ' Create a new sketch.
    Dim sketch As PlanarSketch
    Set sketch = partDef.Sketches.Add(partDef.WorkPlanes.Item(3))

    Dim tg As TransientGeometry
    Set tg = ThisApplication.TransientGeometry

    Dim dPi As Double
    dPi = Atn(1) * 4

    ' Create an arc.
    Dim arc As SketchArc
    Set arc = sketch.SketchArcs.AddByCenterStartSweepAngle(tg.CreatePoint2d(0, 0), 5, dPi / 8, dPi / 4)

    Dim arcConstraint As ArcLengthDimConstraint
    Set arcConstraint = sketch.DimensionConstraints.AddArcLength(arc, tg.CreatePoint2d(10, 9))
End Sub
```

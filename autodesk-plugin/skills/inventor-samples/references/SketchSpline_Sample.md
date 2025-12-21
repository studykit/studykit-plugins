# Sketch Spline

## Description

This sample demonstrates creating and manipulating a sketch spline.

## Code Samples

* [VBA](#VBA)

To use this sample a sketch must be active.

```
Public Sub DrawSketchSpline()
    ' Check to make sure a sketch is open.
    If Not TypeOf ThisApplication.ActiveEditObject Is PlanarSketch Then
        MsgBox "A sketch must be active."
        Exit Sub
    End If

    ' Set a reference to the active sketch.
    Dim oSketch As PlanarSketch
    Set oSketch = ThisApplication.ActiveEditObject

    ' Set a reference to the transient geometry collection.
    Dim oTransGeom As TransientGeometry
    Set oTransGeom = ThisApplication.TransientGeometry

    ' Create the collection that will contain the fit points for the spline.
    Dim oFitPoints As ObjectCollection
    Set oFitPoints = ThisApplication.TransientObjects.CreateObjectCollection

    ' Define the points to fit the spline through.  In this example, transient
    ' points are used.  They could also be sketch points and then the spline
    ' will automatically be constrained to fit through the sketch point.  The
    ' points are at (0,0), (2,2), (4,0), (6,4), (7,-1).
    Dim oPoints(1 To 5) As Point2d
    Set oPoints(1) = oTransGeom.CreatePoint2d(0, 0)
    oFitPoints.Add oPoints(1)

    Set oPoints(2) = oTransGeom.CreatePoint2d(2, 2)
    oFitPoints.Add oPoints(2)

    Set oPoints(3) = oTransGeom.CreatePoint2d(4, 0)
    oFitPoints.Add oPoints(3)

    Set oPoints(4) = oTransGeom.CreatePoint2d(6, 4)
    oFitPoints.Add oPoints(4)

    Set oPoints(5) = oTransGeom.CreatePoint2d(7, -1)
    oFitPoints.Add oPoints(5)

    ' Create the spline.
    Dim oSpline As SketchSpline
    Set oSpline = oSketch.SketchSplines.Add(oFitPoints)

    ' Change the curve to be closed.
    oSpline.Closed = True

    ' Add a ground constraint to the third fit point.
    Call oSketch.GeometricConstraints.AddGround(oSpline.FitPoint(3))

    ' Add an additional fit point.
    Dim oNewPoint As Point2d
    Set oNewPoint = oTransGeom.CreatePoint2d(8, 8)
    Call oSpline.InsertFitPoint(oNewPoint, 5, True)

    ' Reposition the second fit point.
    Call oSpline.FitPoint(2).MoveTo(oTransGeom.CreatePoint2d(2, 3))

    ' Delete a fit point by deleting the underlying sketch point.
    oSpline.FitPoint(2).Delete
End Sub
```

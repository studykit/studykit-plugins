# 3D Curve from Parametric Curve

## Description

Demonstrates the conversion of a 2d parameteric space curve into the equivalent 3d model space curve. To use this sample you must have a part open. You can select any face and 3D curves will be drawn on the face using client graphics.

## Code Samples

* [VBA](#VBA)

To use this sample a part must be active.

|  |
| --- |
| Copy Code |

```
Public Sub ParamCurveto3D()
    ' Have the user select a face whose parametric space will be used.
    Dim testFace As Face
    Set testFace = ThisApplication.CommandManager.Pick(kPartFaceFilter, "Select a face")

    ' Get the surface evaluator from the face.
    Dim surfEval As SurfaceEvaluator
    Set surfEval = testFace.Evaluator

    ' Get the parametric range of the face.
    Dim paramRange As Box2d
    Set paramRange = surfEval.ParamRangeRect

    ' Get the transient geometry object.
    Dim tg As TransientGeometry
    Set tg = ThisApplication.TransientGeometry

    ' Get the active document.  This assumes a part is active.
    Dim partDoc As PartDocument
    Set partDoc = ThisApplication.ActiveDocument

    ' Create a client graphics object.  If one already exists, give the user
    ' the option of re-using it, or creating a new one.
    Dim graphics As ClientGraphics
    On Error Resume Next
    Set graphics = partDoc.ComponentDefinition.ClientGraphicsCollection.Item("Test")
    If Err Then
        Set graphics = partDoc.ComponentDefinition.ClientGraphicsCollection.Add("Test")
    Else
        If MsgBox("Yes to add to existing graphics. No to start over.", vbYesNo + vbQuestion) = vbNo Then
            graphics.Delete

            Set graphics = partDoc.ComponentDefinition.ClientGraphicsCollection.Add("Test")
        End If
    End If

    ' Create a new graphics node.
    Dim node As GraphicsNode
    Set node = graphics.AddNode(1)

    ' Do a loop that creates 5 lines that go from the minimum range point to
    ' five points along the maximum u parameter.
    Dim startPnt As Point2d
    Set startPnt = paramRange.MinPoint
    Dim endPnt As Point2d
    Dim i As Integer
    For i = 1 To 5
        ' Create the 2d line in parametric space.
        Set endPnt = tg.CreatePoint2d(paramRange.MaxPoint.X, (((paramRange.MaxPoint.y - paramRange.MinPoint.y) / 4) * (i - 1)) + paramRange.MinPoint.y)
        Dim surfCurve As LineSegment2d
        Set surfCurve = tg.CreateLineSegment2d(startPnt, endPnt)

        ' Get the equivalent 3d curve in model space.
        Dim resultCurve As Object
        Set resultCurve = surfEval.Get3dCurveFrom2dCurve(surfCurve)

        ' Create client graphics for this curve.
        Dim crvGraphics As CurveGraphics
        Set crvGraphics = node.AddCurveGraphics(resultCurve)
        crvGraphics.DepthPriority = 2
    Next

    ' Create a 2d circle in parametric space.
    Dim center As Point2d
    Set center = tg.CreatePoint2d((paramRange.MaxPoint.X + paramRange.MinPoint.X) / 2, (paramRange.MaxPoint.y + paramRange.MinPoint.y) / 2)
    Dim radius As Double
    radius = (paramRange.MaxPoint.X - paramRange.MinPoint.X) * 0.25
    Dim paramCircle As Circle2d
    Set paramCircle = tg.CreateCircle2d(center, radius)

    ' Get the equivalent 3d curve in model space.
    Set resultCurve = surfEval.Get3dCurveFrom2dCurve(paramCircle)

    ' Create client graphics for this curve.
    Set crvGraphics = node.AddCurveGraphics(resultCurve)
    crvGraphics.DepthPriority = 2

    ThisApplication.ActiveView.Update
    ThisApplication.ActiveView.Fit
End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
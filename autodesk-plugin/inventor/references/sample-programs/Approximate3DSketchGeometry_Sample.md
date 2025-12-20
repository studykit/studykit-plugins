# Create Approximate Polyline to 3D Curve

## Description

Draws a polyline that is an approximation of the selected curve. To use this have a part open that contains a 3D skech that contains curves.

## Code Samples

* [VBA](#VBA)

To use this sample a part must be active.

|  |
| --- |
| Copy Code |

```
Public Sub Approximate3DSketchGeometry()
    Dim partDoc As PartDocument
    Set partDoc = ThisApplication.ActiveDocument

    ' Have the user select a sketch entity.
    Dim selectObj As SketchEntity3D
    Set selectObj = ThisApplication.CommandManager.Pick(kSketch3DCurveFilter, "Select 3D sketch entity")
    If selectObj Is Nothing Then
        On Error Resume Next
        Call partDoc.ComponentDefinition.ClientGraphicsCollection.Item("Test").Delete
        Call partDoc.GraphicsDataSetsCollection.Item("Test").Delete
        ThisApplication.ActiveView.Update
        Exit Sub
    End If

    ' Get the tolerance to approximate with.
    Dim tolerance As Double
    tolerance = Val(InputBox("Enter the chord height tolerance:", "Tolerance", "0.25"))

    ' Get the evaluator from the curve.
    Dim eval As CurveEvaluator
    Set eval = selectObj.Geometry.Evaluator

    ' Get the parameter extents.
    Dim startParam As Double
    Dim endParam As Double
    Call eval.GetParamExtents(startParam, endParam)

    Dim vertexCount As Long
    Dim vertexCoords() As Double
    Call eval.GetStrokes(startParam, endParam, tolerance, vertexCount, vertexCoords)

    ' Create a client graphics object.  If one already exists, give the user
    ' the option of re-using it, or creating a new one.
    Dim graphics As ClientGraphics
    Dim graphicsData As GraphicsDataSets
    On Error Resume Next
    Set graphics = partDoc.ComponentDefinition.ClientGraphicsCollection.Item("Test")
    On Error GoTo 0
    If graphics Is Nothing Then
        Set graphics = partDoc.ComponentDefinition.ClientGraphicsCollection.Add("Test")
        Set graphicsData = partDoc.GraphicsDataSetsCollection.Add("Test")
    Else
        Dim answer As VbMsgBoxResult
        answer = MsgBox("Yes to add to existing graphics. No to create new graphics. Cancel to clean graphics and quit.", vbYesNoCancel + vbQuestion)
        If answer = vbNo Then
            On Error Resume Next
            graphics.Delete
            partDoc.GraphicsDataSetsCollection.Item("Test").Delete
            On Error GoTo 0

            Set graphics = partDoc.ComponentDefinition.ClientGraphicsCollection.Add("Test")
            Set graphicsData = partDoc.GraphicsDataSetsCollection.Add("Test")
        ElseIf answer = vbYes Then
            Set graphicsData = partDoc.GraphicsDataSetsCollection.Item("Test")
        ElseIf answer = vbCancel Then
            If Not graphics Is Nothing Then
                graphics.Delete
                partDoc.GraphicsDataSetsCollection.Item("Test").Delete
                ThisApplication.ActiveView.Update
                Exit Sub
            End If
        End If
    End If

    Dim coordSet As GraphicsCoordinateSet
    Set coordSet = graphicsData.CreateCoordinateSet(1)
    Call coordSet.PutCoordinates(vertexCoords)

    ' Create a graphics node.
    Dim node As GraphicsNode
    Set node = graphics.AddNode(1)

    ' Create a line strip using the calculated coordinates.
    Dim lineStrip As LineStripGraphics
    Set lineStrip = node.AddLineStripGraphics
    lineStrip.CoordinateSet = coordSet

    ThisApplication.ActiveView.Update
End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
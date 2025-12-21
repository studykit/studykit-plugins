# OnDrag Event - dragging a WorkPoint

## Description

This sample demonstrates the use of the OnDrag event to drag fixed work points when no command is active. This sample only allows drags parallel to the X-Y plane. This sample is dependent on events and VB only supports events within a class module.

## Code Samples

* [VBA](#VBA)

To use the sample copy the WorkPointDrag sub into a code module. Create a new class module called clsDragWorkPoint and copy all of the rest of the code into it. Have a part document open that contains at least one fixed work point. Run the sample and drag the fixed work point.

```
Option Explicit
Public oDragWorkPoint As clsDragWorkPoint

Sub WorkPointDrag()

    Set oDragWorkPoint = New clsDragWorkPoint
    oDragWorkPoint.Initialize

End Sub

'*************************************************************
' The declarations and functions below need to be copied into
' a class module whose name is "clsDragWorkPoint".  The name
' can be changed but you'll need to change the declaration in
' the calling function "WorkPointDrag" to use the new name.
Option Explicit
Private WithEvents oUserInputEvents As UserInputEvents
Private oIE As InteractionEvents
Private WithEvents oMouseEvents As MouseEvents
Private oIntGraphics As InteractionGraphics
Private oWP As WorkPoint

Public Sub Initialize()
    Set oUserInputEvents = ThisApplication.CommandManager.UserInputEvents
End Sub

Private Sub oUserInputEvents_OnDrag(ByVal DragState As Inventor.DragStateEnum, ByVal ShiftKeys As Inventor.ShiftStateEnum, ByVal ModelPosition As Inventor.Point, ByVal ViewPosition As Inventor.Point2d, ByVal View As Inventor.View, ByVal AdditionalInfo As Inventor.NameValueMap, HandlingCode As Inventor.HandlingCodeEnum)

    Dim oSS As SelectSet
    Set oSS = ThisApplication.ActiveDocument.SelectSet

    If DragState = kDragStateDragHandlerSelection Then

        If oSS.Count = 1 And oSS.Item(1).Type = kWorkPointObject Then

            Set oWP = oSS.Item(1)

            If oWP.DefinitionType = kFixedWorkPoint Then
                HandlingCode = kEventCanceled
                Set oIE = ThisApplication.CommandManager.CreateInteractionEvents
                Set oMouseEvents = oIE.MouseEvents
                oMouseEvents.MouseMoveEnabled = True

                Set oIntGraphics = oIE.InteractionGraphics
                Call oIE.SetCursor(kCursorBuiltInCommonSketchDrag)
                oIE.Start
            End If
        End If
    End If
End Sub

Private Sub oMouseEvents_OnMouseMove(ByVal Button As MouseButtonEnum, ByVal ShiftKeys As ShiftStateEnum, ByVal ModelPosition As Point, ByVal ViewPosition As Point2d, ByVal View As View)
    Dim oSS As SelectSet
    Set oSS = ThisApplication.ActiveDocument.SelectSet

    If oSS.Count = 1 And oSS.Item(1).Type = kWorkPointObject Then

        Dim oWPDef As FixedWorkPointDef
        Set oWPDef = oWP.Definition

        Dim oProjectedPoint As Inventor.Point
        Call ProjectPoint(ModelPosition, oWPDef.Point, oProjectedPoint)

        ' Set a reference to the transient geometry object for user later.
        Dim oTransGeom As TransientGeometry
        Set oTransGeom = ThisApplication.TransientGeometry

        ' Create a graphics data set object.  This object contains all of the
        ' information used to define the graphics.
        Dim oDataSets As GraphicsDataSets
        Set oDataSets = oIntGraphics.GraphicsDataSets

        If oDataSets.Count <> 0 Then
            oDataSets.Item(1).Delete
        End If

        ' Create a coordinate set.
        Dim oCoordSet As GraphicsCoordinateSet
        Set oCoordSet = oDataSets.CreateCoordinateSet(1)

        ' Create an array that contains coordinates that define a set
        ' of outwardly spiraling points.
        Dim oPointCoords(1 To 3) As Double
        ' Define the X, Y, and Z components of the point.
        oPointCoords(1) = oProjectedPoint.X
        oPointCoords(2) = oProjectedPoint.Y
        oPointCoords(3) = oProjectedPoint.Z

        ' Assign the points into the coordinate set.
        Call oCoordSet.PutCoordinates(oPointCoords)

        ' Create the ClientGraphics object.
        Dim oClientGraphics As ClientGraphics
        Set oClientGraphics = oIntGraphics.PreviewClientGraphics

        If oClientGraphics.Count <> 0 Then
            oClientGraphics.Item(1).Delete
        End If

        ' Create a new graphics node within the client graphics objects.
        Dim oPtNode As GraphicsNode
        Set oPtNode = oClientGraphics.AddNode(1)

        ' Create a PointGraphics object within the node.
        Dim oPtGraphics As PointGraphics
        Set oPtGraphics = oPtNode.AddPointGraphics

        ' Assign the coordinate set to the line graphics.
        oPtGraphics.CoordinateSet = oCoordSet
        oPtGraphics.PointRenderStyle = kCrossPointStyle
        ThisApplication.ActiveView.Update
    End If
End Sub

Private Sub oMouseEvents_OnMouseUp(ByVal Button As MouseButtonEnum, ByVal ShiftKeys As ShiftStateEnum, ByVal ModelPosition As Point, ByVal ViewPosition As Point2d, ByVal View As View)

    Dim oSS As SelectSet
    Set oSS = ThisApplication.ActiveDocument.SelectSet

    If oSS.Count = 1 And oSS.Item(1).Type = kWorkPointObject Then

            Dim oWPDef As FixedWorkPointDef
            Set oWPDef = oWP.Definition

            Dim oProjectedPoint As Inventor.Point
            Call ProjectPoint(ModelPosition, oWPDef.Point, oProjectedPoint)

            ' Reposition the fixed work point
            oWPDef.Point = oProjectedPoint
            ThisApplication.ActiveDocument.Update
            oIE.Stop

            Set oWP = Nothing

    End If
End Sub

' Project the ModelPosition to a plane parallel to the
' X-Y plane on which the work point currently is.
Private Sub ProjectPoint(ByVal ModelPosition As Inventor.Point, ByVal WorkPointPosition As Inventor.Point, ProjectedPoint As Inventor.Point)

    ' Set a reference to the camera object
    Dim oCamera As Inventor.Camera
    Set oCamera = ThisApplication.ActiveView.Camera

    Dim oVec As Vector
    Set oVec = oCamera.Eye.VectorTo(oCamera.Target)

    Dim oLine As Line
    Set oLine = ThisApplication.TransientGeometry.CreateLine(ModelPosition, oVec)

    ' Create the z-axis vector
    Dim oZAxis As Vector
    Set oZAxis = ThisApplication.TransientGeometry.CreateVector(0, 0, 1)

    ' Create a plane parallel to the X-Y plane
    Dim oWPPlane As Plane
    Set oWPPlane = ThisApplication.TransientGeometry.CreatePlane(WorkPointPosition, oZAxis)

    Set ProjectedPoint = oWPPlane.IntersectWithLine(oLine)
End Sub
```

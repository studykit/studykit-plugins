# Basic Selection Using Interaction Events

## Description

This sample demonstrates using the selection events to select a face. Selection is dependent on events and VB only supports events within a class module.

## Code Samples

* [VBA](#VBA)

To use the sample copy the TestSelection sub into a code module. Create a new class module called clsSelect and copy all of the rest of the code into it. To run the sample, have a part document open that contains some geometry and run the TestSelection sub. Select a face and it will display its area.

|  |
| --- |
| Copy Code |

```
Public Sub TestSelection()
    ' Create a new clsSelect object.
    Dim oSelect As New clsSelect

    ' Call the pick method of the clsSelect object and set
    ' the filter to pick any face.
    Dim oFace As Face
    Set oFace = oSelect.Pick(kPartFaceFilter)

    ' Check to make sure an object was selected.
    If Not oFace Is Nothing Then
        ' Display the area of the selected face.
        MsgBox "Face area: " & oFace.Evaluator.Area & " cm^2"
    End If
End Sub

'*************************************************************
' The declarations and functions below need to be copied into
' a class module whose name is "clsSelect". The name can be
' changed but you'll need to change the declaration in the
' calling function "TestSelection" to use the new name.

' Declare the event objects
Private WithEvents oInteractEvents As InteractionEvents
Private WithEvents oSelectEvents As SelectEvents

' Declare a flag that's used to determine when selection stops.
Private bStillSelecting As Boolean

Public Function Pick(filter As SelectionFilterEnum) As Object
    ' Initialize flag.
    bStillSelecting = True

    ' Create an InteractionEvents object.
    Set oInteractEvents = ThisApplication.CommandManager.CreateInteractionEvents

    ' Ensure interaction is enabled.
    oInteractEvents.InteractionDisabled = False

    ' Set a reference to the select events.
    Set oSelectEvents = oInteractEvents.SelectEvents

    ' Set the filter using the value passed in.
    oSelectEvents.AddSelectionFilter filter

    ' Start the InteractionEvents object.
    oInteractEvents.Start

    ' Loop until a selection is made.
    Do While bStillSelecting
        ThisApplication.UserInterfaceManager.DoEvents
    Loop

    ' Get the selected item. If more than one thing was selected,
    ' just get the first item and ignore the rest.
    Dim oSelectedEnts As ObjectsEnumerator
    Set oSelectedEnts = oSelectEvents.SelectedEntities
    If oSelectedEnts.Count > 0 Then
        Set Pick = oSelectedEnts.Item(1)
    Else
        Set Pick = Nothing
    End If

    ' Stop the InteractionEvents object.
    oInteractEvents.Stop

    ' Clean up.
    Set oSelectEvents = Nothing
    Set oInteractEvents = Nothing
End Function

Private Sub oInteractEvents_OnTerminate()
    ' Set the flag to indicate we're done.
    bStillSelecting = False
End Sub

Private Sub oSelectEvents_OnSelect(ByVal JustSelectedEntities As ObjectsEnumerator, ByVal SelectionDevice As SelectionDeviceEnum, ByVal ModelPosition As Point, ByVal ViewPosition As Point2d, ByVal View As View)
    ' Set the flag to indicate we're done.
    bStillSelecting = False
End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
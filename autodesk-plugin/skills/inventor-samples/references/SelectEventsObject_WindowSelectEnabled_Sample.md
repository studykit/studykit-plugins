# Window Selection

## Description

This sample demonstrates using the selection events to window-select multiple edges. Selection is dependent on events and VB only supports events within a class module.

## Code Samples

* [VBA](#VBA)

To use the sample copy the TestWindowSelection sub into a code module. Create a new class module called clsSelect and copy all of the rest of the code into it. To run the sample, have a part document open that contains some geometry and run the TestWindowSelection sub.

```
Private oSelect As clsSelect

Public Sub TestWindowSelection()
    ' Create a new clsSelect object.
    Set oSelect = New clsSelect

    ' Call the WindowSelect method of the clsSelect object
    oSelect.WindowSelect
End Sub

'*************************************************************
' The declarations and functions below need to be copied into
' a class module whose name is "clsSelect". The name can be
' changed but you'll need to change the declaration in the
' calling function "TestWindowSelection" to use the new name.

' Declare the event objects
Private WithEvents oInteractEvents As InteractionEvents
Private WithEvents oSelectEvents As SelectEvents

' Declare a flag that's used to determine if command prompts are shown as tooltips.
Private bTooltipEnabled As Boolean

Public Function WindowSelect()
    ' Create an InteractionEvents object.
    Set oInteractEvents = ThisApplication.CommandManager.CreateInteractionEvents

    ' Ensure interaction is enabled.
    oInteractEvents.InteractionDisabled = False

    ' Set a reference to the select events.
    Set oSelectEvents = oInteractEvents.SelectEvents

    ' Set the filter for circular edges (this includes circular arcs).
    oSelectEvents.AddSelectionFilter kPartEdgeCircularFilter

    oSelectEvents.WindowSelectEnabled = True

    bTooltipEnabled = ThisApplication.GeneralOptions.ShowCommandPromptTooltips
    ThisApplication.GeneralOptions.ShowCommandPromptTooltips = True

    oInteractEvents.StatusBarText = "Window select. Esc to exit."

    ' Start the InteractionEvents object.
    oInteractEvents.Start
End Function

Private Sub oInteractEvents_OnTerminate()
    ' Reset to original value
    ThisApplication.GeneralOptions.ShowCommandPromptTooltips = bTooltipEnabled

    ' Clean up.
    Set oSelectEvents = Nothing
    Set oInteractEvents = Nothing
End Sub

Private Sub oSelectEvents_OnPreSelect(PreSelectEntity As Object, DoHighlight As Boolean, MorePreSelectEntities As ObjectCollection, ByVal SelectionDevice As SelectionDeviceEnum, ByVal ModelPosition As Point, ByVal ViewPosition As Point2d, ByVal View As View)
    ' Set a reference to the selected edge.
    ' Only circular edges can come through since the circular edge filter was set.
    Dim oEdge As Edge
    Set oEdge = PreSelectEntity

    ' Allow only fully circular edges to be picked.
    If Not oEdge.GeometryType = kCircleCurve Then
      DoHighlight = False
    End If
End Sub

Private Sub oSelectEvents_OnSelect(ByVal JustSelectedEntities As ObjectsEnumerator, ByVal SelectionDevice As SelectionDeviceEnum, ByVal ModelPosition As Point, ByVal ViewPosition As Point2d, ByVal View As View)
    MsgBox "Picked " & JustSelectedEntities.Count & " circular edges."
End Sub
```

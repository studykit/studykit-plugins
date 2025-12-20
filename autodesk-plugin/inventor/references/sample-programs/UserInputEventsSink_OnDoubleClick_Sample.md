# Cancel a double click

## Description

Demonstrates how to receive (and in this case, cancel) a double click from a user.

## Code Samples

* [VBA](#VBA)

|  |
| --- |
| Copy Code |

```
Option Explicit
   Private WithEvents oUIEvents As UserInputEvents

   Private Sub Class_Initialize()
       Set oUIEvents = ThisApplication.CommandManager.UserInputEvents
   End Sub

Private Sub oUIEvents_OnDoubleClick(ByVal SelectedEntities As ObjectsEnumerator, ByVal SelectionDevice As SelectionDeviceEnum, ByVal Button As MouseButtonEnum, ByVal ShiftKeys As ShiftStateEnum, ByVal ModelPosition As Point, ByVal ViewPosition As Point2d, ByVal View As View, ByVal AdditionalInfo As NameValueMap, HandlingCode As HandlingCodeEnum)
       Debug.Print "OnDoubleClick: "; SelectedEntities.Count; SelectionDevice; ShiftKeys; View.Caption
       If SelectionDevice = kBrowserSelection Then
           MsgBox "Hello there! I'm not letting you activate this"
           ThisApplication.CommandManager.ControlDefinitions("AppAboutInventorCmd").Execute2 (False)
           HandlingCode = kEventCanceled
       End If
   End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
# Dockable window

## Description

This sample demonstrates creating a dockable window and adding a dialog into it.

## Code Samples

* [VBA](#VBA)

You need to create the (modeless) dialog and set the hwnd of the dialog in the code below.

|  |
| --- |
| Copy Code |

```
Sub DockableWindow()
    Dim oUserInterfaceMgr As UserInterfaceManager
    Set oUserInterfaceMgr = ThisApplication.UserInterfaceManager

    ' Create a new dockable window
    Dim oWindow As DockableWindow
    Set oWindow = oUserInterfaceMgr.DockableWindows.Add("SampleClientId", "TestWindowInternalName", "Test Window")

    ' Get the hwnd of the dialog to be added as a child
    ' CHANGE THIS VALUE!
    Dim hwnd As Long
    hwnd = 4851096

    ' Add the dialog as a child to the dockable window
    Call oWindow.AddChild(hwnd)

    ' Don't allow docking to top and bottom
    oWindow.DisabledDockingStates = kDockTop + kDockBottom

    ' Make the window visible
    oWindow.Visible = True
End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
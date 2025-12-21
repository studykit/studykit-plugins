# Add commands to the application menu

## Description

Demonstrates adding command to the application menu.

## Code Samples

* [VBA](#VBA)

```
Sub AddCommandsToFileBrowser()
    ' Get the application menu controls collection
    Dim oFileBrowserControls As CommandControls
    Set oFileBrowserControls = ThisApplication.UserInterfaceManager.FileBrowserControls

    ' Get the "Zoom All" and "Home View" commands
    Dim oDef1 As ButtonDefinition
    Set oDef1 = ThisApplication.CommandManager.ControlDefinitions.Item("AppZoomAllCmd")

    Dim oDef2 As ButtonDefinition
    Set oDef2 = ThisApplication.CommandManager.ControlDefinitions.Item("AppIsometricViewCmd")

    ' Create button controls, positioned before the "Manage" control
    Call oFileBrowserControls.AddButton(oDef1, True, True, "Manage", True)
    Call oFileBrowserControls.AddButton(oDef2, True, True, "Manage", True)
    Call oFileBrowserControls.AddSeparator("Manage", True)
End Sub
```

# Create a ribbon panel in an existing tab

## Description

Demonstrates creating a new ribbon panel within an existing ribbon tab.

## Code Samples

* [VBA](#VBA)

```
Sub AddPanelToToolsTab()
    ' Get the ribbon associated with the part document
    Dim oPartRibbon As Ribbon
    Set oPartRibbon = ThisApplication.UserInterfaceManager.Ribbons.Item("Part")

    ' Get the "Tools" tab
    Dim oTab As RibbonTab
    Set oTab = oPartRibbon.RibbonTabs.Item("id_TabTools")

    ' Create a panel named "Update", positioned after the "Measure" panel in the Tools tab.
    Dim oPanel As RibbonPanel
    Set oPanel = oTab.RibbonPanels.Add("Update", "ToolsTabUpdatePanel", "SampleClientId", "id_PanelP_ToolsMeasure")

    ' Get the update commands
    Dim oDef1 As ButtonDefinition
    Set oDef1 = ThisApplication.CommandManager.ControlDefinitions.Item("AppLocalUpdateCmd")

    Dim oDef2 As ButtonDefinition
    Set oDef2 = ThisApplication.CommandManager.ControlDefinitions.Item("AppUpdateMassPropertiesCmd")

    Dim oDefs As ObjectCollection
    Set oDefs = ThisApplication.TransientObjects.CreateObjectCollection

    oDefs.Add oDef1
    oDefs.Add oDef2

    ' Create a split button control
    Call oPanel.CommandControls.AddSplitButton(oDef1, oDefs, True)

    ' Get the rebuild command
    Dim oDef3 As ButtonDefinition
    Set oDef3 = ThisApplication.CommandManager.ControlDefinitions.Item("AppRebuildAllWrapperCmd")

    ' Create a button control
    Call oPanel.CommandControls.AddButton(oDef3, True)
End Sub
```

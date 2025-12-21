# Creation of an override environment for a document

## Description

A new ribbon tab is created and associated with the override environment.

## Code Samples

* [VBA](#VBA)

Open a part document and run the sample.

|  |
| --- |
| Copy Code |

```
Sub AddOverrideEnvironment()
    ' Make sure a part document is active
    Dim oPartDoc As PartDocument
    Set oPartDoc = ThisApplication.ActiveDocument

    Dim oEnvironments As Environments
    Set oEnvironments = ThisApplication.UserInterfaceManager.Environments

    ' Create a new environment
    Dim oOverrideEnv As Environment
    Set oOverrideEnv = oEnvironments.Add("Override", "OverrideEnvironment")

    ' Get the part ribbon
    Dim oPartRibbon As Ribbon
    Set oPartRibbon = ThisApplication.UserInterfaceManager.Ribbons.Item("Part")

    ' Create a contextual tab to be used as the default for the override environment
    Dim oTabOne As RibbonTab
    Set oTabOne = oPartRibbon.RibbonTabs.Add("Tab One", "TabOne", "ClientId123", "id_TabSheetMetal", True, False)

    ' Create panels with the tab
    Dim oPanelOne As RibbonPanel
    Set oPanelOne = oTabOne.RibbonPanels.Add("Panel One", "PanelOne", "ClientId123")

    Dim oDef1 As ButtonDefinition
    Set oDef1 = ThisApplication.CommandManager.ControlDefinitions.Item("PartExtrudeCmd")

    Call oPanelOne.CommandControls.AddButton(oDef1, True)

    Dim oPanelTwo As RibbonPanel
    Set oPanelTwo = oTabOne.RibbonPanels.Add("Panel Two", "PanelTwo", "ClientId123")

    Dim oDef2 As ButtonDefinition
    Set oDef2 = ThisApplication.CommandManager.ControlDefinitions.Item("PartRevolveCmd")

    Call oPanelTwo.CommandControls.AddButton(oDef2, True)

    Dim strTabs(0) As String
    strTabs(0) = "TabOne"

    oOverrideEnv.InheritAllRibbonTabs = False
    oOverrideEnv.AdditionalVisibleRibbonTabs = strTabs
    oOverrideEnv.DefaultRibbonTab = "TabOne"

    ' Set the override environment on the active part
    oPartDoc.EnvironmentManager.OverrideEnvironment = oOverrideEnv

End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
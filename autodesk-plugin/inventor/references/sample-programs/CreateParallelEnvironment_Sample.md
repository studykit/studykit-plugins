# Add parallel environment with contextual tabs

## Description

The following sample demonstrates the use of parallel environments and contextual ribbon tabs.

## Code Samples

* [VBA](#VBA)
* [C#](#C#)

Run the following macro. Open an assembly document. Go the the "Environments" tab and click on the "Some Analysis" button.

|  |
| --- |
| Copy Code |

```
Sub AddParallelEnvironment()
    ' Get the Environments collection
    Dim oEnvironments As Environments
    Set oEnvironments = ThisApplication.UserInterfaceManager.Environments

    ' Create a new environment
    Dim oNewEnv As Environment
    Set oNewEnv = oEnvironments.Add("Some Analysis", "SomeAnalysis")

    ' Get the ribbon associated with the assembly environment
    Dim oAssemblyRibbon As Ribbon
    Set oAssemblyRibbon = ThisApplication.UserInterfaceManager.Ribbons.Item("Assembly")

    ' Create contextual tabs and panels within them
    Dim oContextualTabOne As RibbonTab
    Set oContextualTabOne = oAssemblyRibbon.RibbonTabs.Add("Some Analysis", "SomeAnalysis", "ClientId123", , , True)

    Dim oPanelOne As RibbonPanel
    Set oPanelOne = oContextualTabOne.RibbonPanels.Add("Panel One", "PanelOne", "ClientId123")

    Dim oDef1 As ButtonDefinition
    Set oDef1 = ThisApplication.CommandManager.ControlDefinitions.Item("PartExtrudeCmd")

    Call oPanelOne.CommandControls.AddButton(oDef1, True)

    Dim oPanelTwo As RibbonPanel
    Set oPanelTwo = oContextualTabOne.RibbonPanels.Add("Panel Two", "PanelTwo", "ClientId123")

    Dim oDef2 As ButtonDefinition
    Set oDef2 = ThisApplication.CommandManager.ControlDefinitions.Item("AssemblyPlaceComponentCmd")

    Call oPanelTwo.CommandControls.AddButton(oDef2, True)

    Dim oContextualTabTwo As RibbonTab
    Set oContextualTabTwo = oAssemblyRibbon.RibbonTabs.Add("Some Analysis Extras", "SomeAnalysisExtras", "ClientId123", , , True)

    Dim oPanelThree As RibbonPanel
    Set oPanelThree = oContextualTabTwo.RibbonPanels.Add("Panel Three", "PanelThree", "ClientId123")
    Call oPanelThree.CommandControls.AddButton(oDef1, True)

    ' Associate the contextual tabs with the newly created environment
    ' The contextual tabs will only be displayed when this environment is active
    Dim strTabs(1) As String
    strTabs(0) = "SomeAnalysis"
    strTabs(1) = "SomeAnalysisExtras"

    oNewEnv.AdditionalVisibleRibbonTabs = strTabs

    ' Make the "SomeAnalysis" tab default for the environment
    oNewEnv.DefaultRibbonTab = "SomeAnalysis"

    ' Get the collection of parallel environments and add the new environment
    Dim oParEnvs As EnvironmentList
    Set oParEnvs = ThisApplication.UserInterfaceManager.ParallelEnvironments

    Call oParEnvs.Add(oNewEnv)

    ' Make the new parallel environment available only within the assembly environment
    ' A ControlDefinition is automatically created when an environment is added to the
    ' parallel environments list. The internal name of the definition is the same as
    ' the internal name of the environment.
    Dim oParallelEnvButton As ControlDefinition
    Set oParallelEnvButton = ThisApplication.CommandManager.ControlDefinitions.Item("SomeAnalysis")

    Dim oEnv As Environment
    For Each oEnv In oEnvironments
        If Not oEnv.InternalName = "AMxAssemblyEnvironment" Then
            On Error Resume Next
            Call oEnv.DisabledCommandList.Add(oParallelEnvButton)
        End If
    Next
End Sub
```

Run the following macro. Open an assembly document. Go the the "Environments" tab and click on the "Some Analysis" button. The first line of this sample sets the oApp variable to ThisApplication - this should be appropriately changed.

|  |
| --- |
| Copy Code |

```
public void AddParallelEnvironment()
{
    Application oApp = ThisApplication;

    // Get the Environments collection
    Environments oEnvironments = oApp.UserInterfaceManager.Environments;

    // Create a new environment
    Inventor.Environment oNewEnv = oEnvironments.Add("Some Analysis", "SomeAnalysis", null, null, null);

    // Get the ribbon associated with the assembly environment
    Ribbon oAssemblyRibbon = oApp.UserInterfaceManager.Ribbons["Assembly"];

    // Create contextual tabs and panels within them
    RibbonTab oContextualTabOne = oAssemblyRibbon.RibbonTabs.Add("Some Analysis", "SomeAnalysis", "ClientId123","" ,false , true);

    RibbonPanel oPanelOne = oContextualTabOne.RibbonPanels.Add("Panel One", "PanelOne", "ClientId123","", false);
    ButtonDefinition oDef1 = (ButtonDefinition)oApp.CommandManager.ControlDefinitions["PartExtrudeCmd"];
    oPanelOne.CommandControls.AddButton(oDef1, true, true, "", false);

    RibbonPanel oPanelTwo = oContextualTabOne.RibbonPanels.Add("Panel Two", "PanelTwo", "ClientId123", "", false);
    ButtonDefinition oDef2 = (ButtonDefinition)oApp.CommandManager.ControlDefinitions["AssemblyPlaceComponentCmd"];
    oPanelTwo.CommandControls.AddButton(oDef2, true, true, "", false);

    RibbonTab oContextualTabTwo = oAssemblyRibbon.RibbonTabs.Add("Some Analysis Extras", "SomeAnalysisExtras", "ClientId123","" ,false , true);

    RibbonPanel oPanelThree = oContextualTabTwo.RibbonPanels.Add("Panel Three", "PanelThree", "ClientId123", "", false);
    oPanelThree.CommandControls.AddButton(oDef1, true, true, "", false);

    // Associate the contextual tabs with the newly created environment
    // The contextual tabs will only be displayed when this environment is active
    String[] strTabs = new String[2];
    strTabs[0] = "SomeAnalysis";
    strTabs[1] = "SomeAnalysisExtras";

    oNewEnv.AdditionalVisibleRibbonTabs = strTabs;

    // Make the "SomeAnalysis" tab default for the environment
    oNewEnv.DefaultRibbonTab = "SomeAnalysis";

    // Get the collection of parallel environments and add the new environment
    EnvironmentList oParEnvs = oApp.UserInterfaceManager.ParallelEnvironments;

    oParEnvs.Add(oNewEnv);

    // Make the new parallel environment available only within the assembly environment
    // A ControlDefinition is automatically created when an environment is added to the
    // parallel environments list. The internal name of the definition is the same as
    // the internal name of the environment.
    ControlDefinition oParallelEnvButton = oApp.CommandManager.ControlDefinitions["SomeAnalysis"];

    int iEnvCount = oEnvironments.Count;
    Inventor.Environment oEnv;
    int i;
    for (i = 1; i <= iEnvCount; i++)
    {
        oEnv = oEnvironments[i];
        if (oEnv.InternalName != "AMxAssemblyEnvironment")
        {
            oEnv.DisabledCommandList.Add(oParallelEnvButton);
        }
    }
}
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
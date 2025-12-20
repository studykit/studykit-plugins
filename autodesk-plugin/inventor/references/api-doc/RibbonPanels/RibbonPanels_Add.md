# RibbonPanels.Add Method

Parent Object: [RibbonPanels](../RibbonPanels/RibbonPanels.md)

## Description

Method that creates a new RibbonPanel within a ribbon tab. The newly created RibbonPanel is returned.

## Syntax

RibbonPanels.**Add**( ***DisplayName*** As String, ***InternalName*** As String, ***ClientId*** As String, [***TargetPanelInternalName***] As String, [***InsertBeforeTargetPanel***] As Boolean ) As [RibbonPanel](../RibbonPanel/RibbonPanel.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| DisplayName | String | Input string that defines the display name of the ribbon panel. This is the name that is displayed to the user and should be localized for different locales. |
| InternalName | String | Input string that defines the unique internal name of the ribbon panel. This is the internal name and is not displayed to the user. The name must be unique with respect to all other ribbon panels within the tab. The name should remain constant in all locales so it can be used to find a specific panel. |
| ClientId | String | Input String that uniquely identifies the client. This is the CLSID of the AddIn in a string form, e.g. "{C9A6C580\-3817\-11D0\-BE4E\-080036E87B02}". If supplied, this string is used at Inventor start up time to determine whether the AddIn that created this ribbon panel has since been uninstalled. If so, the panel is deleted.The string is also used to find all the panels to delete when the associated Add\-in is unloaded. A 'dummy' string or a null string can be specified, but is not recommended. |
| TargetPanelInternalName | String | Optional input String that specifies the internal name of an existing panel to position the new panel next to. If specified, the InsertBeforeTargetPanel argument indicates whether to place the new panel before or after the target panel. If not specified, the new panel is positioned at the end. |
| InsertBeforeTargetPanel | Boolean | Optional input Boolean that specifies whether to position the new panel before or after the target ribbon panel. The argument defaults to False and is not used if the TargetPanelInternalName argument is not specified.   This is an optional argument whose default value is False. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Add parallel environment with contextual tabs](../../sample-programs/CreateParallelEnvironment_Sample.md) | The following sample demonstrates the use of parallel environments and contextual ribbon tabs. |
| [Creation of an override environment for a document](../../sample-programs/EnvironmentManager_OverrideEnvironment_Sample.md) | A new ribbon tab is created and associated with the override environment. |
| [Create a ribbon panel in an existing tab](../../sample-programs/RibbonPanels_Add_Sample.md) | Demonstrates creating a new ribbon panel within an existing ribbon tab. |

## Version

Introduced in version 2010

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
# RibbonTabs.Add Method

Parent Object: [RibbonTabs](../RibbonTabs/RibbonTabs.md)

## Description

Method that creates a new RibbonTab within a ribbon. The newly created RibbonTab is returned.

## Syntax

RibbonTabs.**Add**( ***DisplayName*** As String, ***InternalName*** As String, ***ClientId*** As String, [***TargetTabInternalName***] As String, [***InsertBeforeTargetTab***] As Boolean, [***Contextual***] As Boolean ) As [RibbonTab](../RibbonTab/RibbonTab.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| DisplayName | String | Input string that defines the display name of the ribbon tab. This is the name that is displayed to the user and should be localized for different locales. |
| InternalName | String | Input string that defines the unique \internal name of the ribbon tab. This is the internal name and is not displayed to the user. The name must be unique with respect to all other ribbon tabs. The name should remain constant in all locales so it can be used to find a specific tab. |
| ClientId | String | Input String that uniquely identifies the client. This is the CLSID of the AddIn in a string form, e.g. "{C9A6C580\-3817\-11D0\-BE4E\-080036E87B02}". If supplied, this string is used at Inventor start up time to determine whether the AddIn that created this ribbon tab has since been uninstalled. If so, the tab is deleted.The string is also used to find all the tabs to delete when the associated Add\-in is unloaded. A 'dummy' string or a null string can be specified, but is not recommended. |
| TargetTabInternalName | String | Optional input String that specifies the internal name of an existing tab to position the new tab next to. If specified, the InsertBeforeTargetTab argument indicates whether to place the new tab before or after the specified tab. If not specified, the new tab is positioned at the end. |
| InsertBeforeTargetTab | Boolean | Optional input Boolean that specifies whether to position the new tab before or after the target ribbon tab. The argument defaults to False and is not used if the TargetTabInternalName argument is not specified.   This is an optional argument whose default value is False. |
| Contextual | Boolean | Optional input Boolean that specifies whether this is a contextual tab. Contextual tabs, such as the Sketch tab in the Sketch environment, come and go based on the current environment. They are displayed in a different color to indicate to the user that this is not a permanent tab. If not provided, this argument defaults to False. If a value of False is provided, the tab is added visibly. If a value of True is provided, the tab is added invisibly. Contextual tabs should then be added to the Environment.AdditionalVisibleRibbonTabs so that they show up visible in the appropriate environment(s).   This is an optional argument whose default value is False. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Add parallel environment with contextual tabs](../../sample-programs/CreateParallelEnvironment_Sample.md) | The following sample demonstrates the use of parallel environments and contextual ribbon tabs. |
| [Creation of an override environment for a document](../../sample-programs/EnvironmentManager_OverrideEnvironment_Sample.md) | A new ribbon tab is created and associated with the override environment. |

## Version

Introduced in version 2010

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
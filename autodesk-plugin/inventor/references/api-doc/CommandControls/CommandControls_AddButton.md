# CommandControls.AddButton Method

Parent Object: [CommandControls](../CommandControls/CommandControls.md)

## Description

Method that creates a new button CommandControl object. An example of this type of control is the 'Extrude' feature command button.

## Syntax

CommandControls.**AddButton**( ***ButtonDefinition*** As [ButtonDefinition](../ButtonDefinition/ButtonDefinition.md), [***UseLargeIcon***] As Boolean, [***ShowText***] As Boolean, [***TargetControlInternalName***] As String, [***InsertBeforeTargetControl***] As Boolean ) As [CommandControl](../CommandControl/CommandControl.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| ButtonDefinition | [ButtonDefinition](../ButtonDefinition/ButtonDefinition.md) | Input ButtonDefinition object that specifies the object to associate with this control. |
| UseLargeIcon | Boolean | Optional input Boolean that specifies whether to use large icon or small icon for the control. If not specified, the small icon is used by default. |
| ShowText | Boolean | Optional input Boolean that specifies whether to display text (display name) for the control. If not specified, text is displayed by default.   This is an optional argument whose default value is True. |
| TargetControlInternalName | String | Optional input String that specifies the internal name of an existing control to position the new control next to. If specified, the InsertBeforeTargetControl argument indicates whether to place the new control before or after the target control. If not specified, the new control is positioned at the end.   This is an optional argument whose default value is "". |
| InsertBeforeTargetControl | Boolean | Optional input Boolean that specifies whether to position the new control before or after the target control. The argument defaults to False and is not used if the TargetControlInternalName argument is not specified.   This is an optional argument whose default value is False. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Add commands to the application menu](../../sample-programs/AddButtonToAppMenu_Sample.md) | Demonstrates adding command to the application menu. |
| [Add parallel environment with contextual tabs](../../sample-programs/CreateParallelEnvironment_Sample.md) | The following sample demonstrates the use of parallel environments and contextual ribbon tabs. |
| [Creation of an override environment for a document](../../sample-programs/EnvironmentManager_OverrideEnvironment_Sample.md) | A new ribbon tab is created and associated with the override environment. |
| [Create a ribbon panel in an existing tab](../../sample-programs/RibbonPanels_Add_Sample.md) | Demonstrates creating a new ribbon panel within an existing ribbon tab. |

## Version

Introduced in version 2010

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
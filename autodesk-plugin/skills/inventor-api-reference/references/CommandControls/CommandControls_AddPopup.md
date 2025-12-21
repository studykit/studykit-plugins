# CommandControls.AddPopup Method

Parent Object: [CommandControls](../CommandControls/CommandControls.md)

## Description

Method that creates a new popup CommandControl object. An example of this type of control is the 'Switch' control available in the Windows panel of the View tab.

## Syntax

CommandControls.**AddPopup**( ***DisplayedControl*** As [ButtonDefinition](../ButtonDefinition/ButtonDefinition.md), ***ButtonDefinitions*** As [ObjectCollection](../ObjectCollection/ObjectCollection.md), [***UseLargeIcon***] As Boolean, [***ShowText***] As Boolean, [***TargetControlInternalName***] As String, [***InsertBeforeTargetControl***] As Boolean ) As [CommandControl](../CommandControl/CommandControl.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| DisplayedControl | [ButtonDefinition](../ButtonDefinition/ButtonDefinition.md) | Input ButtonDefinition object that specifies the displayed control for the control. This ButtonDefinition is only used to extract the icons and the display name for the control. |
| ButtonDefinitions | [ObjectCollection](../ObjectCollection/ObjectCollection.md) | Input ObjectCollection containing the ButtonDefinition objects hosted by this control. |
| UseLargeIcon | Boolean | Optional input Boolean that specifies whether to use large icon or small icon for the control. If not specified, the small icon is used by default. |
| ShowText | Boolean | Optional input Boolean that specifies whether to display text (display name) for the control. If not specified, text is displayed by default.   This is an optional argument whose default value is True. |
| TargetControlInternalName | String | Optional input String that specifies the internal name of an existing control to position the new control next to. If specified, the InsertBeforeTargetControl argument indicates whether to place the new control before or after the target control. If not specified, the new control is positioned at the end.   This is an optional argument whose default value is "". |
| InsertBeforeTargetControl | Boolean | Optional input Boolean that specifies whether to position the new control before or after the target control. The argument defaults to False and is not used if the TargetControlInternalName argument is not specified.   This is an optional argument whose default value is False. |

## Version

Introduced in version 2010

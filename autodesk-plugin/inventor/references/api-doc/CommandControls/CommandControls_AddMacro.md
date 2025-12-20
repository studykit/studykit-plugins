# CommandControls.AddMacro Method

Parent Object: [CommandControls](../CommandControls/CommandControls.md)

## Description

Method that creates a new macro CommandControl object.

## Syntax

CommandControls.**AddMacro**( ***MacroControlDefinition*** As [MacroControlDefinition](../MacroControlDefinition/MacroControlDefinition.md), [***UseLargeIcon***] As Boolean, [***ShowText***] As Boolean, [***TargetControlInternalName***] As String, [***InsertBeforeTargetControl***] As Boolean ) As [CommandControl](../CommandControl/CommandControl.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| MacroControlDefinition | [MacroControlDefinition](../MacroControlDefinition/MacroControlDefinition.md) | Input MacroControlDefinition object that specifies the object to associate with this control. |
| UseLargeIcon | Boolean | Optional input Boolean that specifies whether to use large icon or small icon for the control. If not specified, the small icon is used by default. |
| ShowText | Boolean | Optional input Boolean that specifies whether to display text (display name) for the control. If not specified, text is displayed by default.   This is an optional argument whose default value is True. |
| TargetControlInternalName | String | Optional input String that specifies the internal name of an existing control to position the new control next to. If specified, the InsertBeforeTargetControl argument indicates whether to place the new control before or after the target control. If not specified, the new control is positioned at the end.   This is an optional argument whose default value is "". |
| InsertBeforeTargetControl | Boolean | Optional input Boolean that specifies whether to position the new control before or after the target control. The argument defaults to False and is not used if the TargetControlInternalName argument is not specified.   This is an optional argument whose default value is False. |

## Version

Introduced in version 2010

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
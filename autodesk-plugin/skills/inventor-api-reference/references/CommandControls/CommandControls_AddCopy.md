# CommandControls.AddCopy Method

Parent Object: [CommandControls](../CommandControls/CommandControls.md)

## Description

Method that creates a copy of an existing CommandControl object as a child control of the current CommandControl. This can be used to copy controls between ribbon panels.

## Syntax

CommandControls.**AddCopy**( ***CommandControl*** As [CommandControl](../CommandControl/CommandControl.md), [***TargetControlInternalName***] As String, [***InsertBeforeTargetControl***] As Boolean ) As [CommandControl](../CommandControl/CommandControl.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| CommandControl | [CommandControl](../CommandControl/CommandControl.md) | CommandControl to copy |
| TargetControlInternalName | String | Optional input String that specifies the internal name of an existing control to position the new control next to. If specified, the InsertBeforeTargetControl argument indicates whether to place the new control before or after the target control. If not specified, the new control is positioned at the end. |
| InsertBeforeTargetControl | Boolean | Optional input Boolean that specifies whether to position the new control before or after the target control. The argument defaults to False and is not used if the TargetControlInternalName argument is not specified.   This is an optional argument whose default value is False. |

## Version

Introduced in version 2011

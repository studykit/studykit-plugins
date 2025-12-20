# CommandControls.AddComboBox Method

Parent Object: [CommandControls](../CommandControls/CommandControls.md)

## Description

Method that creates a new combo-box CommandControl object.

## Syntax

CommandControls.**AddComboBox**( ***ComboBoxDefinition*** As [ComboBoxDefinition](../ComboBoxDefinition/ComboBoxDefinition.md), [***TargetControlInternalName***] As String, [***InsertBeforeTargetControl***] As Boolean ) As [CommandControl](../CommandControl/CommandControl.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| ComboBoxDefinition | [ComboBoxDefinition](../ComboBoxDefinition/ComboBoxDefinition.md) | Input ComboBoxDefinition object that specifies the object to associate with this control. |
| TargetControlInternalName | String | Optional input String that specifies the internal name of an existing control to position the new control next to. If specified, the InsertBeforeTargetControl argument indicates whether to place the new control before or after the target control. If not specified, the new control is positioned at the end. |
| InsertBeforeTargetControl | Boolean | Optional input Boolean that specifies whether to position the new control before or after the target control. The argument defaults to False and is not used if the TargetControlInternalName argument is not specified.   This is an optional argument whose default value is False. |

## Version

Introduced in version 2010

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
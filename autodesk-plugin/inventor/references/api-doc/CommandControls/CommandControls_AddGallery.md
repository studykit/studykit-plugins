# CommandControls.AddGallery Method

Parent Object: [CommandControls](../CommandControls/CommandControls.md)

## Description

Method that creates a new gallery CommandControl object. An example of this type of control is the gallery control available in the Symbols panel of the Annotate tab in drawings.

## Syntax

CommandControls.**AddGallery**( ***ButtonDefinitions*** As [ObjectCollection](../ObjectCollection/ObjectCollection.md), [***DisplayAsComboBox***] As Boolean, [***Width***] As Long, [***TargetControlInternalName***] As String, [***InsertBeforeTargetControl***] As Boolean ) As [CommandControl](../CommandControl/CommandControl.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| ButtonDefinitions | [ObjectCollection](../ObjectCollection/ObjectCollection.md) | Input ObjectCollection containing the ButtonDefinition objects hosted by this control. The internal and display names of the first definition are used for the control. |
| DisplayAsComboBox | Boolean | Optional input Boolean that specifies whether to display the controls as a window (see Symbols panel in Annotate tab of drawings) or a combobox (see Insert panel of Manage tab in parts). If not specified, a default of False is assumed and the control is displayed as a window. |
| Width | Long | Optional input Long that specifies the width for the control. If not specified, a default value of 200 is used.   This is an optional argument whose default value is 200. |
| TargetControlInternalName | String | Optional input String that specifies the internal name of an existing control to position the new control next to. If specified, the InsertBeforeTargetControl argument indicates whether to place the new control before or after the target control. If not specified, the new control is positioned at the end.   This is an optional argument whose default value is "". |
| InsertBeforeTargetControl | Boolean | Optional input Boolean that specifies whether to position the new control before or after the target control. The argument defaults to False and is not used if the TargetControlInternalName argument is not specified.   This is an optional argument whose default value is False. |

## Version

Introduced in version 2010

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
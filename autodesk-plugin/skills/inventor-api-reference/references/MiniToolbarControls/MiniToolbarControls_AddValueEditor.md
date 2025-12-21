# MiniToolbarControls.AddValueEditor Method

Parent Object: [MiniToolbarControls](../MiniToolbarControls/MiniToolbarControls.md)

## Description

Method that creates a new value edit control within the MiniToolbar.

## Syntax

MiniToolbarControls.**AddValueEditor**( ***InternalName*** As String, ***ToolTipText*** As String, ***UnitsType*** As [ValueUnitsTypeEnum](../ValueUnitsTypeEnum.md), ***Expression*** As String, [***DisplayName***] As String, [***Width***] As Long, [***StandardIcon***] As Variant, [***LargeIcon***] As Variant ) As [MiniToolbarValueEditor](../MiniToolbarValueEditor/MiniToolbarValueEditor.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| InternalName | String | Input String that specifies an internal name for the control. |
| ToolTipText | String | Input String that specifies the tooltip text for the control. |
| UnitsType | [ValueUnitsTypeEnum](../ValueUnitsTypeEnum.md) | Input enum that specifies the units type for the value editor. |
| Expression | String | Input String that specifies the initial value to display in the value editor. |
| DisplayName | String | Input String that specifies the label text to display next to the value field. |
| Width | Long | Optional input Long that specifies the width of the value editor in pixels. If not specified (or specified to be 0), an internal default width value is used.   This is an optional argument whose default value is 0. |
| StandardIcon | Variant | Optional input IPictureDisp that specifies the icon to use for the control. A standard size icon is 16 pixels wide and 16 pixels high.   This is an optional argument whose default value is null. |
| LargeIcon | Variant | Optional input IPictureDisp that specifies the large icon to use for the control. A large size icon is 24 pixels wide and 24 pixels high.   This is an optional argument whose default value is null. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [MiniToolbarsample(VBA)](../../sample-programs/MiniToolbarSlotSample_VBA_Sample.md) | This sample demonstrates how to create sketch slot with minitoolbar. |

## Version

Introduced in version 2012

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
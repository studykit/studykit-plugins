# MiniToolbarControls.AddCheckBox Method

Parent Object: [MiniToolbarControls](../MiniToolbarControls/MiniToolbarControls.md)

## Description

Method that creates a new check box control within the MiniToolbar.

## Syntax

MiniToolbarControls.**AddCheckBox**( ***InternalName*** As String, ***DisplayName*** As String, ***ToolTipText*** As String, ***Checked*** As Boolean, [***StandardIcon***] As Variant, [***LargeIcon***] As Variant ) As [MiniToolbarCheckBox](../MiniToolbarCheckBox/MiniToolbarCheckBox.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| InternalName | String | Input String that specifies an internal name for the control. |
| DisplayName | String | Input String that specifies a display name for the control. If this is specified to be a null string, the control does not display any text. |
| ToolTipText | String | Input String that specifies the tooltip text for the control. |
| Checked | Boolean | Input Boolean that specifies whether to initially display the control as checked. |
| StandardIcon | Variant | Optional input IPictureDisp that specifies the icon to use for the control. A standard size icon is 16 pixels wide and 16 pixels high. |
| LargeIcon | Variant | Optional input IPictureDisp that specifies the large icon to use for the control. A large size icon is 24 pixels wide and 24 pixels high.   This is an optional argument whose default value is null. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Change color of part, features or faces](../../sample-programs/ChangeAppearanceUsingMiniToolbar_Sample.md) | This sample demonstrates how to use MiniToolBar to change appearance color of part or features or faces. |
| [MiniToolbarsample(VBA)](../../sample-programs/MiniToolbarSlotSample_VBA_Sample.md) | This sample demonstrates how to create sketch slot with minitoolbar. |

## Version

Introduced in version 2012

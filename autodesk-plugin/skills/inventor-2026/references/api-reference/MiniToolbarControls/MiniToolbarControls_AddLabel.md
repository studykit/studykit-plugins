# MiniToolbarControls.AddLabel Method

Parent Object: [MiniToolbarControls](../MiniToolbarControls/MiniToolbarControls.md)

## Description

Method that creates a new label control within the MiniToolbar.

## Syntax

MiniToolbarControls.**AddLabel**( ***InternalName*** As String, ***Text*** As String, ***ToolTipText*** As String, [***StandardIcon***] As Variant, [***LargeIcon***] As Variant ) As [MiniToolbarControl](../MiniToolbarControl/MiniToolbarControl.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| InternalName | String | Input String that specifies an internal name for the control. |
| Text | String | Input String that specifies a display name for the control. If this is specified to be a null string, the control does not display any text. |
| ToolTipText | String | Input String that specifies the tooltip text for the control. |
| StandardIcon | Variant | Optional input IPictureDisp that specifies the icon to use for the control. A standard size icon is 16 pixels wide and 16 pixels high. |
| LargeIcon | Variant | Optional input IPictureDisp that specifies the large icon to use for the control. A large size icon is 24 pixels wide and 24 pixels high.   This is an optional argument whose default value is null. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [MiniToolbarsample(VBA)](../../sample-programs/MiniToolbarSlotSample_VBA_Sample.md) | This sample demonstrates how to create sketch slot with minitoolbar. |

## Version

Introduced in version 2012

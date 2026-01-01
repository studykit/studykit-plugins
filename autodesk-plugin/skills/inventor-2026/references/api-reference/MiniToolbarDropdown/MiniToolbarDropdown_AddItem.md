# MiniToolbarDropdown.AddItem Method

Parent Object: [MiniToolbarDropdown](../MiniToolbarDropdown/MiniToolbarDropdown.md)

## Description

Method that adds an item to the control.

## Syntax

MiniToolbarDropdown.**AddItem**( ***Text*** As String, ***ToolTipText*** As String, [***InternalName***] As String, [***AllowDelete***] As Boolean, [***ShowCheckBox***] As Boolean, [***StandardIcon***] As Variant, [***LargeIcon***] As Variant, [***Index***] As Long ) As [MiniToolbarListItem](../MiniToolbarListItem/MiniToolbarListItem.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Text | String | Input String that specifies the text for the item. |
| ToolTipText | String | Input String that specifies the tooltip text for the item. This is used as the tooltip for the control when this item is selected. |
| InternalName | String | Input String that specifies an internal name for the control. You can provide this for convenience in identifying the item at a later time. If provided, it must be unique with respect to all other items in this drop down. |
| AllowDelete | Boolean | Optional input Boolean that specifies whether the user can delete this item from the drop down.   This is an optional argument whose default value is False. |
| ShowCheckBox | Boolean | Optional input Boolean that specifies if a check box should be displayed by this item. It will be initialized to be unchecked. To check it, use the IsChecked property on the returned MiniToolbarListItem.   This is an optional argument whose default value is False. |
| StandardIcon | Variant | Optional input IPictureDisp that specifies the icon to use for the item. A standard size icon is 16 pixels wide and 16 pixels high.   This is an optional argument whose default value is null. |
| LargeIcon | Variant | Optional input IPictureDisp that specifies the large icon to use for the item. A large size icon is 24 pixels wide and 24 pixels high.   This is an optional argument whose default value is null. |
| Index | Long | Optional input Long value that specifies the 1-based index at which to add the item. If not specified, the item is added at the end.   This is an optional argument whose default value is 0. |

## Version

Introduced in version 2012

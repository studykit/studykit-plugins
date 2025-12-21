# MiniToolbarControls.AddDropdown Method

Parent Object: [MiniToolbarControls](../MiniToolbarControls/MiniToolbarControls.md)

## Description

Method that creates a new dropdown control within the MiniToolbar.

## Remarks

Use the *AddItem* method on the returned control to populate the control with items. The icon, display name and the tooltip for this control are extracted from the currently selected item in the dropdown.

## Syntax

MiniToolbarControls.**AddDropdown**( ***InternalName*** As String, [***ShowIcon***] As Boolean, [***ShowText***] As Boolean, [***HasMRUBehavior***] As Boolean, [***IsSplitButton***] As Boolean ) As [MiniToolbarDropdown](../MiniToolbarDropdown/MiniToolbarDropdown.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| InternalName | String | Input String that specifies an internal name for the control. |
| ShowIcon | Boolean | Optional input Boolean that specifies whether the icon associated with the currently selected item should be displayed on the face of the control. |
| ShowText | Boolean | Optional input Boolean that specifies whether the display name associated with the currently selected item should be displayed on the face of the control.   This is an optional argument whose default value is False. |
| HasMRUBehavior | Boolean | Specifies if this button displays the most recently selected item from the list. When True, the item displayed on the button is the item last selected from the list. If False, the text of the button is independent of the list.   This is an optional argument whose default value is True. |
| IsSplitButton | Boolean | Optional input Boolean that specifies whether this is a split button dropdown control. If set to True, a separator is added between the currently selected item and the dropdown arrow within the control, and the currently selected item is clickable by the user.   This is an optional argument whose default value is False. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Change color of part, features or faces](../../sample-programs/ChangeAppearanceUsingMiniToolbar_Sample.md) | This sample demonstrates how to use MiniToolBar to change appearance color of part or features or faces. |

## Version

Introduced in version 2012

# MiniToolbarDropdown Object

## Description

The MiniToolbarDropdown object represents a dropdown control within a MiniToolbar. The pictures below illustrate various types of drop downs.

![](../images/MiniToolbarDropdown.png)

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [AddItem](../MiniToolbarDropdown/MiniToolbarDropdown_AddItem.md) | Method that adds an item to the control. |
| [AddSeparator](../MiniToolbarDropdown/MiniToolbarDropdown_AddSeparator.md) | Method that adds a separator to the control. |
| [Clear](../MiniToolbarDropdown/MiniToolbarDropdown_Clear.md) | Method that removes all the items from the control. |
| [Delete](../MiniToolbarDropdown/MiniToolbarDropdown_Delete.md) | Method that deletes the control. |
| [RemoveItem](../MiniToolbarDropdown/MiniToolbarDropdown_RemoveItem.md) | Method that removes the specified item from the control. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../MiniToolbarDropdown/MiniToolbarDropdown_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AutoHide](../MiniToolbarDropdown/MiniToolbarDropdown_AutoHide.md) | Read-write property that gets and sets whether the control should be automatically hidden when the user moves the cursor away from the MiniToolbar. |
| [ControlType](../MiniToolbarDropdown/MiniToolbarDropdown_ControlType.md) | Read-only property that returns the control type. |
| [Count](../MiniToolbarDropdown/MiniToolbarDropdown_Count.md) | Read-only property that returns the number of items in the dropdown. |
| [DisplayName](../MiniToolbarDropdown/MiniToolbarDropdown_DisplayName.md) | Read-write property that gets and sets the display name for the control. |
| [Enabled](../MiniToolbarDropdown/MiniToolbarDropdown_Enabled.md) | Read-write property that gets and sets whether the control is enabled. |
| [HasMRUBehavior](../MiniToolbarDropdown/MiniToolbarDropdown_HasMRUBehavior.md) | Read-write property that specifies if this button displays the most recently selected item from the list. |
| [Index](../MiniToolbarDropdown/MiniToolbarDropdown_Index.md) | Read-only property that returns the index this control is currently positioned at within the mini toolbar. |
| [InternalName](../MiniToolbarDropdown/MiniToolbarDropdown_InternalName.md) | Read-only property that returns a string uniquely identifying this control within the toolbar. |
| [IsSplitButton](../MiniToolbarDropdown/MiniToolbarDropdown_IsSplitButton.md) | Read-write property that specifies if this is a split button dropdown control. If True, clicking the button will result in an OnClick event. If this property if False, clicking the button will cause the pop-up to be displayed where the user can click on an item in the list. |
| [Item](../MiniToolbarDropdown/MiniToolbarDropdown_Item.md) | Returns the display name of the specified item from the dropdown. |
| [LargeIcon](../MiniToolbarDropdown/MiniToolbarDropdown_LargeIcon.md) | Read-write property that gets and sets the large icon for the control. |
| [Parent](../MiniToolbarDropdown/MiniToolbarDropdown_Parent.md) | Gets the parent object from whom this object can logically be reached. |
| [Pressed](../MiniToolbarDropdown/MiniToolbarDropdown_Pressed.md) | Read-write property that gets and sets whether the currently selected item is active. |
| [SelectedIndex](../MiniToolbarDropdown/MiniToolbarDropdown_SelectedIndex.md) | Read-write property that gets and sets the index of the item currently selected. |
| [SelectedItem](../MiniToolbarDropdown/MiniToolbarDropdown_SelectedItem.md) | Returns the item currently selected. This can return Nothing in the case where nothing is selected and will always return Nothing in the case where HasMRUBehavior is False. |
| [ShowIcon](../MiniToolbarDropdown/MiniToolbarDropdown_ShowIcon.md) | Read-write property that gets and sets whether the icon associated with the currently selected. |
| [ShowText](../MiniToolbarDropdown/MiniToolbarDropdown_ShowText.md) | Read-write property that gets and sets whether the display name associated with the currently selected item should be displayed on the face of the control. |
| [StandardIcon](../MiniToolbarDropdown/MiniToolbarDropdown_StandardIcon.md) | Read-write property that gets and sets the standard (small) icon for the control. |
| [ToolTipText](../MiniToolbarDropdown/MiniToolbarDropdown_ToolTipText.md) | Read-write property that gets and sets the tooltip text for the control. |
| [Type](../MiniToolbarDropdown/MiniToolbarDropdown_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [Visible](../MiniToolbarDropdown/MiniToolbarDropdown_Visible.md) | Read-write property that gets and sets whether the control is visible. |

## Events

|  |  |
| --- | --- |
| Name | Description |
| [OnItemHoverEnd](../MiniToolbarDropdown/MiniToolbarDropdown_OnItemHoverEnd.md) | Event that is fired when the user stops hovering over an item in the drop down in the expanded state. |
| [OnItemHoverStart](../MiniToolbarDropdown/MiniToolbarDropdown_OnItemHoverStart.md) | Event that is fired when the user starts to hover over an item in the drop down in the expanded state. |
| [OnItemRemove](../MiniToolbarDropdown/MiniToolbarDropdown_OnItemRemove.md) | Event that is fired when the user removes an item from the dropdown. |
| [OnPreMenuDisplay](../MiniToolbarDropdown/MiniToolbarDropdown_OnPreMenuDisplay.md) | Event that is fired when the user clicks the dropdown in a way where the drop down menu will be displayed. The event is fired just before the contents of the drop down list are shown to the user, so you can dynamically modify the contents of the list. If the IsSplitButton property is True, then clicking on the arrow to the right of the button will cause this event to be fired and display the drop-down list. Clicking the button itself is result in the OnSelect event to be fired. If the IsSplitbutton property is False, clicking the button will cause this event to be fired and display the drop-down list. |
| [OnSelect](../MiniToolbarDropdown/MiniToolbarDropdown_OnSelect.md) | Event that is fired soon after the user changes the currently selected item using the drop down. |

## Accessed From

[MiniToolbarControls.AddDropdown](../MiniToolbarControls/MiniToolbarControls_AddDropdown.md)

## Version

Introduced in version 2012

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
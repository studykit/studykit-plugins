# MiniToolbarComboBox Object

## Description

The MiniToolbarComboBox object represents a combobox control within a MiniToolbar.

![](../images/MiniToolbarComboBox.png)

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [AddItem](../MiniToolbarComboBox/MiniToolbarComboBox_AddItem.md) | Method that adds an item to the controls list. |
| [Clear](../MiniToolbarComboBox/MiniToolbarComboBox_Clear.md) | Method that removes all the items from the control, including any separators. |
| [Delete](../MiniToolbarComboBox/MiniToolbarComboBox_Delete.md) | Method that deletes the control. |
| [RemoveItem](../MiniToolbarComboBox/MiniToolbarComboBox_RemoveItem.md) | Method that removes the specified item or the separator from the control. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../MiniToolbarComboBox/MiniToolbarComboBox_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AutoHide](../MiniToolbarComboBox/MiniToolbarComboBox_AutoHide.md) | Read-write property that gets and sets whether the control should be automatically hidden when the user moves the cursor away from the MiniToolbar. |
| [ControlType](../MiniToolbarComboBox/MiniToolbarComboBox_ControlType.md) | Read-only property that returns the control type. |
| [Count](../MiniToolbarComboBox/MiniToolbarComboBox_Count.md) | Read-only property that returns the number of items in the combobox, including separators. |
| [DisplayName](../MiniToolbarComboBox/MiniToolbarComboBox_DisplayName.md) | Read-write property that gets and sets the display name for the control. |
| [Enabled](../MiniToolbarComboBox/MiniToolbarComboBox_Enabled.md) | Read-write property that gets and sets whether the control is enabled. |
| [Index](../MiniToolbarComboBox/MiniToolbarComboBox_Index.md) | Read-only property that returns the index this control is currently positioned at within the mini toolbar. |
| [InternalName](../MiniToolbarComboBox/MiniToolbarComboBox_InternalName.md) | Read-only property that returns a string uniquely identifying this control within the toolbar. |
| [Item](../MiniToolbarComboBox/MiniToolbarComboBox_Item.md) | Returns the text of the specified item or the name of the specified separator from the combobox. |
| [LargeIcon](../MiniToolbarComboBox/MiniToolbarComboBox_LargeIcon.md) | Read-write property that gets and sets the large icon for the control. |
| [Parent](../MiniToolbarComboBox/MiniToolbarComboBox_Parent.md) | Gets the parent object from whom this object can logically be reached. |
| [SelectedIndex](../MiniToolbarComboBox/MiniToolbarComboBox_SelectedIndex.md) | Read-write property that gets and set the index of the item currently selected. |
| [SelectedItem](../MiniToolbarComboBox/MiniToolbarComboBox_SelectedItem.md) | Returns the item currently selected. |
| [ShowIcon](../MiniToolbarComboBox/MiniToolbarComboBox_ShowIcon.md) | Read-write property that gets and sets whether the icon associated with the currently selected item should be displayed on the face of the control. |
| [ShowText](../MiniToolbarComboBox/MiniToolbarComboBox_ShowText.md) | Read-write property that gets and sets whether the display name associated with the currently selected item should be displayed on the face of the control. |
| [StandardIcon](../MiniToolbarComboBox/MiniToolbarComboBox_StandardIcon.md) | Read-write property that gets and sets the standard (small) icon for the control. |
| [ToolTipText](../MiniToolbarComboBox/MiniToolbarComboBox_ToolTipText.md) | Read-write property that gets and sets the tooltip text for the control. |
| [Type](../MiniToolbarComboBox/MiniToolbarComboBox_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [Visible](../MiniToolbarComboBox/MiniToolbarComboBox_Visible.md) | Read-write property that gets and sets whether the control is visible. |
| [Width](../MiniToolbarComboBox/MiniToolbarComboBox_Width.md) | Read-write property that gets and sets the width of the combobox in pixels. |

## Events

|  |  |
| --- | --- |
| Name | Description |
| [OnItemHoverEnd](../MiniToolbarComboBox/MiniToolbarComboBox_OnItemHoverEnd.md) | Event that is fired when the user stops hovering over an item in the combobox in the expanded state. |
| [OnItemHoverStart](../MiniToolbarComboBox/MiniToolbarComboBox_OnItemHoverStart.md) | Event that is fired when the user starts to hover over an item in the combobox in the expanded state. |
| [OnItemRemove](../MiniToolbarComboBox/MiniToolbarComboBox_OnItemRemove.md) | Event that is fired when the user removes an item from the combobox. |
| [OnPreMenuDisplay](../MiniToolbarComboBox/MiniToolbarComboBox_OnPreMenuDisplay.md) | Event that is fired when the user clicks the combobox. |
| [OnSelect](../MiniToolbarComboBox/MiniToolbarComboBox_OnSelect.md) | Event that is fired soon after the user changes the currently selected item using the drop down. |

## Accessed From

[MiniToolbarControls.AddComboBox](../MiniToolbarControls/MiniToolbarControls_AddComboBox.md)

## Version

Introduced in version 2012

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
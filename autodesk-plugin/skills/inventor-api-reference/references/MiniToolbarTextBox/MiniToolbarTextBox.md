# MiniToolbarTextBox Object

## Description

The MiniToolbarTextBox object represents a text box control within a MiniToolbar.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [AddItem](../MiniToolbarTextBox/MiniToolbarTextBox_AddItem.md) | Adds an item to the control. |
| [AddSeparator](../MiniToolbarTextBox/MiniToolbarTextBox_AddSeparator.md) | Adds a separator to this control. |
| [Clear](../MiniToolbarTextBox/MiniToolbarTextBox_Clear.md) | Removes all the items from the control. |
| [Delete](../MiniToolbarTextBox/MiniToolbarTextBox_Delete.md) | Method that deletes the control. |
| [RemoveItem](../MiniToolbarTextBox/MiniToolbarTextBox_RemoveItem.md) | Removes the specified item from the control. |
| [SetFocus](../MiniToolbarTextBox/MiniToolbarTextBox_SetFocus.md) | Sets the focus on this control and highlights the current content of the value editor. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../MiniToolbarTextBox/MiniToolbarTextBox_Application.md) | Gets the root Application object. Where the property is weakly-typed, it can be set to (QueryInterfaced for) 'Application' when running with Inventor whereas, 'ApprenticeServer' when running with the Apprentice Server. |
| [AutoHide](../MiniToolbarTextBox/MiniToolbarTextBox_AutoHide.md) | Read-write property that gets and sets whether the control should be automatically hidden when the user moves the cursor away from the MiniToolbar. |
| [BackgroundColor](../MiniToolbarTextBox/MiniToolbarTextBox_BackgroundColor.md) | Gets and sets the color of the background of the text box. |
| [ControlType](../MiniToolbarTextBox/MiniToolbarTextBox_ControlType.md) | Read-only property that returns the control type. |
| [Count](../MiniToolbarTextBox/MiniToolbarTextBox_Count.md) | Returns the number of items in the text box list. |
| [DisplayName](../MiniToolbarTextBox/MiniToolbarTextBox_DisplayName.md) | Read-write property that gets and sets the display name for the control. |
| [Enabled](../MiniToolbarTextBox/MiniToolbarTextBox_Enabled.md) | Read-write property that gets and sets whether the control is enabled. |
| [Index](../MiniToolbarTextBox/MiniToolbarTextBox_Index.md) | Read-only property that returns the index this control is currently positioned at within the mini toolbar. |
| [InternalName](../MiniToolbarTextBox/MiniToolbarTextBox_InternalName.md) | Read-only property that returns a string uniquely identifying this control within the toolbar. |
| [IsTextAcceptable](../MiniToolbarTextBox/MiniToolbarTextBox_IsTextAcceptable.md) | Gets and sets whether the text in the text box is acceptable. |
| [Item](../MiniToolbarTextBox/MiniToolbarTextBox_Item.md) | Returns the MiniToolbarListItem of the specified item from the text box list. |
| [LargeIcon](../MiniToolbarTextBox/MiniToolbarTextBox_LargeIcon.md) | Read-write property that gets and sets the large icon for the control. |
| [Parent](../MiniToolbarTextBox/MiniToolbarTextBox_Parent.md) | Gets the parent object from whom this object can logically be reached. |
| [SelectedIndex](../MiniToolbarTextBox/MiniToolbarTextBox_SelectedIndex.md) | Gets and sets the index of the item currently selected. |
| [SelectedItem](../MiniToolbarTextBox/MiniToolbarTextBox_SelectedItem.md) | Returns the item currently selected. |
| [SelectionEndPosition](../MiniToolbarTextBox/MiniToolbarTextBox_SelectionEndPosition.md) | Returns the position of the selected characters end position in the text box. |
| [SelectionStartPosition](../MiniToolbarTextBox/MiniToolbarTextBox_SelectionStartPosition.md) | Returns the position of the selected characters start position in the text box. |
| [ShowIcon](../MiniToolbarTextBox/MiniToolbarTextBox_ShowIcon.md) | Gets and sets whether the icon associated with the currently selected item should be displayed on the face of the control. |
| [StandardIcon](../MiniToolbarTextBox/MiniToolbarTextBox_StandardIcon.md) | Read-write property that gets and sets the standard (small) icon for the control. |
| [Text](../MiniToolbarTextBox/MiniToolbarTextBox_Text.md) | Gets and sets the text displayed in the text box. |
| [TextColor](../MiniToolbarTextBox/MiniToolbarTextBox_TextColor.md) | Gets and sets the color of the text in the text box. |
| [ToolTipText](../MiniToolbarTextBox/MiniToolbarTextBox_ToolTipText.md) | Read-write property that gets and sets the tooltip text for the control. |
| [Type](../MiniToolbarTextBox/MiniToolbarTextBox_Type.md) | Gets the constant that indicates the type of this object. |
| [Visible](../MiniToolbarTextBox/MiniToolbarTextBox_Visible.md) | Read-write property that gets and sets whether the control is visible. |

## Events

|  |  |
| --- | --- |
| Name | Description |
| [OnChange](../MiniToolbarTextBox/MiniToolbarTextBox_OnChange.md) | Event that is fired when the content of the value editor is changed by the user. |
| [OnEnter](../MiniToolbarTextBox/MiniToolbarTextBox_OnEnter.md) | Event that is fired just before the control gets focus. |
| [OnExit](../MiniToolbarTextBox/MiniToolbarTextBox_OnExit.md) | Event that is fired just before the control loses focus. |
| [OnItemHoverEnd](../MiniToolbarTextBox/MiniToolbarTextBox_OnItemHoverEnd.md) | Event that is fired when the user stops hovering over an item in the drop down in the expanded state. |
| [OnItemHoverStart](../MiniToolbarTextBox/MiniToolbarTextBox_OnItemHoverStart.md) | Event that is fired when the user starts to hover over an item in the drop down in the expanded state. |
| [OnItemRemove](../MiniToolbarTextBox/MiniToolbarTextBox_OnItemRemove.md) | Event that is fired when the user removes an item from the drop down. |
| [OnSelect](../MiniToolbarTextBox/MiniToolbarTextBox_OnSelect.md) | Event that is fired soon after the user changes the currently selected item using the drop down. |

## Version

Introduced in version 2018

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
# MiniToolbar Object

## Description

The MiniToolbar object provides the ability to create and display in-canvas controls for user interaction.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../MiniToolbar/MiniToolbar_Delete.md) | Method that deletes the MiniToolbar object. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../MiniToolbar/MiniToolbar_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Controls](../MiniToolbar/MiniToolbar_Controls.md) | Read-only property that returns the MiniToolbarControls collection object. |
| [EnableApply](../MiniToolbar/MiniToolbar_EnableApply.md) | Read-write property that specifies whether the ‘Apply’ button is enabled. |
| [EnableOK](../MiniToolbar/MiniToolbar_EnableOK.md) | Read-write property that specifies whether the ‘OK’ button is enabled. |
| [Height](../MiniToolbar/MiniToolbar_Height.md) | Read-only property that returns the height of the mini toolbar. |
| [HWND](../MiniToolbar/MiniToolbar_HWND.md) | Returns the HWND. |
| [Parent](../MiniToolbar/MiniToolbar_Parent.md) | Gets the parent object from whom this object can logically be reached. |
| [Position](../MiniToolbar/MiniToolbar_Position.md) | Read-write property that gets and sets the view space point specifying the current position of the toolbar within the graphical window. |
| [ShowApply](../MiniToolbar/MiniToolbar_ShowApply.md) | Read-write property that gets and sets whether the toolbar should display the ‘Apply’ button (represented by a green plus symbol). |
| [ShowCancel](../MiniToolbar/MiniToolbar_ShowCancel.md) | Read-write property that gets and sets whether the toolbar should display the ‘Cancel’ button (represented by a red ‘x’). |
| [ShowHandle](../MiniToolbar/MiniToolbar_ShowHandle.md) | Read-write property that gets and sets whether the toolbar should display the handle which is used to move the minitoolbar. |
| [ShowOK](../MiniToolbar/MiniToolbar_ShowOK.md) | Read-write property that gets and sets whether the toolbar should display the OK button (represented by a green check mark). |
| [ShowOptionBox](../MiniToolbar/MiniToolbar_ShowOptionBox.md) | Read-write property that gets and sets whether the toolbar should display the option box. |
| [Type](../MiniToolbar/MiniToolbar_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [Visible](../MiniToolbar/MiniToolbar_Visible.md) | Read-write property that gets and sets whether the toolbar is visible. |
| [Width](../MiniToolbar/MiniToolbar_Width.md) | Read-only property that returns the width of the mini toolbar. |

## Events

|  |  |
| --- | --- |
| Name | Description |
| [OnApply](../MiniToolbar/MiniToolbar_OnApply.md) | Event that fires when the ‘Apply’ button is clicked. |
| [OnCancel](../MiniToolbar/MiniToolbar_OnCancel.md) | Event that fires when the ‘Cancel’ button is clicked. |
| [OnEndMove](../MiniToolbar/MiniToolbar_OnEndMove.md) | Event that fires when a drag or a reposition of this MiniToolbar ends. |
| [OnHide](../MiniToolbar/MiniToolbar_OnHide.md) | Event that fires when this MiniToolbar is hidden. |
| [OnMove](../MiniToolbar/MiniToolbar_OnMove.md) | Event that fires when this MiniToolbar moves as a result of a drag. |
| [OnOK](../MiniToolbar/MiniToolbar_OnOK.md) | Event that fires when the ‘OK’ button is clicked. |
| [OnShow](../MiniToolbar/MiniToolbar_OnShow.md) | Event that fires when this MiniToolbar is shown. |
| [OnStartMove](../MiniToolbar/MiniToolbar_OnStartMove.md) | Event that fires when this MiniToolbar begins to move as a result of a drag or a reposition. |

## Accessed From

[CommandManager.CreateMiniToolbar](../CommandManager/CommandManager_CreateMiniToolbar.md), [InteractionEvents.CreateMiniToolbar](../InteractionEvents/InteractionEvents_CreateMiniToolbar.md), [MiniToolbarButton.Parent](../MiniToolbarButton/MiniToolbarButton_Parent.md), [MiniToolbarCheckBox.Parent](../MiniToolbarCheckBox/MiniToolbarCheckBox_Parent.md), [MiniToolbarComboBox.Parent](../MiniToolbarComboBox/MiniToolbarComboBox_Parent.md), [MiniToolbarControl.Parent](../MiniToolbarControl/MiniToolbarControl_Parent.md), [MiniToolbarDropdown.Parent](../MiniToolbarDropdown/MiniToolbarDropdown_Parent.md), [MiniToolbarSlider.Parent](../MiniToolbarSlider/MiniToolbarSlider_Parent.md), [MiniToolbarTextBox.Parent](../MiniToolbarTextBox/MiniToolbarTextBox_Parent.md), [MiniToolbarTextEditor.Parent](MiniToolbarTextEditor_Parent.md), [MiniToolbarValueEditor.Parent](../MiniToolbarValueEditor/MiniToolbarValueEditor_Parent.md)

## Version

Introduced in version 2012

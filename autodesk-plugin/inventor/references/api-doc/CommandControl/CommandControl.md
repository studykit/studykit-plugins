# CommandControl Object

## Description

A CommandControl object represents a user interface control (button, combobox, split button, etc.).

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../CommandControl/CommandControl_Delete.md) | Method that deletes the CommandControl. This simply removes the control from the panel, but does not delete the underlying ControlDefinition(s). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../CommandControl/CommandControl_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [ChildControls](../CommandControl/CommandControl_ChildControls.md) | Property that returns a CommandControls collection object that provides access to the child controls of this control. |
| [ControlDefinition](../CommandControl/CommandControl_ControlDefinition.md) | Property that returns the ControlDefinition associated with this control. |
| [ControlType](../CommandControl/CommandControl_ControlType.md) | Property that returns the control type. |
| [DisplayedControl](../CommandControl/CommandControl_DisplayedControl.md) | Gets and sets the current ControlDefinition object for kButtonPopupControl, kPopupControl, kSplitButtonMRUControl and kSplitButtonControl control types. For other control types, this property returns Nothing. |
| [DisplayName](../CommandControl/CommandControl_DisplayName.md) | Property that returns the display name of the control. |
| [InternalName](../CommandControl/CommandControl_InternalName.md) | Property that returns the unique internal name of the control. |
| [KeyTip](../CommandControl/CommandControl_KeyTip.md) | Gets and sets the keyboard access key for the control. |
| [Parent](../CommandControl/CommandControl_Parent.md) | Property that returns the parent object. This can either be a RibbonPanel object if the control resides within a panel, or the UserInterfaceManager object if the control resides elsewhere (Quick Access Toolbar, etc.). |
| [ShowText](../CommandControl/CommandControl_ShowText.md) | Gets and sets whether to display the text (display name) associated with the control. The 'Ribbon Appearance' user choice overrides this setting. |
| [Type](../CommandControl/CommandControl_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [UseLargeIcon](../CommandControl/CommandControl_UseLargeIcon.md) | Gets and sets whether to display the control in the larger size. The 'Ribbon Appearance' user choice overrides this setting. |
| [Visible](../CommandControl/CommandControl_Visible.md) | Gets and sets whether this control is currently visible in the ribbon. |

## Accessed From

[CommandControls.AddButton](../CommandControls/CommandControls_AddButton.md), [CommandControls.AddButtonPopup](../CommandControls/CommandControls_AddButtonPopup.md), [CommandControls.AddComboBox](../CommandControls/CommandControls_AddComboBox.md), [CommandControls.AddCopy](../CommandControls/CommandControls_AddCopy.md), [CommandControls.AddGallery](../CommandControls/CommandControls_AddGallery.md), [CommandControls.AddMacro](../CommandControls/CommandControls_AddMacro.md), [CommandControls.AddPopup](../CommandControls/CommandControls_AddPopup.md), [CommandControls.AddSeparator](../CommandControls/CommandControls_AddSeparator.md), [CommandControls.AddSplitButton](../CommandControls/CommandControls_AddSplitButton.md), [CommandControls.AddSplitButtonMRU](../CommandControls/CommandControls_AddSplitButtonMRU.md), [CommandControls.AddTogglePopup](../CommandControls/CommandControls_AddTogglePopup.md), [CommandControls.Item](../CommandControls/CommandControls_Item.md), [CommandControlsEnumerator.Item](../CommandControlsEnumerator/CommandControlsEnumerator_Item.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Print information about all available ribbons.](../../sample-programs/DumpRibbons_Sample.md) | This sample prints out all of the elements of the ribbons. This output is very useful when customizing the ribbon to be able to get the names of the various existing ribbons, tabs, and panels. |

## Version

Introduced in version 2010

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
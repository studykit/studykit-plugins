# ComboBoxDefinition Object

## Description

The ComboBoxDefinition object represents any command whose user interface is a combo box.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [AddItem](../ComboBoxDefinition/ComboBoxDefinition_AddItem.md) | Adds Item to ComboBox. |
| [AutoAddToGUI](../ComboBoxDefinition/ComboBoxDefinition_AutoAddToGUI.md) | Adds it to AddIn Toolbar. |
| [Clear](../ComboBoxDefinition/ComboBoxDefinition_Clear.md) | Clear the ComboBox Definition. |
| [Delete](../ComboBoxDefinition/ComboBoxDefinition_Delete.md) | Method that deletes the UIDefinition Object. |
| [Execute](../ComboBoxDefinition/ComboBoxDefinition_Execute.md) | Executes this ControlDefinition object. |
| [Execute2](../ComboBoxDefinition/ComboBoxDefinition_Execute2.md) | Executes the ControlDefinition synchronously or asynchronously. |
| [RemoveItem](../ComboBoxDefinition/ComboBoxDefinition_RemoveItem.md) | Removes specified item from the combo box list. The index is 1 based. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../ComboBoxDefinition/ComboBoxDefinition_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [BuiltIn](../ComboBoxDefinition/ComboBoxDefinition_BuiltIn.md) | Gets the BuiltIn status for a UIDefinition. |
| [Classification](../ComboBoxDefinition/ComboBoxDefinition_Classification.md) | Gets the classification. |
| [ClientId](../ComboBoxDefinition/ComboBoxDefinition_ClientId.md) | Gets ClientID. |
| [DefaultShortcut](../ComboBoxDefinition/ComboBoxDefinition_DefaultShortcut.md) | Gets/Sets the default (internal) shortcut assigned to the command. Setting this property fails for built-in ControlDefinitions. |
| [DefaultShortcutType](../ComboBoxDefinition/ComboBoxDefinition_DefaultShortcutType.md) | Gets the type of default shortcut assigned to this command. Possible return values are kNoShortcut (no shortcut has been assigned), kAcceleratorShortcut (a shortcut that directly launches the command), or kAliasShortcut (a command alias). |
| [DefinitionType](../ComboBoxDefinition/ComboBoxDefinition_DefinitionType.md) | Gets the ControlDefinitionType. |
| [DescriptionText](../ComboBoxDefinition/ComboBoxDefinition_DescriptionText.md) | Gets/Sets Description Text. |
| [DisplayName](../ComboBoxDefinition/ComboBoxDefinition_DisplayName.md) | Gets the Display Name. |
| [DropDownWidth](../ComboBoxDefinition/ComboBoxDefinition_DropDownWidth.md) | Gets/Sets DropDown Width. |
| [Enabled](../ComboBoxDefinition/ComboBoxDefinition_Enabled.md) | Enables/Disables the UIDefinition object. |
| [InternalName](../ComboBoxDefinition/ComboBoxDefinition_InternalName.md) | Gets the Internal Name. |
| [IntroducedInVersion](../ComboBoxDefinition/ComboBoxDefinition_IntroducedInVersion.md) | Read-write property that gets and sets the introduced in version of the control definition. The values from AvailableComparisonVersions can be used to set this property. This is read only if the control definition is built-in. |
| [IsShortcutOverridden](../ComboBoxDefinition/ComboBoxDefinition_IsShortcutOverridden.md) | Gets whether the default (internal) shortcut has been overridden by the user or through the API. |
| [LargeIcon](../ComboBoxDefinition/ComboBoxDefinition_LargeIcon.md) | Gets/Sets LargeIcon. |
| [LastUpdatedVersion](../ComboBoxDefinition/ComboBoxDefinition_LastUpdatedVersion.md) | Read-write property that gets and sets the last updated version of the control definition. The values from AvailableComparisonVersions can be used to set this property. This is read only if the control definition is built-in. |
| [ListCount](../ComboBoxDefinition/ComboBoxDefinition_ListCount.md) | Gets number of Items in the combo box list. |
| [ListIndex](../ComboBoxDefinition/ComboBoxDefinition_ListIndex.md) | Gets or sets 1 based index of selected item. Returns 0 if nothing is selected. |
| [ListItem](../ComboBoxDefinition/ComboBoxDefinition_ListItem.md) | Gets the item specified in the combo box. The index is 1 based. |
| [OverrideShortcut](../ComboBoxDefinition/ComboBoxDefinition_OverrideShortcut.md) | Gets/Sets the override shortcut assigned to the command. Setting this property to a null string clears the override. |
| [OverrideShortcutType](../ComboBoxDefinition/ComboBoxDefinition_OverrideShortcutType.md) | Gets the type of override shortcut assigned to this command. Possible return values are kNoShortcut (no shortcut has been assigned), kAcceleratorShortcut (a shortcut that directly launches the command), or kAliasShortcut (a command alias). |
| [Parent](../ComboBoxDefinition/ComboBoxDefinition_Parent.md) | Gets the parent object from whom this object can logically be reached. |
| [ProgressiveToolTip](../ComboBoxDefinition/ComboBoxDefinition_ProgressiveToolTip.md) | Returns a ProgressiveToolTip object providing access to enhanced tooltip display for controls in the ribbon interface. |
| [StandardIcon](../ComboBoxDefinition/ComboBoxDefinition_StandardIcon.md) | Gets/Sets StandardIcon. |
| [Text](../ComboBoxDefinition/ComboBoxDefinition_Text.md) | Gets the Text from the display or edit portion of the combo box. |
| [ToolTipText](../ComboBoxDefinition/ComboBoxDefinition_ToolTipText.md) | Gets/Sets Tooltip. |
| [Type](../ComboBoxDefinition/ComboBoxDefinition_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Events

|  |  |
| --- | --- |
| Name | Description |
| [OnHelp](../ComboBoxDefinition/ComboBoxDefinition_OnHelp.md) | Fires signaling the client to present help for the associated command. |
| [OnSelect](../ComboBoxDefinition/ComboBoxDefinition_OnSelect.md) | Event that is fired when an end user changes the selection in the combo box or when the selection is changed using the ListIndex property. This event is not fired for built-in definitions. |

## Accessed From

[ControlDefinitions.AddComboBoxDefinition](../ControlDefinitions/ControlDefinitions_AddComboBoxDefinition.md)

## Version

Introduced in version 9

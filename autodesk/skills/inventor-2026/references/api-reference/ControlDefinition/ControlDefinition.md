# ControlDefinition Object

## Description

The ControlDefinition object is the base class for all other command definition types. This includes the following objects: ButtonDefinition, ComboBoxDefinition, and MacroControlDefinition.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [AutoAddToGUI](../ControlDefinition/ControlDefinition_AutoAddToGUI.md) | Method that automatically adds a control based on this definition to the General panel of the Add-Ins tab in the ribbon interface. |
| [Delete](../ControlDefinition/ControlDefinition_Delete.md) | Method that deletes the control definition. This method fails for built-in definitions. |
| [Execute](../ControlDefinition/ControlDefinition_Execute.md) | Method that runs the built-in command or sends the Click event to the Add-In. The end result of calling the Execute method is the same as if the user had clicked/pressed the relevant control - for example, by clicking on a button that references a ButtonDefinition object. |
| [Execute2](../ControlDefinition/ControlDefinition_Execute2.md) | Method that executes the control definition synchronously or asynchronously. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../ControlDefinition/ControlDefinition_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [BuiltIn](../ControlDefinition/ControlDefinition_BuiltIn.md) | Property that specifies if the control or definition is a standard Autodesk Inventor control or definition. Built-in ones have restrictions in the edits that can be performed. |
| [Classification](../ControlDefinition/ControlDefinition_Classification.md) | Property that returns the command classification of the ControlDefinition. These classifications are bits and can be combined to designate that a command falls within more than one classification. Because they are bits, care needs to be taken when interpreting the returned values. |
| [ClientId](../ControlDefinition/ControlDefinition_ClientId.md) | Property that returns the string that uniquely identifies the client. This is the CLSID of the AddIn in a string form, e.g. "{C9A6C580-3817-11D0-BE4E-080036E87B02}". |
| [DefaultShortcut](../ControlDefinition/ControlDefinition_DefaultShortcut.md) | Gets/Sets the default (internal) shortcut assigned to the command. Setting this property fails for built-in ControlDefinitions. |
| [DefaultShortcutType](../ControlDefinition/ControlDefinition_DefaultShortcutType.md) | Property that returns the type of shortcut assigned to this command. |
| [DefinitionType](../ControlDefinition/ControlDefinition_DefinitionType.md) | Property that returns the control definition type. The possible return values are kButtonDefinition, kComboBoxDefinition, and kMacroControlDefinition. |
| [DescriptionText](../ControlDefinition/ControlDefinition_DescriptionText.md) | Gets/Sets Description Text. For MacroControlDefinition this property is read-only. |
| [DisplayName](../ControlDefinition/ControlDefinition_DisplayName.md) | Property that returns the display name of the ControlDefinition. |
| [Enabled](../ControlDefinition/ControlDefinition_Enabled.md) | Enables/Disables the UIDefinition object. |
| [InternalName](../ControlDefinition/ControlDefinition_InternalName.md) | Property that returns the internal name. This name is the internal unique identifier for the ControlDefinition. |
| [IntroducedInVersion](../ControlDefinition/ControlDefinition_IntroducedInVersion.md) | Read-write property that gets and sets the introduced in version of the control definition. The values from AvailableComparisonVersions can be used to set this property. This is read only if the control definition is built-in or if it is MacroControlDefinition. |
| [IsShortcutOverridden](../ControlDefinition/ControlDefinition_IsShortcutOverridden.md) | Property that returns whether the default (internal) shortcut has been overridden by the user or through the API. |
| [LargeIcon](../ControlDefinition/ControlDefinition_LargeIcon.md) | Gets/Sets LargeIcon. For MacroControlDefinition this property is read-only. |
| [LastUpdatedVersion](../ControlDefinition/ControlDefinition_LastUpdatedVersion.md) | Read-write property that gets and sets the last updated version of the control definition. The values from AvailableComparisonVersions can be used to set this property. This is read only if the control definition is built-in or if it is MacroControlDefinition. |
| [OverrideShortcut](../ControlDefinition/ControlDefinition_OverrideShortcut.md) | Gets/Sets the override shortcut assigned to the command. Setting this property to a null string clears the override. |
| [OverrideShortcutType](../ControlDefinition/ControlDefinition_OverrideShortcutType.md) | Property that returns the type of override shortcut assigned to this command. |
| [Parent](../ControlDefinition/ControlDefinition_Parent.md) | Property that returns the parent object from whom this object can logically be reached. |
| [ProgressiveToolTip](../ControlDefinition/ControlDefinition_ProgressiveToolTip.md) | Property that returns a ProgressiveToolTip object providing access to enhanced tooltip display for controls in the ribbon interface. |
| [StandardIcon](../ControlDefinition/ControlDefinition_StandardIcon.md) | Gets/Sets StandardIcon. For MacroControlDefinition this property is read-only. |
| [ToolTipText](../ControlDefinition/ControlDefinition_ToolTipText.md) | Gets/Sets Tooltip. For MacroControlDefinition this property is read-only |
| [Type](../ControlDefinition/ControlDefinition_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[ButtonDefinitionHandler.ControlDefinition](ButtonDefinitionHandler_ControlDefinition.md), [CommandBarButton.ControlDefinition](CommandBarButton_ControlDefinition.md), [CommandBarButton.DisplayedControl](CommandBarButton_DisplayedControl.md), [CommandBarControl.ControlDefinition](CommandBarControl_ControlDefinition.md), [CommandBarControl.DisplayedControl](CommandBarControl_DisplayedControl.md), [CommandBarPopUp.ControlDefinition](CommandBarPopUp_ControlDefinition.md), [CommandBarPopUp.DisplayedControl](CommandBarPopUp_DisplayedControl.md), [CommandControl.ControlDefinition](../CommandControl/CommandControl_ControlDefinition.md), [CommandControl.DisplayedControl](../CommandControl/CommandControl_DisplayedControl.md), [ControlDefinitionEvents.Parent](ControlDefinitionEvents_Parent.md), [ControlDefinitions.Item](../ControlDefinitions/ControlDefinitions_Item.md), [DisabledCommandList.Item](../DisabledCommandList/DisabledCommandList_Item.md), [DockableWindow.VisibilityControl](../DockableWindow/DockableWindow_VisibilityControl.md), [ProgressiveToolTip.Parent](../ProgressiveToolTip/ProgressiveToolTip_Parent.md), [WebBrowserDockableWindow.VisibilityControl](WebBrowserDockableWindow_VisibilityControl.md)

## Derived Classes

[MacroControlDefinition](../MacroControlDefinition/MacroControlDefinition.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Copy a sketch](../../sample-programs/CopySketch_Sample.md) | This sample demonstrates copying the contents of a sketch into another sketch via the API. |
| [Add parallel environment with contextual tabs](../../sample-programs/CreateParallelEnvironment_Sample.md) | The following sample demonstrates the use of parallel environments and contextual ribbon tabs. |
| [Print list of all Inventor Commands](../../sample-programs/DumpControlDefinitions_Sample.md) | This sample prints the internal names and descriptions of all commands (aka ControlDefinitions) in Inventor. |
| [Post Private Event Sample](../../sample-programs/PostPrivateEventSample_Sample.md) | This sample demonstrates how to use the PostPrivateEvent to configure the options for placing a part component. |
| [Break alignment of a section view](../../sample-programs/SectionDrawingView_Sample.md) | Sample showing how to break the alignment of a drawing section view by calling the DrawingBreakViewAlignment command. |

## Version

Introduced in version 6

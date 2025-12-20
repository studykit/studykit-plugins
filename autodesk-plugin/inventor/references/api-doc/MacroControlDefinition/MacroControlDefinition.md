# MacroControlDefinition Object

Derived from: [ControlDefinition](../ControlDefinition/ControlDefinition.md) Object

## Description

The MacroControlDefinition object represents a command that causes a macro to run.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [AutoAddToGUI](../MacroControlDefinition/MacroControlDefinition_AutoAddToGUI.md) | Method that automatically adds a control based on this definition to the General panel of the Add-Ins tab in the ribbon interface. |
| [Delete](../MacroControlDefinition/MacroControlDefinition_Delete.md) | Method that deletes the control definition. This method fails for built-in definitions. |
| [Execute](../MacroControlDefinition/MacroControlDefinition_Execute.md) | Method that runs the built-in command or sends the Click event to the Add-In. The end result of calling the Execute method is the same as if the user had clicked/pressed the relevant control - for example, by clicking on a button that references a ButtonDefinition object. |
| [Execute2](../MacroControlDefinition/MacroControlDefinition_Execute2.md) | Method that executes the control definition synchronously or asynchronously. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../MacroControlDefinition/MacroControlDefinition_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [BuiltIn](../MacroControlDefinition/MacroControlDefinition_BuiltIn.md) | Property that specifies if the control or definition is a standard Autodesk Inventor control or definition. Built-in ones have restrictions in the edits that can be performed. |
| [Classification](../MacroControlDefinition/MacroControlDefinition_Classification.md) | Property that returns the command classification of the ControlDefinition. These classifications are bits and can be combined to designate that a command falls within more than one classification. Because they are bits, care needs to be taken when interpreting the returned values. |
| [ClientId](../MacroControlDefinition/MacroControlDefinition_ClientId.md) | Property that returns the string that uniquely identifies the client. This is the CLSID of the AddIn in a string form, e.g. "{C9A6C580-3817-11D0-BE4E-080036E87B02}". |
| [DefaultShortcut](../MacroControlDefinition/MacroControlDefinition_DefaultShortcut.md) | Gets/Sets the default (internal) shortcut assigned to the command. Setting this property fails for built-in ControlDefinitions. |
| [DefaultShortcutType](../MacroControlDefinition/MacroControlDefinition_DefaultShortcutType.md) | Property that returns the type of shortcut assigned to this command. |
| [DefinitionType](../MacroControlDefinition/MacroControlDefinition_DefinitionType.md) | Property that returns the control definition type. The possible return values are kButtonDefinition, kComboBoxDefinition, and kMacroControlDefinition. |
| [DescriptionText](../MacroControlDefinition/MacroControlDefinition_DescriptionText.md) | Gets/Sets Description Text. For MacroControlDefinition this property is read-only. |
| [DisplayName](../MacroControlDefinition/MacroControlDefinition_DisplayName.md) | Property that returns the display name of the ControlDefinition. |
| [Enabled](../MacroControlDefinition/MacroControlDefinition_Enabled.md) | Enables/Disables the UIDefinition object. |
| [InternalName](../MacroControlDefinition/MacroControlDefinition_InternalName.md) | Property that returns the internal name. This name is the internal unique identifier for the ControlDefinition. |
| [IntroducedInVersion](../MacroControlDefinition/MacroControlDefinition_IntroducedInVersion.md) | Read-write property that gets and sets the introduced in version of the control definition. The values from AvailableComparisonVersions can be used to set this property. This is read only if the control definition is built-in or if it is MacroControlDefinition. |
| [IsShortcutOverridden](../MacroControlDefinition/MacroControlDefinition_IsShortcutOverridden.md) | Property that returns whether the default (internal) shortcut has been overridden by the user or through the API. |
| [LargeIcon](../MacroControlDefinition/MacroControlDefinition_LargeIcon.md) | Gets/Sets LargeIcon. For MacroControlDefinition this property is read-only. |
| [LastUpdatedVersion](../MacroControlDefinition/MacroControlDefinition_LastUpdatedVersion.md) | Read-write property that gets and sets the last updated version of the control definition. The values from AvailableComparisonVersions can be used to set this property. This is read only if the control definition is built-in or if it is MacroControlDefinition. |
| [MacroOrFileName](../MacroControlDefinition/MacroControlDefinition_MacroOrFileName.md) | Property that indicates the macro or filename associated with this MacroControlDefinition. A VBA macro must be a Public Sub defined in a standard code module of the Application VBA project. The Sub cannot have any input arguments. The Sub is specified using 'Module.SubName' format. For example, the Sub MovePart in a module named AsmTools would be specified by 'AsmTools.MovePart'. If a filename with an .ide extension is supplied it is assumed to be an iFeature. When the user clicks the button it will begin placement of the iFeature. The filename must be a full filename. If an external EXE is specified, this must be the full path to the EXE. |
| [OverrideShortcut](../MacroControlDefinition/MacroControlDefinition_OverrideShortcut.md) | Gets/Sets the override shortcut assigned to the command. Setting this property to a null string clears the override. |
| [OverrideShortcutType](../MacroControlDefinition/MacroControlDefinition_OverrideShortcutType.md) | Property that returns the type of override shortcut assigned to this command. |
| [Parent](../MacroControlDefinition/MacroControlDefinition_Parent.md) | Property that returns the parent object from whom this object can logically be reached. |
| [ProgressiveToolTip](../MacroControlDefinition/MacroControlDefinition_ProgressiveToolTip.md) | Property that returns a ProgressiveToolTip object providing access to enhanced tooltip display for controls in the ribbon interface. |
| [StandardIcon](../MacroControlDefinition/MacroControlDefinition_StandardIcon.md) | Gets/Sets StandardIcon. For MacroControlDefinition this property is read-only. |
| [ToolTipText](../MacroControlDefinition/MacroControlDefinition_ToolTipText.md) | Gets/Sets Tooltip. For MacroControlDefinition this property is read-only |
| [Type](../MacroControlDefinition/MacroControlDefinition_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[ControlDefinitions.AddMacroControlDefinition](../ControlDefinitions/ControlDefinitions_AddMacroControlDefinition.md)

## Version

Introduced in version 9

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
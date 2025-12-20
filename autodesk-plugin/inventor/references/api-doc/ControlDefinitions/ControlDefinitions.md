# ControlDefinitions Object

## Description

The ControlDefinitions collection object provides access to existing objects.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [AddButtonDefinition](../ControlDefinitions/ControlDefinitions_AddButtonDefinition.md) | Method that adds a newButtonDefinition object. |
| [AddComboBoxDefinition](../ControlDefinitions/ControlDefinitions_AddComboBoxDefinition.md) | Method that creates a new ComboBoxDefinition object. |
| [AddMacroControlDefinition](../ControlDefinitions/ControlDefinitions_AddMacroControlDefinition.md) | Method that creates a new MacroControlDefinition object. The MacroControlDefinition object is used to define the information associated with a button that can be used to execute an Inventor VBA macro, insert an iPart, insert an iFeature or execute an EXE. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../ControlDefinitions/ControlDefinitions_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Count](../ControlDefinitions/ControlDefinitions_Count.md) | Property that returns the number of items in the collection. |
| [Item](../ControlDefinitions/ControlDefinitions_Item.md) | Returns the specified ControlDefinitionobject from the collection. |
| [Type](../ControlDefinitions/ControlDefinitions_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [UseDefaultMultiCharAliases](../ControlDefinitions/ControlDefinitions_UseDefaultMultiCharAliases.md) | Gets/Sets whether the multi-character Command Aliases delivered with Inventor should be used. The equivalent UI option is found under the 'Keyboard' tab of the Customize dialog. |

## Accessed From

[CommandManager.ControlDefinitions](../CommandManager/CommandManager_ControlDefinitions.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Add commands to the application menu](../../sample-programs/AddButtonToAppMenu_Sample.md) | Demonstrates adding command to the application menu. |
| [Add parallel environment with contextual tabs](../../sample-programs/CreateParallelEnvironment_Sample.md) | The following sample demonstrates the use of parallel environments and contextual ribbon tabs. |
| [Print list of all Inventor Commands](../../sample-programs/DumpControlDefinitions_Sample.md) | This sample prints the internal names and descriptions of all commands (aka ControlDefinitions) in Inventor. |
| [Create a ribbon panel in an existing tab](../../sample-programs/RibbonPanels_Add_Sample.md) | Demonstrates creating a new ribbon panel within an existing ribbon tab. |
| [Break alignment of a section view](../../sample-programs/SectionDrawingView_Sample.md) | Sample showing how to break the alignment of a drawing section view by calling the DrawingBreakViewAlignment command. |

## Version

Introduced in version 6

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
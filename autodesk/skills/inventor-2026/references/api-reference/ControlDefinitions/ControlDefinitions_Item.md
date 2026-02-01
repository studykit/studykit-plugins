# ControlDefinitions.Item Property

Parent Object: [ControlDefinitions](../ControlDefinitions/ControlDefinitions.md)

## Description

Returns the specified ControlDefinitionobject from the collection.

## Syntax

ControlDefinitions.**Item**( ***Index*** As Variant ) As [ControlDefinition](../ControlDefinition/ControlDefinition.md)

## Property Value

This is a read only property whose value is a [ControlDefinition](../ControlDefinition/ControlDefinition.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Input Variant value that specifies the index of the to return. This can be either a numeric value indicating the index of the item in the collection or it can be a string indicating the ControlDefinition name. If an out of range index or a name of a non-existent ControlDefinition is provided, an error occurs. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Add commands to the application menu](../../sample-programs/AddButtonToAppMenu_Sample.md) | Demonstrates adding command to the application menu. |
| [Copy a sketch](../../sample-programs/CopySketch_Sample.md) | This sample demonstrates copying the contents of a sketch into another sketch via the API. |
| [Add parallel environment with contextual tabs](../../sample-programs/CreateParallelEnvironment_Sample.md) | The following sample demonstrates the use of parallel environments and contextual ribbon tabs. |
| [Creation of an override environment for a document](../../sample-programs/EnvironmentManager_OverrideEnvironment_Sample.md) | A new ribbon tab is created and associated with the override environment. |
| [Create a ribbon panel in an existing tab](../../sample-programs/RibbonPanels_Add_Sample.md) | Demonstrates creating a new ribbon panel within an existing ribbon tab. |
| [Break alignment of a section view](../../sample-programs/SectionDrawingView_Sample.md) | Sample showing how to break the alignment of a drawing section view by calling the DrawingBreakViewAlignment command. |

## Version

Introduced in version 7

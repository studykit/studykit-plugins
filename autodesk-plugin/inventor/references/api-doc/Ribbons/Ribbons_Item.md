# Ribbons.Item Property

Parent Object: [Ribbons](../Ribbons/Ribbons.md)

## Description

Returns the specified Ribbon object from the collection.

## Syntax

Ribbons.**Item**( ***Index*** As Variant ) As [Ribbon](../Ribbon/Ribbon.md)

## Property Value

This is a read only property whose value is a [Ribbon](../Ribbon/Ribbon.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Input Variant value that specifies the Ribbon to return. This can be either a numeric value indicating the index of the item in the collection or it can be a string indicating the internal name of the Ribbon. If an out of range index or a name of a non\-existent Ribbon is provided, an error will occur.  The following are the names of Inventor Ribbons\: \* 'Part' \* 'Assembly' \* 'Drawing' \* 'Presentation' \* 'iFeatures' \* 'ZeroDoc' \* 'UnknownDocument' |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Add parallel environment with contextual tabs](../../sample-programs/CreateParallelEnvironment_Sample.md) | The following sample demonstrates the use of parallel environments and contextual ribbon tabs. |
| [Creation of an override environment for a document](../../sample-programs/EnvironmentManager_OverrideEnvironment_Sample.md) | A new ribbon tab is created and associated with the override environment. |
| [Create a ribbon panel in an existing tab](../../sample-programs/RibbonPanels_Add_Sample.md) | Demonstrates creating a new ribbon panel within an existing ribbon tab. |

## Version

Introduced in version 2010

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
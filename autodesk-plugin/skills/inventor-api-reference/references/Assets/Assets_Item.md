# Assets.Item Property

Parent Object: [Assets](../Assets/Assets.md)

## Description

Read-only property that returns the specified Asset object from the collection.

## Syntax

Assets.**Item**( ***Index*** As Variant ) As [Asset](../Asset/Asset.md)

## Property Value

This is a read only property whose value is an [Asset](../Asset/Asset.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Input Variant value that specifies the Asset to return. This can be either a numeric value indicating the index of the item in the collection or it can be a string indicating the asset name. For the name, the value of the Name property is used as a unique identifier for the asset. If an out of range index or a name of a non-existent asset is provided, an error will occur. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Set the appearance of an occurrence.](../../sample-programs/SetOccurrenceAppearance_Sample.md) | Sets the appearance of a selected occurrence in an assembly. |

## Version

Introduced in version 2014

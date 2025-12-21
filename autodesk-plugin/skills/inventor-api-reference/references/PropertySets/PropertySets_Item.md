# PropertySets.Item Property

Parent Object: [PropertySets](../PropertySets/PropertySets.md)

## Description

Gets the set in this collection in a sequences fashion; by index, or by its name -- Display or Internal.

## Syntax

PropertySets.**Item**( ***Index*** As Variant ) As [PropertySet](../PropertySet/PropertySet.md)

## Property Value

This is a read only property whose value is a [PropertySet](../PropertySet/PropertySet.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Input Variant value that specifies the index of the PropertySet to return. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Using the BOM APIs](../../sample-programs/BOM_Sample.md) | This sample demonstrates the Bill of Materials API functionality in assemblies. |
| [Update iProperty values using Apprentice](../../sample-programs/iPropertyApprentice_Sample.md) | Updates some iProperty values using Apprentice. The document specified in the code for the Open method must exist. |
| [Create custom iProperties](../../sample-programs/iPropertyCreateCustom_Sample.md) | Creates custom iProperties of various types. A document must be open when this sample is run. |
| [Create or update custom iProperty](../../sample-programs/iPropertyCreateUpdateCustom_Sample.md) | This example creates a custom iProperty if it doesn't exist and updates the value if it does already exist. A part document must be open before runnin the sample. |
| [Get value of iProperty](../../sample-programs/iPropertyGetValue_Sample.md) | Demonstrates getting the values of the "Part Number" iProperty. Any property can be retrieved by accesing the correct property set and property.  A document must be open when this sample is run. |

## Version

Introduced in version 4

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
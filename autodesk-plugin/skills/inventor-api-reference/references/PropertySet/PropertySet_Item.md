# PropertySet.Item Property

Parent Object: [PropertySet](../PropertySet/PropertySet.md)

## Description

Gets the Property given either its name or its sequential index.

## Syntax

PropertySet.**Item**( ***Index*** As Variant ) As [Property](../Property/Property.md)

## Property Value

This is a read only property whose value is a [Property](../Property/Property.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Input Variant value that specifies the index of the Property to return. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Update iProperty values using Apprentice](../../sample-programs/iPropertyApprentice_Sample.md) | Updates some iProperty values using Apprentice. The document specified in the code for the Open method must exist. |
| [Create or update custom iProperty](../../sample-programs/iPropertyCreateUpdateCustom_Sample.md) | This example creates a custom iProperty if it doesn't exist and updates the value if it does already exist. A part document must be open before runnin the sample. |
| [Get value of iProperty](../../sample-programs/iPropertyGetValue_Sample.md) | Demonstrates getting the values of the "Part Number" iProperty. Any property can be retrieved by accesing the correct property set and property.  A document must be open when this sample is run. |

## Version

Introduced in version 4

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
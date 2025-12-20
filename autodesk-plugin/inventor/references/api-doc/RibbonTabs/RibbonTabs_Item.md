# RibbonTabs.Item Property

Parent Object: [RibbonTabs](../RibbonTabs/RibbonTabs.md)

## Description

Returns the specified RibbonTab object from the collection.

## Syntax

RibbonTabs.**Item**( ***Index*** As Variant ) As [RibbonTab](../RibbonTab/RibbonTab.md)

## Property Value

This is a read only property whose value is a [RibbonTab](../RibbonTab/RibbonTab.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Input Variant value that specifies the RibbonTab to return. This can be either a numeric value indicating the index of the item in the collection or it can be a string indicating the RibbonTab name. If an out of range index or a name of a non-existent RibbonTab is provided, an error will occur. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create a ribbon panel in an existing tab](../../sample-programs/RibbonPanels_Add_Sample.md) | Demonstrates creating a new ribbon panel within an existing ribbon tab. |

## Version

Introduced in version 2010

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
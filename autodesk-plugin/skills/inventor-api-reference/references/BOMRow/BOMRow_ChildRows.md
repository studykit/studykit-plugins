# BOMRow.ChildRows Property

Parent Object: [BOMRow](../BOMRow/BOMRow.md)

## Description

Property that gets the BOMRowsEnumerator object containing the locally-stored rows under this BOMRow. This property will return Nothing for BOMRows in a parts-only view and if there are no sub-rows for this BOMRow.

## Syntax

BOMRow.**ChildRows**() As [BOMRowsEnumerator](../BOMRowsEnumerator/BOMRowsEnumerator.md)

## Property Value

This is a read only property whose value is a [BOMRowsEnumerator](../BOMRowsEnumerator/BOMRowsEnumerator.md).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Using the BOM APIs](../../sample-programs/BOM_Sample.md) | This sample demonstrates the Bill of Materials API functionality in assemblies. |

## Version

Introduced in version 11

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
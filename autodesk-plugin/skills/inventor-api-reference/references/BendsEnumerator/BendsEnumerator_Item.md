# BendsEnumerator.Item Property

Parent Object: [BendsEnumerator](../BendsEnumerator/BendsEnumerator.md)

## Description

Returns the specified Bend object from the collection.

## Syntax

BendsEnumerator.**Item**( ***Index*** As Variant ) As [Bend](../Bend/Bend.md)

## Property Value

This is a read only property whose value is a [Bend](../Bend/Bend.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Input Long or Face object that specifies the Bend object within the collection to return. Inputting a Long indicates the index of the Bend within the collection to return. When a Face object is input the Bend that contains that face is returned. If the index is out of range or the input face is not part of a bend this property will fail. |

## Version

Introduced in version 2010

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
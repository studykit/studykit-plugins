# SketchConstraints3DEnumerator.Item Property

Parent Object: [SketchConstraints3DEnumerator](../SketchConstraints3DEnumerator/SketchConstraints3DEnumerator.md)

## Description

Returns the specified SketchConstraint object from the collection.

## Syntax

SketchConstraints3DEnumerator.**Item**( ***Index*** As Long ) As Object

## Property Value

This is a read only property whose value is an Object.

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Long | Value that specifies the SketchConstraint to return. This can be either a numeric value indicating the index of the item in the collection or it can be a string indicating the constraint name. The name expected is the display name of the constraint. This is the name that is displayed to the user in the assembly browser. If an out of range index or a name of a non\-existent constraint name is provided, an error occurs. |

## Version

Introduced in version 6

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
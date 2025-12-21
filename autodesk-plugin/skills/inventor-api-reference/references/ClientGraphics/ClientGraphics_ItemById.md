# ClientGraphics.ItemById Property

Parent Object: [ClientGraphics](../ClientGraphics/ClientGraphics.md)

## Description

Returns the specified object from the collection.

## Syntax

ClientGraphics.**ItemById**( ***NodeId*** As Long ) As [GraphicsNode](../GraphicsNode/GraphicsNode.md)

## Property Value

This is a read only property whose value is a [GraphicsNode](../GraphicsNode/GraphicsNode.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| NodeId | Long | Input Long that specifies the ID of the within the this ClientGraphics object. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Client graphics texture-based color mapping](../../sample-programs/GraphicsColorMapper_Sample.md) | This test applies texture coordinates expressing distance from the origin to 'the triangle mesh of whatever Part you have open. It then creates either a discrete-band or continuous color mapper and allows you to adjust the values of the mapper to change the range of values that map to various colors. |

## Version

Introduced in version 5

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
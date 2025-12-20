# GraphicsNodeProxy.Copy Method

Parent Object: [GraphicsNodeProxy](../GraphicsNodeProxy/GraphicsNodeProxy.md)

## Description

Method that creates a copy of this . The copy has the same property values as the original, a duplicate of all of the graphics primitives, and the CustomRenderStyle has the same values. A new ID is generated for the copy.

## Syntax

GraphicsNodeProxy.**Copy**( ***Transformation*** As [Matrix](../Matrix/Matrix.md), ***NodeId*** As Long ) As [GraphicsNode](../GraphicsNode/GraphicsNode.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Transformation | [Matrix](../Matrix/Matrix.md) | Input that defines the transform for the copy. |
| NodeId | Long | Input Long that specifies the identifier for the newly created node. This id needs to be unique with respect to all other object in this ClientGraphics object. |

## Version

Introduced in version 2008

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
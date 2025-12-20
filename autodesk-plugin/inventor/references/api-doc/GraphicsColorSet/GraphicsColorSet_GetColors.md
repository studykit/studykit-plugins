# GraphicsColorSet.GetColors Method

Parent Object: [GraphicsColorSet](../GraphicsColorSet/GraphicsColorSet.md)

## Description

Method that gets all of the colors of the set.

## Syntax

GraphicsColorSet.**GetColors**( ***Colors***() As Byte )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Colors | Byte | Output array of bytes that contains the values of the colors. The array is a single dimension array containing sequential red, green, and blue values. If the array has been declared undimensioned, this method will redimension its size to be able to contain the complete set of colors. If the array has been dimensioned, it must be large enough to contain the entire set of colors or an error will occur. |

## Version

Introduced in version 5

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
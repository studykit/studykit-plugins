# GraphicsColorMapper.GetColors Method

Parent Object: [GraphicsColorMapper](../GraphicsColorMapper/GraphicsColorMapper.md)

## Description

Method that gets all of the colors in the map.

## Syntax

GraphicsColorMapper.**GetColors**( ***Colors***() As Byte )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Colors | Byte | Output array of bytes that contains the values of the colors. The array is a single dimension array containing sequential red, green, and blue values. If the array has been declared undimensioned, this method will redimension its size to be able to contain the complete set of colors. If the array has been dimensioned, it must be large enough to contain the entire set of colors or an error will occur. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Client graphics texture-based color mapping](../../sample-programs/GraphicsColorMapper_Sample.md) | This test applies texture coordinates expressing distance from the origin to 'the triangle mesh of whatever Part you have open. It then creates either a discrete-band or continuous color mapper and allows you to adjust the values of the mapper to change the range of values that map to various colors. |

## Version

Introduced in version 2010

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
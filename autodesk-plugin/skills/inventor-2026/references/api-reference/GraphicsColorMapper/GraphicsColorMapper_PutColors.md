# GraphicsColorMapper.PutColors Method

Parent Object: [GraphicsColorMapper](../GraphicsColorMapper/GraphicsColorMapper.md)

## Description

Method that sets all of the colors in the map. This will replace all existing colors currently defined for the map.

## Syntax

GraphicsColorMapper.**PutColors**( ***Colors***() As Byte )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Colors | Byte | Input array of Bytes that contains the values of the colors. The array is a single dimension array containing sequential red, green, and blue values. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Client graphics texture-based color mapping](../../sample-programs/GraphicsColorMapper_Sample.md) | This test applies texture coordinates expressing distance from the origin to 'the triangle mesh of whatever Part you have open. It then creates either a discrete-band or continuous color mapper and allows you to adjust the values of the mapper to change the range of values that map to various colors. |

## Version

Introduced in version 2010

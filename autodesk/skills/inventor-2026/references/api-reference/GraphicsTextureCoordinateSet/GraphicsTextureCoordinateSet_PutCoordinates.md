# GraphicsTextureCoordinateSet.PutCoordinates Method

Parent Object: [GraphicsTextureCoordinateSet](../GraphicsTextureCoordinateSet/GraphicsTextureCoordinateSet.md)

## Description

Method that sets all of the coordinates of the set. This will replace all existing coordinates currently defined for the set.

## Syntax

GraphicsTextureCoordinateSet.**PutCoordinates**( ***Coordinates***() As Double )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Coordinates | Double | Input array of doubles that contains value of the texture coordinates. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Client graphics texture-based color mapping](../../sample-programs/GraphicsColorMapper_Sample.md) | This test applies texture coordinates expressing distance from the origin to 'the triangle mesh of whatever Part you have open. It then creates either a discrete-band or continuous color mapper and allows you to adjust the values of the mapper to change the range of values that map to various colors. |

## Version

Introduced in version 2010

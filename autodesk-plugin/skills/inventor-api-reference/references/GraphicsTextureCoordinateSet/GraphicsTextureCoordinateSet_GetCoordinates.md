# GraphicsTextureCoordinateSet.GetCoordinates Method

Parent Object: [GraphicsTextureCoordinateSet](../GraphicsTextureCoordinateSet/GraphicsTextureCoordinateSet.md)

## Description

Method that gets all of the coordinates of the set.

## Syntax

GraphicsTextureCoordinateSet.**GetCoordinates**( ***Coordinates***() As Double )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Coordinates | Double | Output array of doubles that contains the scalar texture coordinates. The array is a single dimension array containing texture coordinates. If the array has been declared undimensioned, this method will redimension its size to contain the complete set of coordinates. If the array has been dimensioned, it must be large enough to contain the entire set of coordinates or an error will occur. |

## Version

Introduced in version 2010

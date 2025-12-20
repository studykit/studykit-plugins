# GraphicsTextureCoordinateSet Object

Derived from: [GraphicsDataSet](../GraphicsDataSet/GraphicsDataSet.md) Object

## Description

The GraphicsTextureCoordinateSet object contains a list of coordinate values

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Add](../GraphicsTextureCoordinateSet/GraphicsTextureCoordinateSet_Add.md) | Method that adds a single coordinate to the set. |
| [Delete](../GraphicsTextureCoordinateSet/GraphicsTextureCoordinateSet_Delete.md) | Method that deletes the GraphicsDataSet. |
| [GetCoordinates](../GraphicsTextureCoordinateSet/GraphicsTextureCoordinateSet_GetCoordinates.md) | Method that gets all of the coordinates of the set. |
| [PutCoordinates](../GraphicsTextureCoordinateSet/GraphicsTextureCoordinateSet_PutCoordinates.md) | Method that sets all of the coordinates of the set. This will replace all existing coordinates currently defined for the set. |
| [Remove](../GraphicsTextureCoordinateSet/GraphicsTextureCoordinateSet_Remove.md) | Method that removes a coordinate from the set. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Coordinate](../GraphicsTextureCoordinateSet/GraphicsTextureCoordinateSet_Coordinate.md) | Read-write property that gets and sets the value of a specific coordinate within the set. |
| [Count](../GraphicsTextureCoordinateSet/GraphicsTextureCoordinateSet_Count.md) | Property that returns the number of objects in this collection. |
| [Id](../GraphicsTextureCoordinateSet/GraphicsTextureCoordinateSet_Id.md) | Property returning the unique id of this GraphicsDataSet. |
| [TextureDimension](../GraphicsTextureCoordinateSet/GraphicsTextureCoordinateSet_TextureDimension.md) | Read-write property that defines the dimension of the texture coordinate array. |
| [Type](../GraphicsTextureCoordinateSet/GraphicsTextureCoordinateSet_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[GraphicsDataSets.CreateTextureCoordinateSet](../GraphicsDataSets/GraphicsDataSets_CreateTextureCoordinateSet.md), [TriangleFanGraphics.TextureCoordinateSet](../TriangleFanGraphics/TriangleFanGraphics_TextureCoordinateSet.md), [TriangleGraphics.TextureCoordinateSet](../TriangleGraphics/TriangleGraphics_TextureCoordinateSet.md), [TriangleStripGraphics.TextureCoordinateSet](../TriangleStripGraphics/TriangleStripGraphics_TextureCoordinateSet.md)

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
# GraphicsImageSet Object

Derived from: [GraphicsDataSet](../GraphicsDataSet/GraphicsDataSet.md) Object

## Description

The GraphicsImageSet defines images that can be used when displaying client graphics objects that support images. Currently this is limited to the GraphicsPoint object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Add](../GraphicsImageSet/GraphicsImageSet_Add.md) | Method that adds a new custom point to the set. |
| [Delete](../GraphicsImageSet/GraphicsImageSet_Delete.md) | Method that deletes the GraphicsDataSet. |
| [Remove](../GraphicsImageSet/GraphicsImageSet_Remove.md) | Method that removes a coordinate from the set. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Count](../GraphicsImageSet/GraphicsImageSet_Count.md) | Property that returns the number of objects in this collection. |
| [Id](../GraphicsImageSet/GraphicsImageSet_Id.md) | Property returning the unique id of this GraphicsDataSet. |
| [Type](../GraphicsImageSet/GraphicsImageSet_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[GraphicsDataSets.CreateImageSet](../GraphicsDataSets/GraphicsDataSets_CreateImageSet.md), [PointGraphics.GetCustomImage](../PointGraphics/PointGraphics_GetCustomImage.md), [TriangleGraphics.GetCustomImage](../TriangleGraphics/TriangleGraphics_GetCustomImage.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Client graphics - image in point graphics](../../sample-programs/PointGraphics_SetCustomImage_Sample.md) | The following sample demonstrates creation of point client graphics with a custom image. |

## Version

Introduced in version 2011

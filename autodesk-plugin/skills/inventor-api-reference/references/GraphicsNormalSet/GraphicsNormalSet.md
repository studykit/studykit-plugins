# GraphicsNormalSet Object

Derived from: [GraphicsDataSet](../GraphicsDataSet/GraphicsDataSet.md) Object

## Description

The GraphicsNormalSet object contains a list of normals. This object can be referenced by any number of graphic primitives to help define the normals to be used when rendering.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Add](../GraphicsNormalSet/GraphicsNormalSet_Add.md) | Method that adds a new normal to the set. |
| [Delete](../GraphicsNormalSet/GraphicsNormalSet_Delete.md) | Method that deletes the GraphicsDataSet. |
| [GetNormals](../GraphicsNormalSet/GraphicsNormalSet_GetNormals.md) | Method that gets all of the normals of the set. |
| [PutNormals](../GraphicsNormalSet/GraphicsNormalSet_PutNormals.md) | Method that sets all of the normals of the set. This will replace any existing normals currently defined for the set. |
| [Remove](../GraphicsNormalSet/GraphicsNormalSet_Remove.md) | Method that removes a coordinate from the set. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Count](../GraphicsNormalSet/GraphicsNormalSet_Count.md) | Property that returns the number of objects in this collection. |
| [Id](../GraphicsNormalSet/GraphicsNormalSet_Id.md) | Property returning the unique id of this GraphicsDataSet. |
| [Normal](../GraphicsNormalSet/GraphicsNormalSet_Normal.md) | Allows integer-indexed access to items in the collection. |
| [Type](../GraphicsNormalSet/GraphicsNormalSet_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[GraphicsDataSets.CreateNormalSet](../GraphicsDataSets/GraphicsDataSets_CreateNormalSet.md), [MeshFeatureEntity.NormalSet](../MeshFeatureEntity/MeshFeatureEntity_NormalSet.md), [MeshFeatureEntityProxy.NormalSet](../MeshFeatureEntityProxy/MeshFeatureEntityProxy_NormalSet.md), [PresentationMeshFeatureEntity.NormalSet](../PresentationMeshFeatureEntity/PresentationMeshFeatureEntity_NormalSet.md), [TriangleFanGraphics.NormalSet](../TriangleFanGraphics/TriangleFanGraphics_NormalSet.md), [TriangleGraphics.NormalSet](../TriangleGraphics/TriangleGraphics_NormalSet.md), [TriangleStripGraphics.NormalSet](../TriangleStripGraphics/TriangleStripGraphics_NormalSet.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Client graphics texture-based color mapping](../../sample-programs/GraphicsColorMapper_Sample.md) | This test applies texture coordinates expressing distance from the origin to 'the triangle mesh of whatever Part you have open. It then creates either a discrete-band or continuous color mapper and allows you to adjust the values of the mapper to change the range of values that map to various colors. |
| [Client Graphics - Vertex Color by Z Height](../../sample-programs/GraphicsDataSets_CreateColorSet_Sample.md) | This sample demonstrates using client graphics and some other functions that help to support display control. It uses the currently active part and replaces the part display with a display where the part's color varies from blue to red where blue is assigned to the lowest Z portion of the part and red is assigned to the highest Z portion of the part. Areas in between are represented by a smooth blend of color from blue to red. |
| [Client Graphics - Triangle](../../sample-programs/GraphicsNode_AddTriangleFanGraphics_Sample.md) | This sample demonstrates the creation of client graphics triangles using triange fans and strips. It does this by drawing a cylinder. The end caps are triangle fans and the cylinder is made from a triangle strip. |

## Version

Introduced in version 5

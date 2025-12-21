# GraphicsIndexSet Object

Derived from: [GraphicsDataSet](../GraphicsDataSet/GraphicsDataSet.md) Object

## Description

The GraphicsIndexSet object contains a list of indices. This object can be referenced by any number of graphic primitives to use in defining the list of indices that index into a coordinate set.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Add](../GraphicsIndexSet/GraphicsIndexSet_Add.md) | Method that adds a new index to the set. |
| [Delete](../GraphicsIndexSet/GraphicsIndexSet_Delete.md) | Method that deletes the GraphicsDataSet. |
| [GetIndices](../GraphicsIndexSet/GraphicsIndexSet_GetIndices.md) | Method that gets all of the indices of the set. |
| [PutIndices](../GraphicsIndexSet/GraphicsIndexSet_PutIndices.md) | Method that sets all of the indices of the set. This will replace any existing indices currently defined for the set. |
| [Remove](../GraphicsIndexSet/GraphicsIndexSet_Remove.md) | Method that removes a coordinate from the set. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Count](../GraphicsIndexSet/GraphicsIndexSet_Count.md) | Property that returns the number of objects in this collection. |
| [Id](../GraphicsIndexSet/GraphicsIndexSet_Id.md) | Property returning the unique id of this GraphicsDataSet. |
| [IndexValue](../GraphicsIndexSet/GraphicsIndexSet_IndexValue.md) | Allows integer-indexed access to items in the collection. |
| [Type](../GraphicsIndexSet/GraphicsIndexSet_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[GraphicsDataSets.CreateIndexSet](../GraphicsDataSets/GraphicsDataSets_CreateIndexSet.md), [LineGraphics.ColorIndexSet](../LineGraphics/LineGraphics_ColorIndexSet.md), [LineGraphics.CoordinateIndexSet](../LineGraphics/LineGraphics_CoordinateIndexSet.md), [LineStripGraphics.ColorIndexSet](../LineStripGraphics/LineStripGraphics_ColorIndexSet.md), [LineStripGraphics.CoordinateIndexSet](../LineStripGraphics/LineStripGraphics_CoordinateIndexSet.md), [MeshFeatureEntity.ColorIndexSet](../MeshFeatureEntity/MeshFeatureEntity_ColorIndexSet.md), [MeshFeatureEntity.CoordinateIndexSet](../MeshFeatureEntity/MeshFeatureEntity_CoordinateIndexSet.md), [MeshFeatureEntity.NormalIndexSet](../MeshFeatureEntity/MeshFeatureEntity_NormalIndexSet.md), [MeshFeatureEntityProxy.ColorIndexSet](../MeshFeatureEntityProxy/MeshFeatureEntityProxy_ColorIndexSet.md), [MeshFeatureEntityProxy.CoordinateIndexSet](../MeshFeatureEntityProxy/MeshFeatureEntityProxy_CoordinateIndexSet.md), [MeshFeatureEntityProxy.NormalIndexSet](../MeshFeatureEntityProxy/MeshFeatureEntityProxy_NormalIndexSet.md), [PointGraphics.CoordinateIndexSet](../PointGraphics/PointGraphics_CoordinateIndexSet.md), [PresentationMeshFeatureEntity.ColorIndexSet](../PresentationMeshFeatureEntity/PresentationMeshFeatureEntity_ColorIndexSet.md), [PresentationMeshFeatureEntity.CoordinateIndexSet](../PresentationMeshFeatureEntity/PresentationMeshFeatureEntity_CoordinateIndexSet.md), [PresentationMeshFeatureEntity.NormalIndexSet](../PresentationMeshFeatureEntity/PresentationMeshFeatureEntity_NormalIndexSet.md), [TriangleFanGraphics.ColorIndexSet](../TriangleFanGraphics/TriangleFanGraphics_ColorIndexSet.md), [TriangleFanGraphics.CoordinateIndexSet](../TriangleFanGraphics/TriangleFanGraphics_CoordinateIndexSet.md), [TriangleFanGraphics.NormalIndexSet](../TriangleFanGraphics/TriangleFanGraphics_NormalIndexSet.md), [TriangleFanGraphics.TextureCoordinateIndexSet](../TriangleFanGraphics/TriangleFanGraphics_TextureCoordinateIndexSet.md), [TriangleGraphics.ColorIndexSet](../TriangleGraphics/TriangleGraphics_ColorIndexSet.md), [TriangleGraphics.CoordinateIndexSet](../TriangleGraphics/TriangleGraphics_CoordinateIndexSet.md), [TriangleGraphics.NormalIndexSet](../TriangleGraphics/TriangleGraphics_NormalIndexSet.md), [TriangleGraphics.TextureCoordinateIndexSet](../TriangleGraphics/TriangleGraphics_TextureCoordinateIndexSet.md), [TriangleStripGraphics.ColorIndexSet](../TriangleStripGraphics/TriangleStripGraphics_ColorIndexSet.md), [TriangleStripGraphics.CoordinateIndexSet](../TriangleStripGraphics/TriangleStripGraphics_CoordinateIndexSet.md), [TriangleStripGraphics.NormalIndexSet](../TriangleStripGraphics/TriangleStripGraphics_NormalIndexSet.md), [TriangleStripGraphics.TextureCoordinateIndexSet](../TriangleStripGraphics/TriangleStripGraphics_TextureCoordinateIndexSet.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Client graphics texture-based color mapping](../../sample-programs/GraphicsColorMapper_Sample.md) | This test applies texture coordinates expressing distance from the origin to 'the triangle mesh of whatever Part you have open. It then creates either a discrete-band or continuous color mapper and allows you to adjust the values of the mapper to change the range of values that map to various colors. |
| [Client Graphics - Vertex Color by Z Height](../../sample-programs/GraphicsDataSets_CreateColorSet_Sample.md) | This sample demonstrates using client graphics and some other functions that help to support display control. It uses the currently active part and replaces the part display with a display where the part's color varies from blue to red where blue is assigned to the lowest Z portion of the part and red is assigned to the highest Z portion of the part. Areas in between are represented by a smooth blend of color from blue to red. |
| [Client Graphics - Triangle](../../sample-programs/GraphicsNode_AddTriangleFanGraphics_Sample.md) | This sample demonstrates the creation of client graphics triangles using triange fans and strips. It does this by drawing a cylinder. The end caps are triangle fans and the cylinder is made from a triangle strip. |

## Version

Introduced in version 5

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
# GraphicsDataSets.CreateNormalSet Method

Parent Object: [GraphicsDataSets](../GraphicsDataSets/GraphicsDataSets.md)

## Description

Method that creates a new GraphicsNormalSet object. You use methods provided by the NormalSet object to define the normal vectors.

## Syntax

GraphicsDataSets.**CreateNormalSet**( ***DataSetId*** As Long ) As [GraphicsNormalSet](../GraphicsNormalSet/GraphicsNormalSet.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| DataSetId | Long | Input Long that specifies the unique identifier for the GraphicsDataSet object. This must be unique with respect to all other GraphicsDataSet objects within this GraphicsDataSets object. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Client graphics texture-based color mapping](../../sample-programs/GraphicsColorMapper_Sample.md) | This test applies texture coordinates expressing distance from the origin to 'the triangle mesh of whatever Part you have open. It then creates either a discrete-band or continuous color mapper and allows you to adjust the values of the mapper to change the range of values that map to various colors. |
| [Client Graphics - Vertex Color by Z Height](../../sample-programs/GraphicsDataSets_CreateColorSet_Sample.md) | This sample demonstrates using client graphics and some other functions that help to support display control. It uses the currently active part and replaces the part display with a display where the part's color varies from blue to red where blue is assigned to the lowest Z portion of the part and red is assigned to the highest Z portion of the part. Areas in between are represented by a smooth blend of color from blue to red. |
| [Client Graphics - Triangle](../../sample-programs/GraphicsNode_AddTriangleFanGraphics_Sample.md) | This sample demonstrates the creation of client graphics triangles using triange fans and strips. It does this by drawing a cylinder. The end caps are triangle fans and the cylinder is made from a triangle strip. |

## Version

Introduced in version 5

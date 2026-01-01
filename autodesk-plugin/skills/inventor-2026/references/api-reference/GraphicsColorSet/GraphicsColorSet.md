# GraphicsColorSet Object

Derived from: [GraphicsDataSet](../GraphicsDataSet/GraphicsDataSet.md) Object

## Description

The GraphicsColorSet object contains a list of colors. This object can be referenced by any number of graphic primitives to use in defining triangle or vertex specific colors to use when rendering.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Add](../GraphicsColorSet/GraphicsColorSet_Add.md) | Method that adds a new color to the set. |
| [Delete](../GraphicsColorSet/GraphicsColorSet_Delete.md) | Method that deletes the GraphicsDataSet. |
| [GetColors](../GraphicsColorSet/GraphicsColorSet_GetColors.md) | Method that gets all of the colors of the set. |
| [PutColors](../GraphicsColorSet/GraphicsColorSet_PutColors.md) | Method that sets all of the colors of the set. This will replace all existing colors currently defined for the set. |
| [Remove](../GraphicsColorSet/GraphicsColorSet_Remove.md) | Method that removes a coordinate from the set. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Color](../GraphicsColorSet/GraphicsColorSet_Color.md) | Property that gets and sets the color at a given index in the set. |
| [Count](../GraphicsColorSet/GraphicsColorSet_Count.md) | Property that returns the number of objects in this collection. |
| [Id](../GraphicsColorSet/GraphicsColorSet_Id.md) | Property returning the unique id of this GraphicsDataSet. |
| [Type](../GraphicsColorSet/GraphicsColorSet_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[GraphicsDataSets.CreateColorSet](../GraphicsDataSets/GraphicsDataSets_CreateColorSet.md), [LineGraphics.ColorSet](../LineGraphics/LineGraphics_ColorSet.md), [LineStripGraphics.ColorSet](../LineStripGraphics/LineStripGraphics_ColorSet.md), [MeshFeatureEntity.ColorSet](../MeshFeatureEntity/MeshFeatureEntity_ColorSet.md), [MeshFeatureEntityProxy.ColorSet](../MeshFeatureEntityProxy/MeshFeatureEntityProxy_ColorSet.md), [PresentationMeshFeatureEntity.ColorSet](../PresentationMeshFeatureEntity/PresentationMeshFeatureEntity_ColorSet.md), [TriangleFanGraphics.ColorSet](../TriangleFanGraphics/TriangleFanGraphics_ColorSet.md), [TriangleGraphics.ColorSet](../TriangleGraphics/TriangleGraphics_ColorSet.md), [TriangleStripGraphics.ColorSet](../TriangleStripGraphics/TriangleStripGraphics_ColorSet.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Client graphics texture-based color mapping](../../sample-programs/GraphicsColorMapper_Sample.md) | This test applies texture coordinates expressing distance from the origin to 'the triangle mesh of whatever Part you have open. It then creates either a discrete-band or continuous color mapper and allows you to adjust the values of the mapper to change the range of values that map to various colors. |
| [Client Graphics - Vertex Color by Z Height](../../sample-programs/GraphicsDataSets_CreateColorSet_Sample.md) | This sample demonstrates using client graphics and some other functions that help to support display control. It uses the currently active part and replaces the part display with a display where the part's color varies from blue to red where blue is assigned to the lowest Z portion of the part and red is assigned to the highest Z portion of the part. Areas in between are represented by a smooth blend of color from blue to red. |
| [Client Graphics - Line](../../sample-programs/GraphicsNode_AddLineGraphics_Sample.md) | This sample demonstrates the creation of custom graphics using LineGraphics and LineStripGraphics. The same set of coordinate data is used for both types of graphics. Line graphics use two coordinates to define a line, and then the next two coordinates to define the next line, and so on through the defined coordinates. For the data provided, this results in gaps in the drawn curve. Line strips use the first two coordinates to define the first line and then the last point of the first line becomes the first point of the second line and the next coordinate is used as the end point of the second line. This results in the set of points being connected by a continuous set of lines, drawing a continuous curve. This sample also demonstrates two methods of defining the color for client graphics. In one case it uses an existing appearance asset, and in the other, it explicitly defines a color and assigns it. To use the sample you need to have an assembly or part document open. The program has two behaviors: the first time it is run it will draw the graphics. The second time it is run it deletes the previously drawn graphics. |

## Version

Introduced in version 5

# GraphicsDataSets.CreateColorSet Method

Parent Object: [GraphicsDataSets](../GraphicsDataSets/GraphicsDataSets.md)

## Description

Method that creates a new GraphicsColorSet object. You use methods provided by the ColorSet object to define the colors.

## Syntax

GraphicsDataSets.**CreateColorSet**( ***DataSetId*** As Long ) As [GraphicsColorSet](../GraphicsColorSet/GraphicsColorSet.md)

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
| [Client Graphics - Line](../../sample-programs/GraphicsNode_AddLineGraphics_Sample.md) | This sample demonstrates the creation of custom graphics using LineGraphics and LineStripGraphics. The same set of coordinate data is used for both types of graphics. Line graphics use two coordinates to define a line, and then the next two coordinates to define the next line, and so on through the defined coordinates. For the data provided, this results in gaps in the drawn curve. Line strips use the first two coordinates to define the first line and then the last point of the first line becomes the first point of the second line and the next coordinate is used as the end point of the second line. This results in the set of points being connected by a continuous set of lines, drawing a continuous curve. This sample also demonstrates two methods of defining the color for client graphics. In one case it uses an existing appearance asset, and in the other, it explicitly defines a color and assigns it. To use the sample you need to have an assembly or part document open. The program has two behaviors: the first time it is run it will draw the graphics. The second time it is run it deletes the previously drawn graphics. |
| [InteractionGraphics](../../sample-programs/InteractionGraphics_Sample.md) | The sample creates overlay graphics. |

## Version

Introduced in version 5

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
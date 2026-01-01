# GraphicsNode.Transformation Property

Parent Object: [GraphicsNode](../GraphicsNode/GraphicsNode.md)

## Description

Property that gets and sets the transformation of the GraphicsNode.

## Syntax

GraphicsNode.**Transformation**() As [Matrix](../Matrix/Matrix.md)

## Property Value

This is a read/write property whose value is a [Matrix](../Matrix/Matrix.md).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Client Graphics - Line](../../sample-programs/GraphicsNode_AddLineGraphics_Sample.md) | This sample demonstrates the creation of custom graphics using LineGraphics and LineStripGraphics. The same set of coordinate data is used for both types of graphics. Line graphics use two coordinates to define a line, and then the next two coordinates to define the next line, and so on through the defined coordinates. For the data provided, this results in gaps in the drawn curve. Line strips use the first two coordinates to define the first line and then the last point of the first line becomes the first point of the second line and the next coordinate is used as the end point of the second line. This results in the set of points being connected by a continuous set of lines, drawing a continuous curve. This sample also demonstrates two methods of defining the color for client graphics. In one case it uses an existing appearance asset, and in the other, it explicitly defines a color and assigns it. To use the sample you need to have an assembly or part document open. The program has two behaviors: the first time it is run it will draw the graphics. The second time it is run it deletes the previously drawn graphics. |
| [InteractionGraphics](../../sample-programs/InteractionGraphics_Sample.md) | The sample creates overlay graphics. |

## Version

Introduced in version 5

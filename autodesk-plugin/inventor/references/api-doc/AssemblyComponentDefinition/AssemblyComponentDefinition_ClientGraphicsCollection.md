# AssemblyComponentDefinition.ClientGraphicsCollection Property

Parent Object: [AssemblyComponentDefinition](../AssemblyComponentDefinition/AssemblyComponentDefinition.md)

## Description

Property that returns the ClientGraphicsCollection object.

## Syntax

AssemblyComponentDefinition.**ClientGraphicsCollection**() As [ClientGraphicsCollection](../ClientGraphicsCollection/ClientGraphicsCollection.md)

## Property Value

This is a read only property whose value is a [ClientGraphicsCollection](../ClientGraphicsCollection/ClientGraphicsCollection.md).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Client Graphics - Line](../../sample-programs/GraphicsNode_AddLineGraphics_Sample.md) | This sample demonstrates the creation of custom graphics using LineGraphics and LineStripGraphics. The same set of coordinate data is used for both types of graphics. Line graphics use two coordinates to define a line, and then the next two coordinates to define the next line, and so on through the defined coordinates. For the data provided, this results in gaps in the drawn curve. Line strips use the first two coordinates to define the first line and then the last point of the first line becomes the first point of the second line and the next coordinate is used as the end point of the second line. This results in the set of points being connected by a continuous set of lines, drawing a continuous curve. This sample also demonstrates two methods of defining the color for client graphics. In one case it uses an existing appearance asset, and in the other, it explicitly defines a color and assigns it. To use the sample you need to have an assembly or part document open. The program has two behaviors: the first time it is run it will draw the graphics. The second time it is run it deletes the previously drawn graphics. |
| [Text Using Client Graphics (Simple)](../../sample-programs/GraphicsNode_AddTextGraphics_Sample.md) | This sample demonstrates creating text using client graphics. It illustrates the simple case where the text is one font and is one line. |
| [Text Using Client Graphics (Multiple fonts and lines)](../../sample-programs/GraphicsNode_AddTextGraphics2_Sample.md) | This sample demonstrates creating text using client graphics. It illustrates the more complex case of changes in font and more than one line. |
| [Client Graphics - Triangle](../../sample-programs/GraphicsNode_AddTriangleFanGraphics_Sample.md) | This sample demonstrates the creation of client graphics triangles using triange fans and strips. It does this by drawing a cylinder. The end caps are triangle fans and the cylinder is made from a triangle strip. |

## Version

Introduced in version 5

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
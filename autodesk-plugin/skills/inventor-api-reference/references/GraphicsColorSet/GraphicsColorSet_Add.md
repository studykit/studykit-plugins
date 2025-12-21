# GraphicsColorSet.Add Method

Parent Object: [GraphicsColorSet](../GraphicsColorSet/GraphicsColorSet.md)

## Description

Method that adds a new color to the set.

## Syntax

GraphicsColorSet.**Add**( ***Index*** As Long, ***Red*** As Byte, ***Green*** As Byte, ***Blue*** As Byte )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Long | Input Long value that specifies the index of the object to return. |
| Red | Byte | Input value that specifies the red component of the color. This must be a value between 0 and 255. |
| Green | Byte | Input Byte that specifies the green component of the color. This value must be between 0 and 255. |
| Blue | Byte | The blue component of the color. A Byte value between 0 and 255. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Client Graphics - Line](../../sample-programs/GraphicsNode_AddLineGraphics_Sample.md) | This sample demonstrates the creation of custom graphics using LineGraphics and LineStripGraphics. The same set of coordinate data is used for both types of graphics. Line graphics use two coordinates to define a line, and then the next two coordinates to define the next line, and so on through the defined coordinates. For the data provided, this results in gaps in the drawn curve. Line strips use the first two coordinates to define the first line and then the last point of the first line becomes the first point of the second line and the next coordinate is used as the end point of the second line. This results in the set of points being connected by a continuous set of lines, drawing a continuous curve. This sample also demonstrates two methods of defining the color for client graphics. In one case it uses an existing appearance asset, and in the other, it explicitly defines a color and assigns it. To use the sample you need to have an assembly or part document open. The program has two behaviors: the first time it is run it will draw the graphics. The second time it is run it deletes the previously drawn graphics. |
| [InteractionGraphics](../../sample-programs/InteractionGraphics_Sample.md) | The sample creates overlay graphics. |

## Version

Introduced in version 5

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
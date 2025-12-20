# GraphicsDataSetsCollection.Add Method

Parent Object: [GraphicsDataSetsCollection](../GraphicsDataSetsCollection/GraphicsDataSetsCollection.md)

## Description

Method that creates a new GraphicsDataSets object. When the GraphicsDataSetsCollection object is obtained from a Document, this will always create a transient graphics data object. That is, its lifetime is only for the period of time the document is open.When the GraphicsDataSetsCollection object is obtained from a ClientFeatureDefinition object, the graphics data objects created are persistent and will be saved with the document. In that case it is only intended to be used for graphics that are associated with a client feature.

## Syntax

GraphicsDataSetsCollection.**Add**( ***ClientId*** As String ) As [GraphicsDataSets](../GraphicsDataSets/GraphicsDataSets.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| ClientId | String | Specifies the unique identifier for the GraphicsDataSets object. This must be unique with respect to all other GraphicsDataSets objects. Typically, this is a GUID in string form, but any string is valid. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Client Graphics - Draw Range Box](../../sample-programs/ClientGraphics_Sample.md) | This sample demonstrates the use of client graphics to draw the range box of selected entities. |
| [Client Graphics - Vertex Color by Z Height](../../sample-programs/GraphicsDataSets_CreateColorSet_Sample.md) | This sample demonstrates using client graphics and some other functions that help to support display control. It uses the currently active part and replaces the part display with a display where the part's color varies from blue to red where blue is assigned to the lowest Z portion of the part and red is assigned to the highest Z portion of the part. Areas in between are represented by a smooth blend of color from blue to red. |
| [Client Graphics - Line](../../sample-programs/GraphicsNode_AddLineGraphics_Sample.md) | This sample demonstrates the creation of custom graphics using LineGraphics and LineStripGraphics. The same set of coordinate data is used for both types of graphics. Line graphics use two coordinates to define a line, and then the next two coordinates to define the next line, and so on through the defined coordinates. For the data provided, this results in gaps in the drawn curve. Line strips use the first two coordinates to define the first line and then the last point of the first line becomes the first point of the second line and the next coordinate is used as the end point of the second line. This results in the set of points being connected by a continuous set of lines, drawing a continuous curve. This sample also demonstrates two methods of defining the color for client graphics. In one case it uses an existing appearance asset, and in the other, it explicitly defines a color and assigns it. To use the sample you need to have an assembly or part document open. The program has two behaviors: the first time it is run it will draw the graphics. The second time it is run it deletes the previously drawn graphics. |
| [Client Graphics - Triangle](../../sample-programs/GraphicsNode_AddTriangleFanGraphics_Sample.md) | This sample demonstrates the creation of client graphics triangles using triange fans and strips. It does this by drawing a cylinder. The end caps are triangle fans and the cylinder is made from a triangle strip. |
| [Client graphics - image in point graphics](../../sample-programs/PointGraphics_SetCustomImage_Sample.md) | The following sample demonstrates creation of point client graphics with a custom image. |

## Version

Introduced in version 5

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
# ClientGraphicsCollection.Item Property

Parent Object: [ClientGraphicsCollection](../ClientGraphicsCollection/ClientGraphicsCollection.md)

## Description

Returns an existing ClientGraphics object.

## Syntax

ClientGraphicsCollection.**Item**( ***Index*** As Variant ) As [ClientGraphics](../ClientGraphics/ClientGraphics.md)

## Property Value

This is a read only property whose value is a [ClientGraphics](../ClientGraphics/ClientGraphics.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Specifies which objects to return. This can be an integer, which specifies the index in the collection, or it can be a string, which specifies the Client ID of the object. The property will fail in the case where an Index is provided that does not identify an existing ClientGraphics object. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Client Graphics - Vertex Color by Z Height](../../sample-programs/GraphicsDataSets_CreateColorSet_Sample.md) | This sample demonstrates using client graphics and some other functions that help to support display control. It uses the currently active part and replaces the part display with a display where the part's color varies from blue to red where blue is assigned to the lowest Z portion of the part and red is assigned to the highest Z portion of the part. Areas in between are represented by a smooth blend of color from blue to red. |
| [Client Graphics - Line](../../sample-programs/GraphicsNode_AddLineGraphics_Sample.md) | This sample demonstrates the creation of custom graphics using LineGraphics and LineStripGraphics. The same set of coordinate data is used for both types of graphics. Line graphics use two coordinates to define a line, and then the next two coordinates to define the next line, and so on through the defined coordinates. For the data provided, this results in gaps in the drawn curve. Line strips use the first two coordinates to define the first line and then the last point of the first line becomes the first point of the second line and the next coordinate is used as the end point of the second line. This results in the set of points being connected by a continuous set of lines, drawing a continuous curve. This sample also demonstrates two methods of defining the color for client graphics. In one case it uses an existing appearance asset, and in the other, it explicitly defines a color and assigns it. To use the sample you need to have an assembly or part document open. The program has two behaviors: the first time it is run it will draw the graphics. The second time it is run it deletes the previously drawn graphics. |
| [Text Using Client Graphics (Simple)](../../sample-programs/GraphicsNode_AddTextGraphics_Sample.md) | This sample demonstrates creating text using client graphics. It illustrates the simple case where the text is one font and is one line. |
| [Text Using Client Graphics (Multiple fonts and lines)](../../sample-programs/GraphicsNode_AddTextGraphics2_Sample.md) | This sample demonstrates creating text using client graphics. It illustrates the more complex case of changes in font and more than one line. |
| [Client Graphics - Triangle](../../sample-programs/GraphicsNode_AddTriangleFanGraphics_Sample.md) | This sample demonstrates the creation of client graphics triangles using triange fans and strips. It does this by drawing a cylinder. The end caps are triangle fans and the cylinder is made from a triangle strip. |
| [3D Curve from Parametric Curve](../../sample-programs/ParameterCurveTo3D_Sample.md) | Demonstrates the conversion of a 2d parameteric space curve into the equivalent 3d model space curve. To use this sample you must have a part open. You can select any face and 3D curves will be drawn on the face using client graphics. |
| [Client graphics - image in point graphics](../../sample-programs/PointGraphics_SetCustomImage_Sample.md) | The following sample demonstrates creation of point client graphics with a custom image. |
| [Client graphics creation of 3D primitives](../../sample-programs/TransientBRep_CreateSolidCylinderCone_Sample.md) | This sample demonstrates the creation of 3D primitives (cylinder, cone, etc.) using client graphics. |
| [Create curve primitives](../../sample-programs/TransientGeometry_Sample.md) | This sample demonstrates the creation of curve primitives (lines, arcs, circles, etc.) using client graphics. |

## Version

Introduced in version 5

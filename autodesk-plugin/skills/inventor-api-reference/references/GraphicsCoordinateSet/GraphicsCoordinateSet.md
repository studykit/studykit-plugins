# GraphicsCoordinateSet Object

Derived from: [GraphicsDataSet](../GraphicsDataSet/GraphicsDataSet.md) Object

## Description

The GraphicsCoordinateSet object contains a list of coordinate values. This object can be referenced by any number of graphic primitives to use in defining their coordinates.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Add](../GraphicsCoordinateSet/GraphicsCoordinateSet_Add.md) | Method that adds a single coordinate to the set. |
| [Delete](../GraphicsCoordinateSet/GraphicsCoordinateSet_Delete.md) | Method that deletes the GraphicsDataSet. |
| [GetCoordinates](../GraphicsCoordinateSet/GraphicsCoordinateSet_GetCoordinates.md) | Method that gets all of the coordinates of the set. |
| [PutCoordinates](../GraphicsCoordinateSet/GraphicsCoordinateSet_PutCoordinates.md) | Method that sets all of the coordinates of the set. This will replace all existing coordinates currently defined for the set. |
| [Remove](../GraphicsCoordinateSet/GraphicsCoordinateSet_Remove.md) | Method that removes a coordinate from the set. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Coordinate](../GraphicsCoordinateSet/GraphicsCoordinateSet_Coordinate.md) | Allows integer-indexed access to items in the collection. |
| [Count](../GraphicsCoordinateSet/GraphicsCoordinateSet_Count.md) | Property that returns the number of objects in this collection. |
| [Id](../GraphicsCoordinateSet/GraphicsCoordinateSet_Id.md) | Property returning the unique id of this GraphicsDataSet. |
| [Type](../GraphicsCoordinateSet/GraphicsCoordinateSet_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[GraphicsDataSets.CreateCoordinateSet](../GraphicsDataSets/GraphicsDataSets_CreateCoordinateSet.md), [LineGraphics.CoordinateSet](../LineGraphics/LineGraphics_CoordinateSet.md), [LineStripGraphics.CoordinateSet](../LineStripGraphics/LineStripGraphics_CoordinateSet.md), [MeshFeatureEntity.CoordinateSet](../MeshFeatureEntity/MeshFeatureEntity_CoordinateSet.md), [MeshFeatureEntityProxy.CoordinateSet](../MeshFeatureEntityProxy/MeshFeatureEntityProxy_CoordinateSet.md), [PointGraphics.CoordinateSet](../PointGraphics/PointGraphics_CoordinateSet.md), [PresentationMeshFeatureEntity.CoordinateSet](../PresentationMeshFeatureEntity/PresentationMeshFeatureEntity_CoordinateSet.md), [TriangleFanGraphics.CoordinateSet](../TriangleFanGraphics/TriangleFanGraphics_CoordinateSet.md), [TriangleGraphics.CoordinateSet](../TriangleGraphics/TriangleGraphics_CoordinateSet.md), [TriangleStripGraphics.CoordinateSet](../TriangleStripGraphics/TriangleStripGraphics_CoordinateSet.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Client Graphics - Draw Range Box](../../sample-programs/ClientGraphics_Sample.md) | This sample demonstrates the use of client graphics to draw the range box of selected entities. |
| [Client graphics texture-based color mapping](../../sample-programs/GraphicsColorMapper_Sample.md) | This test applies texture coordinates expressing distance from the origin to 'the triangle mesh of whatever Part you have open. It then creates either a discrete-band or continuous color mapper and allows you to adjust the values of the mapper to change the range of values that map to various colors. |
| [Client Graphics - Vertex Color by Z Height](../../sample-programs/GraphicsDataSets_CreateColorSet_Sample.md) | This sample demonstrates using client graphics and some other functions that help to support display control. It uses the currently active part and replaces the part display with a display where the part's color varies from blue to red where blue is assigned to the lowest Z portion of the part and red is assigned to the highest Z portion of the part. Areas in between are represented by a smooth blend of color from blue to red. |
| [Client Graphics - Line](../../sample-programs/GraphicsNode_AddLineGraphics_Sample.md) | This sample demonstrates the creation of custom graphics using LineGraphics and LineStripGraphics. The same set of coordinate data is used for both types of graphics. Line graphics use two coordinates to define a line, and then the next two coordinates to define the next line, and so on through the defined coordinates. For the data provided, this results in gaps in the drawn curve. Line strips use the first two coordinates to define the first line and then the last point of the first line becomes the first point of the second line and the next coordinate is used as the end point of the second line. This results in the set of points being connected by a continuous set of lines, drawing a continuous curve. This sample also demonstrates two methods of defining the color for client graphics. In one case it uses an existing appearance asset, and in the other, it explicitly defines a color and assigns it. To use the sample you need to have an assembly or part document open. The program has two behaviors: the first time it is run it will draw the graphics. The second time it is run it deletes the previously drawn graphics. |
| [Client Graphics - Triangle](../../sample-programs/GraphicsNode_AddTriangleFanGraphics_Sample.md) | This sample demonstrates the creation of client graphics triangles using triange fans and strips. It does this by drawing a cylinder. The end caps are triangle fans and the cylinder is made from a triangle strip. |
| [Client graphics - image in point graphics](../../sample-programs/PointGraphics_SetCustomImage_Sample.md) | The following sample demonstrates creation of point client graphics with a custom image. |
| [OnDrag Event - dragging a WorkPoint](../../sample-programs/UserInputEventsSink_OnDrag_Sample.md) | This sample demonstrates the use of the OnDrag event to drag fixed work points when no command is active. This sample only allows drags parallel to the X-Y plane. This sample is dependent on events and VB only supports events within a class module. |

## Version

Introduced in version 5

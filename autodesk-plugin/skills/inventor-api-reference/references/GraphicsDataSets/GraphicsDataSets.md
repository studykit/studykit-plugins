# GraphicsDataSets Object

## Description

The GrahicsDataSets object supports methods to create the various graphics-related data objects.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [CreateColorMapper](../GraphicsDataSets/GraphicsDataSets_CreateColorMapper.md) | Method that creates a new GraphicsColorMapper object. |
| [CreateColorSet](../GraphicsDataSets/GraphicsDataSets_CreateColorSet.md) | Method that creates a new GraphicsColorSet object. You use methods provided by the ColorSet object to define the colors. |
| [CreateCoordinateSet](../GraphicsDataSets/GraphicsDataSets_CreateCoordinateSet.md) | Method that creates a new GraphicsCoordinateSet object. You use methods provided by the CoordinateSet object to define the coordinates. |
| [CreateImageSet](../GraphicsDataSets/GraphicsDataSets_CreateImageSet.md) | Method that creates a new GraphicsImageSet object. You use methods provided by the GraphicsImageSet object to define the images. |
| [CreateIndexSet](../GraphicsDataSets/GraphicsDataSets_CreateIndexSet.md) | Method that creates a new GraphicsIndexSet object. You use methods provided by the GraphicsIndexSet object to define the indices. |
| [CreateNormalSet](../GraphicsDataSets/GraphicsDataSets_CreateNormalSet.md) | Method that creates a new GraphicsNormalSet object. You use methods provided by the NormalSet object to define the normal vectors. |
| [CreateTextureCoordinateSet](../GraphicsDataSets/GraphicsDataSets_CreateTextureCoordinateSet.md) | Method that creates a new GraphicsTextureCoordinateSet object. You use methods provided by the GraphicsTextureCoordinateSet object to define the coordinates. |
| [Delete](../GraphicsDataSets/GraphicsDataSets_Delete.md) | Method that deletes the GraphicsDataSets object. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../GraphicsDataSets/GraphicsDataSets_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [ClientId](../GraphicsDataSets/GraphicsDataSets_ClientId.md) | Property that returns the unique identifier for the GraphicsDataSets object. The ClientId is assigned during the creation of the GraphicsDataSets object. Typically, it is a GUID in string form, but any string is valid. |
| [Count](../GraphicsDataSets/GraphicsDataSets_Count.md) | Property that returns the number of GraphicDataSet objects in this collection. |
| [Item](../GraphicsDataSets/GraphicsDataSets_Item.md) | Returns the specified object from the collection. |
| [ItemById](../GraphicsDataSets/GraphicsDataSets_ItemById.md) | Returns the specified object from the collection. |
| [NonTransacting](../GraphicsDataSets/GraphicsDataSets_NonTransacting.md) | Read-only property that returns whether the creation of this GraphicsDataSets object and all its associated data is non-transacting. |
| [Parent](../GraphicsDataSets/GraphicsDataSets_Parent.md) | Property returns the parent of this object. |
| [SaveWithDocument](../GraphicsDataSets/GraphicsDataSets_SaveWithDocument.md) | Property that returns whether to save the GraphicsDataSets with the document. |
| [Type](../GraphicsDataSets/GraphicsDataSets_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[GraphicsDataSetsCollection.Add](../GraphicsDataSetsCollection/GraphicsDataSetsCollection_Add.md), [GraphicsDataSetsCollection.Item](../GraphicsDataSetsCollection/GraphicsDataSetsCollection_Item.md), [InteractionGraphics.GraphicsDataSets](../InteractionGraphics/InteractionGraphics_GraphicsDataSets.md)

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

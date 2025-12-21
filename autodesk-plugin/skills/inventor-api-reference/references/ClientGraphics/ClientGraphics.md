# ClientGraphics Object

## Description

The ClientGraphics object is a collection of objects.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [AddNode](../ClientGraphics/ClientGraphics_AddNode.md) | Method that creates a new GraphicsNode object. |
| [Delete](../ClientGraphics/ClientGraphics_Delete.md) | Method that deletes this ClientGraphics object. This will delete all of its associated GraphicsNode objects too. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../ClientGraphics/ClientGraphics_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [ClientId](../ClientGraphics/ClientGraphics_ClientId.md) | Property that returns the ID of this ClientGraphics object. |
| [Count](../ClientGraphics/ClientGraphics_Count.md) | Property that returns the number of GraphicsNode objects associated with this ClientGraphics object. |
| [Item](../ClientGraphics/ClientGraphics_Item.md) | Returns the specified object from the collection. |
| [ItemById](../ClientGraphics/ClientGraphics_ItemById.md) | Returns the specified object from the collection. |
| [NonTransacting](../ClientGraphics/ClientGraphics_NonTransacting.md) | Read-only property that returns whether the creation of this ClientGraphics object and all its associated data is non-transacting. |
| [Parent](../ClientGraphics/ClientGraphics_Parent.md) | Property returns the logical parent of this object. |
| [RangeBox](../ClientGraphics/ClientGraphics_RangeBox.md) | Property that returns a Box object which contains the opposing points of a rectangular box that is guaranteed to enclose this object. |
| [Selectable](../ClientGraphics/ClientGraphics_Selectable.md) | Property that gets and sets whether all of the GraphicsNode objects within the ClientGraphics object are selectable. When getting this property valid values are kAllGraphicsSelectable, kNoGraphicsSelectable, and kSomeGraphicsSelectable. When setting this property kAllGraphicsSelectable and kNoGraphicsSelectable are valid. |
| [Type](../ClientGraphics/ClientGraphics_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [Visible](../ClientGraphics/ClientGraphics_Visible.md) | Property that gets and sets whether all of the GraphicsNode objects within the ClientGraphics object are visible. When getting this property valid values are kAllGraphicsVisible, kNoGraphicsVisible, and kSomeGraphicsVisible. When setting this property kAllGraphicsVisible and kNoGraphicsVisible are valid. |

## Accessed From

[ClientGraphicsCollection.Add](../ClientGraphicsCollection/ClientGraphicsCollection_Add.md), [ClientGraphicsCollection.Item](../ClientGraphicsCollection/ClientGraphicsCollection_Item.md), [GraphicsNode.Parent](../GraphicsNode/GraphicsNode_Parent.md), [GraphicsNodeProxy.Parent](../GraphicsNodeProxy/GraphicsNodeProxy_Parent.md), [InteractionGraphics.OverlayClientGraphics](../InteractionGraphics/InteractionGraphics_OverlayClientGraphics.md), [InteractionGraphics.PreviewClientGraphics](../InteractionGraphics/InteractionGraphics_PreviewClientGraphics.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Client Graphics - Draw Range Box](../../sample-programs/ClientGraphics_Sample.md) | This sample demonstrates the use of client graphics to draw the range box of selected entities. |
| [Client graphics texture-based color mapping](../../sample-programs/GraphicsColorMapper_Sample.md) | This test applies texture coordinates expressing distance from the origin to 'the triangle mesh of whatever Part you have open. It then creates either a discrete-band or continuous color mapper and allows you to adjust the values of the mapper to change the range of values that map to various colors. |
| [Client Graphics - Vertex Color by Z Height](../../sample-programs/GraphicsDataSets_CreateColorSet_Sample.md) | This sample demonstrates using client graphics and some other functions that help to support display control. It uses the currently active part and replaces the part display with a display where the part's color varies from blue to red where blue is assigned to the lowest Z portion of the part and red is assigned to the highest Z portion of the part. Areas in between are represented by a smooth blend of color from blue to red. |
| [Client Graphics - Line](../../sample-programs/GraphicsNode_AddLineGraphics_Sample.md) | This sample demonstrates the creation of custom graphics using LineGraphics and LineStripGraphics. The same set of coordinate data is used for both types of graphics. Line graphics use two coordinates to define a line, and then the next two coordinates to define the next line, and so on through the defined coordinates. For the data provided, this results in gaps in the drawn curve. Line strips use the first two coordinates to define the first line and then the last point of the first line becomes the first point of the second line and the next coordinate is used as the end point of the second line. This results in the set of points being connected by a continuous set of lines, drawing a continuous curve. This sample also demonstrates two methods of defining the color for client graphics. In one case it uses an existing appearance asset, and in the other, it explicitly defines a color and assigns it. To use the sample you need to have an assembly or part document open. The program has two behaviors: the first time it is run it will draw the graphics. The second time it is run it deletes the previously drawn graphics. |
| [Client graphics from SAT file body](../../sample-programs/GraphicsNode_AddSurfaceGraphics_Sample.md) | The following sample demonstrates how to display client graphics based on bodies read in from a SAT file. |
| [Text Using Client Graphics (Simple)](../../sample-programs/GraphicsNode_AddTextGraphics_Sample.md) | This sample demonstrates creating text using client graphics. It illustrates the simple case where the text is one font and is one line. |
| [Text Using Client Graphics (Multiple fonts and lines)](../../sample-programs/GraphicsNode_AddTextGraphics2_Sample.md) | This sample demonstrates creating text using client graphics. It illustrates the more complex case of changes in font and more than one line. |
| [Client Graphics - Triangle](../../sample-programs/GraphicsNode_AddTriangleFanGraphics_Sample.md) | This sample demonstrates the creation of client graphics triangles using triange fans and strips. It does this by drawing a cylinder. The end caps are triangle fans and the cylinder is made from a triangle strip. |
| [3D Curve from Parametric Curve](../../sample-programs/ParameterCurveTo3D_Sample.md) | Demonstrates the conversion of a 2d parameteric space curve into the equivalent 3d model space curve. To use this sample you must have a part open. You can select any face and 3D curves will be drawn on the face using client graphics. |
| [Client graphics - image in point graphics](../../sample-programs/PointGraphics_SetCustomImage_Sample.md) | The following sample demonstrates creation of point client graphics with a custom image. |
| [Selection of Surface Graphics Primitives](../../sample-programs/SelectSurfaceGraphicsPrimitives_Sample.md) | This demonstrates the ability to select client graphic primitives, by creating SurfaceGraphics and showing how you can select B-Rep entities within the graphics. You must have a part or assembly open and select a part of sat file which will be read in and displayed as client graphics. Depending on our responses to the program it will create the graphics so that only the node is selectable (which is all that was supported before), so that all of the primitives are selected, or so that only certain primitives are selectable (every other face in this case). |
| [Transient solid body creation](../../sample-programs/SurfaceBodyDefinition_CreateTransientSurfaceBody_Sample.md) | The following sample demonstrates the creation of a transient solid block body. The newly created body is then displayed using client graphics in a part. |
| [Client graphics creation of 3D primitives](../../sample-programs/TransientBRep_CreateSolidCylinderCone_Sample.md) | This sample demonstrates the creation of 3D primitives (cylinder, cone, etc.) using client graphics. |
| [Create curve primitives](../../sample-programs/TransientGeometry_Sample.md) | This sample demonstrates the creation of curve primitives (lines, arcs, circles, etc.) using client graphics. |
| [OnDrag Event - dragging a WorkPoint](../../sample-programs/UserInputEventsSink_OnDrag_Sample.md) | This sample demonstrates the use of the OnDrag event to drag fixed work points when no command is active. This sample only allows drags parallel to the X-Y plane. This sample is dependent on events and VB only supports events within a class module. |

## Version

Introduced in version 5

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
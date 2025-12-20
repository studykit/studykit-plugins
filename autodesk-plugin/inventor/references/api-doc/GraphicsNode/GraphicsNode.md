# GraphicsNode Object

## Description

The GraphicsNode object provides a logical grouping of Client graphics. It is the lowest level of detail the user will see when selecting objects.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [AddComponentGraphics](../GraphicsNode/GraphicsNode_AddComponentGraphics.md) | Method that creates a new ComponentGraphics object based on the input ComponentDefinition. |
| [AddCurveGraphics](../GraphicsNode/GraphicsNode_AddCurveGraphics.md) | Method that creates a new CurveGraphics graphic primitive. |
| [AddLineGraphics](../GraphicsNode/GraphicsNode_AddLineGraphics.md) | Method that creates a new LineGraphics graphic primitive. |
| [AddLineStripGraphics](../GraphicsNode/GraphicsNode_AddLineStripGraphics.md) | Method that creates a new LineStripGraphics graphic primitive. |
| [AddPointGraphics](../GraphicsNode/GraphicsNode_AddPointGraphics.md) | Method that creates a new PointGraphics graphic primitive. |
| [AddScalableTextGraphics](../GraphicsNode/GraphicsNode_AddScalableTextGraphics.md) | Method that creates a new (scalable) TextGraphics graphic primitive. |
| [AddSurfaceGraphics](../GraphicsNode/GraphicsNode_AddSurfaceGraphics.md) | Method that creates a new SurfaceGraphics object based on the input surface(s). |
| [AddTextGraphics](../GraphicsNode/GraphicsNode_AddTextGraphics.md) | Method that creates a new TextGraphics graphic primitive. |
| [AddTriangleFanGraphics](../GraphicsNode/GraphicsNode_AddTriangleFanGraphics.md) | Method that creates a new TriangleFanGraphics graphic primitive. |
| [AddTriangleGraphics](../GraphicsNode/GraphicsNode_AddTriangleGraphics.md) | Method that creates a new TriangleGraphics graphic primitive. |
| [AddTriangleStripGraphics](../GraphicsNode/GraphicsNode_AddTriangleStripGraphics.md) | Method that creates a new TriangleStripGraphics graphic primitive. |
| [ClearSlice](../GraphicsNode/GraphicsNode_ClearSlice.md) | Method that clears all the slicing applied to the graphics node. |
| [Copy](../GraphicsNode/GraphicsNode_Copy.md) | Method that creates a copy of this . The copy has the same property values as the original, a duplicate of all of the graphics primitives, and the CustomRenderStyle has the same values. A new ID is generated for the copy. |
| [Delete](../GraphicsNode/GraphicsNode_Delete.md) | Method that deletes the GraphicsNode. This also deletes all associated graphic primitives. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [AllowSliceCapping](../GraphicsNode/GraphicsNode_AllowSliceCapping.md) | Specifies that whether this graphics node will display a cap or not when sliced. |
| [AllowSlicing](../GraphicsNode/GraphicsNode_AllowSlicing.md) | Specifies that the node participates in slicing of client graphics. |
| [Appearance](../GraphicsNode/GraphicsNode_Appearance.md) | Gets and sets the appearance asset associated with the graphics node. |
| [Application](../GraphicsNode/GraphicsNode_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Count](../GraphicsNode/GraphicsNode_Count.md) | Property that returns the number of graphic primitive objects associated with this GraphicsNode object. |
| [DisplayName](../GraphicsNode/GraphicsNode_DisplayName.md) | Read-write Property that gets and sets display name of this graphics node. |
| [ExcludedFromViewAll](../GraphicsNode/GraphicsNode_ExcludedFromViewAll.md) | Specifies that the node is not considered when doing a view all. |
| [Id](../GraphicsNode/GraphicsNode_Id.md) | Property that returns the Id of the GraphicsNode. |
| [IsTransparentInPlaceEdit](../GraphicsNode/GraphicsNode_IsTransparentInPlaceEdit.md) | Read-write Property that gets and sets transparency behavior of this graphics node in inactive mode. |
| [Item](../GraphicsNode/GraphicsNode_Item.md) | Returns the specified graphic entity from the collection. |
| [ItemById](../GraphicsNode/GraphicsNode_ItemById.md) | Returns the specified GraphicsPrimitive from the collection using its Id as index. |
| [OverrideOpacity](../GraphicsNode/GraphicsNode_OverrideOpacity.md) | Override Opacity that controls the transparencty of the node. |
| [Parent](../GraphicsNode/GraphicsNode_Parent.md) | Property that returns the object this graphics node belongs to. |
| [RangeBox](../GraphicsNode/GraphicsNode_RangeBox.md) | Property that returns a Box object which contains the opposing points of a rectangular box that is guaranteed to enclose this object. |
| [Selectable](../GraphicsNode/GraphicsNode_Selectable.md) | Property that specifies whether the GraphicsNode object can be selected when the Select command is running in Inventor. |
| [Transformation](../GraphicsNode/GraphicsNode_Transformation.md) | Property that gets and sets the transformation of the GraphicsNode. |
| [Type](../GraphicsNode/GraphicsNode_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [Visible](../GraphicsNode/GraphicsNode_Visible.md) | Read-write property that gets and sets whether the GraphicsNode is visible or not. |
| [VisibleInActiveEditObject](../GraphicsNode/GraphicsNode_VisibleInActiveEditObject.md) | Read-write property that gets and sets whether this graphics node is visible when the containing object is not the active edit object. A value of True indicates that this node is visible only when the containing object is activated. The value of this property is ignored if the Visible property on GraphicsNode is False. |
| [VisibleInViews](../GraphicsNode/GraphicsNode_VisibleInViews.md) | Property that returns a object containing the Views that this graphics node is visible in. If there are no views in the list, the node is visible in all views. Views may be added or removed from the list. This property is ignored if the Visible property on GraphicsNode is False. |

## Accessed From

[ClientGraphics.AddNode](../ClientGraphics/ClientGraphics_AddNode.md), [ClientGraphics.Item](../ClientGraphics/ClientGraphics_Item.md), [ClientGraphics.ItemById](../ClientGraphics/ClientGraphics_ItemById.md), [ComponentGraphics.Parent](../ComponentGraphics/ComponentGraphics_Parent.md), [CurveGraphics.Parent](../CurveGraphics/CurveGraphics_Parent.md), [FeatureGraphics.Parent](FeatureGraphics_Parent.md), [GraphicsNode.Copy](../GraphicsNode/GraphicsNode_Copy.md), [GraphicsNodeProxy.Copy](../GraphicsNodeProxy/GraphicsNodeProxy_Copy.md), [GraphicsNodeProxy.NativeObject](../GraphicsNodeProxy/GraphicsNodeProxy_NativeObject.md), [GraphicsPrimitive.Parent](../GraphicsPrimitive/GraphicsPrimitive_Parent.md), [LineGraphics.Parent](../LineGraphics/LineGraphics_Parent.md), [LineStripGraphics.Parent](../LineStripGraphics/LineStripGraphics_Parent.md), [PointGraphics.Parent](../PointGraphics/PointGraphics_Parent.md), [SurfaceGraphics.Parent](../SurfaceGraphics/SurfaceGraphics_Parent.md), [SweepGraphics.Parent](SweepGraphics_Parent.md), [TextGraphics.Parent](../TextGraphics/TextGraphics_Parent.md), [TriangleFanGraphics.Parent](../TriangleFanGraphics/TriangleFanGraphics_Parent.md), [TriangleGraphics.Parent](../TriangleGraphics/TriangleGraphics_Parent.md), [TriangleStripGraphics.Parent](../TriangleStripGraphics/TriangleStripGraphics_Parent.md)

## Derived Classes

[GraphicsNodeProxy](../GraphicsNodeProxy/GraphicsNodeProxy.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Client Graphics - Draw Range Box](../../sample-programs/ClientGraphics_Sample.md) | This sample demonstrates the use of client graphics to draw the range box of selected entities. |
| [Client graphics texture-based color mapping](../../sample-programs/GraphicsColorMapper_Sample.md) | This test applies texture coordinates expressing distance from the origin to 'the triangle mesh of whatever Part you have open. It then creates either a discrete-band or continuous color mapper and allows you to adjust the values of the mapper to change the range of values that map to various colors. |
| [Client Graphics - Vertex Color by Z Height](../../sample-programs/GraphicsDataSets_CreateColorSet_Sample.md) | This sample demonstrates using client graphics and some other functions that help to support display control. It uses the currently active part and replaces the part display with a display where the part's color varies from blue to red where blue is assigned to the lowest Z portion of the part and red is assigned to the highest Z portion of the part. Areas in between are represented by a smooth blend of color from blue to red. |
| [Client Graphics - Line](../../sample-programs/GraphicsNode_AddLineGraphics_Sample.md) | This sample demonstrates the creation of custom graphics using LineGraphics and LineStripGraphics. The same set of coordinate data is used for both types of graphics. Line graphics use two coordinates to define a line, and then the next two coordinates to define the next line, and so on through the defined coordinates. For the data provided, this results in gaps in the drawn curve. Line strips use the first two coordinates to define the first line and then the last point of the first line becomes the first point of the second line and the next coordinate is used as the end point of the second line. This results in the set of points being connected by a continuous set of lines, drawing a continuous curve. This sample also demonstrates two methods of defining the color for client graphics. In one case it uses an existing appearance asset, and in the other, it explicitly defines a color and assigns it. To use the sample you need to have an assembly or part document open. The program has two behaviors: the first time it is run it will draw the graphics. The second time it is run it deletes the previously drawn graphics. |
| [Client graphics from SAT file body](../../sample-programs/GraphicsNode_AddSurfaceGraphics_Sample.md) | The following sample demonstrates how to display client graphics based on bodies read in from a SAT file. |
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
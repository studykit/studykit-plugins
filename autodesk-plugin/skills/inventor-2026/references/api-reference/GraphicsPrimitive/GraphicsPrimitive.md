# GraphicsPrimitive Object

## Description

The GraphicsPrimitive object is the base class for all the various primitive types of client graphics.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../GraphicsPrimitive/GraphicsPrimitive_Delete.md) | Method that deletes the graphics primitive. |
| [GetViewSpaceAnchor](../GraphicsPrimitive/GraphicsPrimitive_GetViewSpaceAnchor.md) | Method that gets the anchor information of the graphics object. This method returns an error if the 'Anchored' property returns False. |
| [RemoveViewSpaceAnchor](../GraphicsPrimitive/GraphicsPrimitive_RemoveViewSpaceAnchor.md) | The RemoveViewSpaceAnchor method removes the view space anchor from the object, and sets the Anchored property to false. |
| [SetViewSpaceAnchor](../GraphicsPrimitive/GraphicsPrimitive_SetViewSpaceAnchor.md) | Method that anchors the graphics object at the specified point in view space. The Anchored property is set to True. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Anchored](../GraphicsPrimitive/GraphicsPrimitive_Anchored.md) | Property that indicates whether this graphics primitive is anchored in view space. This property can only be set to False. The Anchored property is automatically set to True by the SetViewSpaceAnchor method. |
| [Application](../GraphicsPrimitive/GraphicsPrimitive_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Id](../GraphicsPrimitive/GraphicsPrimitive_Id.md) | Read-only property that returns the Id of the object. |
| [Parent](../GraphicsPrimitive/GraphicsPrimitive_Parent.md) | Property that returns the parent object from whom this object can logically be reached. |
| [RangeBox](../GraphicsPrimitive/GraphicsPrimitive_RangeBox.md) | Property that returns a Box object which contains the opposing points of a rectangular box that is guaranteed to enclose this object. |
| [Type](../GraphicsPrimitive/GraphicsPrimitive_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[GraphicsNode.Item](../GraphicsNode/GraphicsNode_Item.md), [GraphicsNode.ItemById](../GraphicsNode/GraphicsNode_ItemById.md), [GraphicsNodeProxy.Item](../GraphicsNodeProxy/GraphicsNodeProxy_Item.md), [GraphicsNodeProxy.ItemById](../GraphicsNodeProxy/GraphicsNodeProxy_ItemById.md)

## Derived Classes

[ComponentGraphics](../ComponentGraphics/ComponentGraphics.md), [CurveGraphics](../CurveGraphics/CurveGraphics.md), [LineGraphics](../LineGraphics/LineGraphics.md), [LineStripGraphics](../LineStripGraphics/LineStripGraphics.md), [PointGraphics](../PointGraphics/PointGraphics.md), [SurfaceGraphics](../SurfaceGraphics/SurfaceGraphics.md), [TextGraphics](../TextGraphics/TextGraphics.md), [TriangleFanGraphics](../TriangleFanGraphics/TriangleFanGraphics.md), [TriangleGraphics](../TriangleGraphics/TriangleGraphics.md), [TriangleStripGraphics](../TriangleStripGraphics/TriangleStripGraphics.md)

## Version

Introduced in version 5

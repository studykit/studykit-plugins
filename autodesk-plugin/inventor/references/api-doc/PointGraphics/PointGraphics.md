# PointGraphics Object

Derived from: [GraphicsPrimitive](../GraphicsPrimitive/GraphicsPrimitive.md) Object

## Description

The PointGraphics object defines a set of points. Each coordinate provided defines a point.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../PointGraphics/PointGraphics_Delete.md) | Method that deletes the graphics primitive. |
| [GetCustomImage](../PointGraphics/PointGraphics_GetCustomImage.md) | Method that gets the image used for this PointGraphics object. This is only valid in the case where the PointRenderStyle property returns kCustomImagePointStyle, otherwise this method will fail. |
| [GetViewSpaceAnchor](../PointGraphics/PointGraphics_GetViewSpaceAnchor.md) | Method that gets the anchor information of the graphics object. This method returns an error if the 'Anchored' property returns False. |
| [RemoveViewSpaceAnchor](../PointGraphics/PointGraphics_RemoveViewSpaceAnchor.md) | The RemoveViewSpaceAnchor method removes the view space anchor from the object, and sets the Anchored property to false. |
| [SetCustomImage](../PointGraphics/PointGraphics_SetCustomImage.md) | Method that sets the custom image to use for this PointGraphics object. This is cause the PointerRenderStyleProperty to return kCustomImagePointStyle. You can remove the custom image by setting the PointRenderStyle to one of the predefined point types. |
| [SetViewSpaceAnchor](../PointGraphics/PointGraphics_SetViewSpaceAnchor.md) | Method that anchors the graphics object at the specified point in view space. The Anchored property is set to True. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Anchored](../PointGraphics/PointGraphics_Anchored.md) | Property that indicates whether this graphics primitive is anchored in view space. This property can only be set to False. The Anchored property is automatically set to True by the SetViewSpaceAnchor method. |
| [Application](../PointGraphics/PointGraphics_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [BurnThrough](../PointGraphics/PointGraphics_BurnThrough.md) | Read-write property that specifies whether or not graphics are always visible even if they are blocked by other objects. |
| [CoordinateIndexSet](../PointGraphics/PointGraphics_CoordinateIndexSet.md) | Gets and sets the GraphicsIndexSet that defines indices within the coordinate set to use for the point of the set. |
| [CoordinateSet](../PointGraphics/PointGraphics_CoordinateSet.md) | Gets and sets the GraphicsCoordinateSet associate with set. |
| [DepthPriority](../PointGraphics/PointGraphics_DepthPriority.md) | Read-write property that allows you specify a priority to a set. |
| [Id](../PointGraphics/PointGraphics_Id.md) | Read-only property that returns the Id of the object. |
| [Parent](../PointGraphics/PointGraphics_Parent.md) | Property that returns the parent object from whom this object can logically be reached. |
| [PointRenderStyle](../PointGraphics/PointGraphics_PointRenderStyle.md) | Gets and sets the point style associated with the PointGraphics object. |
| [RangeBox](../PointGraphics/PointGraphics_RangeBox.md) | Property that returns a Box object which contains the opposing points of a rectangular box that is guaranteed to enclose this object. |
| [Type](../PointGraphics/PointGraphics_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[GraphicsNode.AddPointGraphics](../GraphicsNode/GraphicsNode_AddPointGraphics.md), [GraphicsNodeProxy.AddPointGraphics](../GraphicsNodeProxy/GraphicsNodeProxy_AddPointGraphics.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Client graphics - image in point graphics](../../sample-programs/PointGraphics_SetCustomImage_Sample.md) | The following sample demonstrates creation of point client graphics with a custom image. |
| [OnDrag Event - dragging a WorkPoint](../../sample-programs/UserInputEventsSink_OnDrag_Sample.md) | This sample demonstrates the use of the OnDrag event to drag fixed work points when no command is active. This sample only allows drags parallel to the X-Y plane. This sample is dependent on events and VB only supports events within a class module. |

## Version

Introduced in version 5

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
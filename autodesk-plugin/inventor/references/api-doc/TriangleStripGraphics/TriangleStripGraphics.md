# TriangleStripGraphics Object

Derived from: [GraphicsPrimitive](../GraphicsPrimitive/GraphicsPrimitive.md) Object

## Description

The TriangleStripGraphics object defines a set of connected triangles. The first three coordinates define a triangle and the next coordinate defines another triangle using the previous two coordinates.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../TriangleStripGraphics/TriangleStripGraphics_Delete.md) | Method that deletes the graphics primitive. |
| [GetStripLengths](../TriangleStripGraphics/TriangleStripGraphics_GetStripLengths.md) | Method that returns the current strip lengths. The strip lengths are defined by the number of coordinates used for each strip. |
| [GetTransformBehavior](../TriangleStripGraphics/TriangleStripGraphics_GetTransformBehavior.md) | Returns the current view transformation settings (e.g. pixel scaling and front facing). |
| [GetViewSpaceAnchor](../TriangleStripGraphics/TriangleStripGraphics_GetViewSpaceAnchor.md) | Method that gets the anchor information of the graphics object. This method returns an error if the 'Anchored' property returns False. |
| [PutStripLengths](../TriangleStripGraphics/TriangleStripGraphics_PutStripLengths.md) | Method that sets the current strip lengths. The strip lengths are defined by the number of coordinates used for each strip. |
| [RemoveViewSpaceAnchor](../TriangleStripGraphics/TriangleStripGraphics_RemoveViewSpaceAnchor.md) | The RemoveViewSpaceAnchor method removes the view space anchor from the object, and sets the Anchored property to false. |
| [SetTransformBehavior](../TriangleStripGraphics/TriangleStripGraphics_SetTransformBehavior.md) | Sets the view transformation settings (e.g. pixel scaling and front facing). |
| [SetViewSpaceAnchor](../TriangleStripGraphics/TriangleStripGraphics_SetViewSpaceAnchor.md) | Method that anchors the graphics object at the specified point in view space. The Anchored property is set to True. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Anchored](../TriangleStripGraphics/TriangleStripGraphics_Anchored.md) | Property that indicates whether this graphics primitive is anchored in view space. This property can only be set to False. The Anchored property is automatically set to True by the SetViewSpaceAnchor method. |
| [Application](../TriangleStripGraphics/TriangleStripGraphics_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [BackFaceCulling](../TriangleStripGraphics/TriangleStripGraphics_BackFaceCulling.md) | Gets and sets how the back face culling are defined for the triangles. |
| [BurnThrough](../TriangleStripGraphics/TriangleStripGraphics_BurnThrough.md) | Read-write property that specifies whether or not graphics are always visible even if they are blocked by other object. |
| [ColorBinding](../TriangleStripGraphics/TriangleStripGraphics_ColorBinding.md) | Gets and sets how the colors are defined for the triangle. |
| [ColorIndexSet](../TriangleStripGraphics/TriangleStripGraphics_ColorIndexSet.md) | Gets and sets the GraphicsIndexSet that defines the indices within the GraphicsColorSet to use. |
| [ColorMapper](../TriangleStripGraphics/TriangleStripGraphics_ColorMapper.md) | Read-write property that gets and sets the GraphicsColorMapper object associated with the set. |
| [ColorSet](../TriangleStripGraphics/TriangleStripGraphics_ColorSet.md) | Gets and sets the GraphicsColorSet associated with the set. |
| [CoordinateIndexSet](../TriangleStripGraphics/TriangleStripGraphics_CoordinateIndexSet.md) | Get and sets the GraphicsIndexSet that defines the indices within the coordinate set to use for the triangles of the set. |
| [CoordinateSet](../TriangleStripGraphics/TriangleStripGraphics_CoordinateSet.md) | Gets and sets the GraphicsCoordinateSet associated with the set. |
| [DepthPriority](../TriangleStripGraphics/TriangleStripGraphics_DepthPriority.md) | Read-write property that allows you to specify a priority to a set. |
| [Id](../TriangleStripGraphics/TriangleStripGraphics_Id.md) | Read-only property that returns the Id of the object. |
| [NormalBinding](../TriangleStripGraphics/TriangleStripGraphics_NormalBinding.md) | Gets and sets how the normals are defined for the triangles. |
| [NormalIndexSet](../TriangleStripGraphics/TriangleStripGraphics_NormalIndexSet.md) | Gets and sets the GraphicsIndexSet that defines the indices within the normal set to use for the triangles of the set. |
| [NormalSet](../TriangleStripGraphics/TriangleStripGraphics_NormalSet.md) | Gets and sets the GraphicsNormalSet associated with the set. |
| [Parent](../TriangleStripGraphics/TriangleStripGraphics_Parent.md) | Property that returns the parent object from whom this object can logically be reached. |
| [RangeBox](../TriangleStripGraphics/TriangleStripGraphics_RangeBox.md) | Property that returns a Box object which contains the opposing points of a rectangular box that is guaranteed to enclose this object. |
| [TextureCoordinateIndexSet](../TriangleStripGraphics/TriangleStripGraphics_TextureCoordinateIndexSet.md) | Read-write property that gets and sets the GraphicsCoordinateIndexSet that defines the indices within the texture coordinate set to use for the triangles of the set. |
| [TextureCoordinateSet](../TriangleStripGraphics/TriangleStripGraphics_TextureCoordinateSet.md) | Read-write property that gets and sets the GraphicsCoordinateSet associated with the set. |
| [Type](../TriangleStripGraphics/TriangleStripGraphics_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[GraphicsNode.AddTriangleStripGraphics](../GraphicsNode/GraphicsNode_AddTriangleStripGraphics.md), [GraphicsNodeProxy.AddTriangleStripGraphics](../GraphicsNodeProxy/GraphicsNodeProxy_AddTriangleStripGraphics.md)

## Version

Introduced in version 5

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
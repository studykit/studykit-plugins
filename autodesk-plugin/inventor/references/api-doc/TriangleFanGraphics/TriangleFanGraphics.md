# TriangleFanGraphics Object

Derived from: [GraphicsPrimitive](../GraphicsPrimitive/GraphicsPrimitive.md) Object

## Description

The TriangleFanGraphics object defines a set of connected triangles. The first three coordinates define a triangle and the next coordinate defines another triangle using two previous coordinates.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../TriangleFanGraphics/TriangleFanGraphics_Delete.md) | Method that deletes the graphics primitive. |
| [GetStripLengths](../TriangleFanGraphics/TriangleFanGraphics_GetStripLengths.md) | Method that returns the current strip lengths. The strip lengths are defined by the number of coordinates used for each strip. |
| [GetTransformBehavior](../TriangleFanGraphics/TriangleFanGraphics_GetTransformBehavior.md) | Returns the current view transformation settings (e.g. pixel scaling and front facing). |
| [GetViewSpaceAnchor](../TriangleFanGraphics/TriangleFanGraphics_GetViewSpaceAnchor.md) | Method that gets the anchor information of the graphics object. This method returns an error if the 'Anchored' property returns False. |
| [PutStripLengths](../TriangleFanGraphics/TriangleFanGraphics_PutStripLengths.md) | Method that sets the current strip lengths. The strip lengths are defined by the number of coordinates used for each strip. |
| [RemoveViewSpaceAnchor](../TriangleFanGraphics/TriangleFanGraphics_RemoveViewSpaceAnchor.md) | The RemoveViewSpaceAnchor method removes the view space anchor from the object, and sets the Anchored property to false. |
| [SetTransformBehavior](../TriangleFanGraphics/TriangleFanGraphics_SetTransformBehavior.md) | Sets the view transformation settings (e.g. pixel scaling and front facing). |
| [SetViewSpaceAnchor](../TriangleFanGraphics/TriangleFanGraphics_SetViewSpaceAnchor.md) | Method that anchors the graphics object at the specified point in view space. The Anchored property is set to True. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Anchored](../TriangleFanGraphics/TriangleFanGraphics_Anchored.md) | Property that indicates whether this graphics primitive is anchored in view space. This property can only be set to False. The Anchored property is automatically set to True by the SetViewSpaceAnchor method. |
| [Application](../TriangleFanGraphics/TriangleFanGraphics_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [BackFaceCulling](../TriangleFanGraphics/TriangleFanGraphics_BackFaceCulling.md) | Gets and sets how the back face culling are defined for the triangles. |
| [BurnThrough](../TriangleFanGraphics/TriangleFanGraphics_BurnThrough.md) | Read-write property that specifies whether or not graphics are always visible even if they are blocked by other object. |
| [ColorBinding](../TriangleFanGraphics/TriangleFanGraphics_ColorBinding.md) | Gets and sets how the colors are defined for the triangle. |
| [ColorIndexSet](../TriangleFanGraphics/TriangleFanGraphics_ColorIndexSet.md) | Gets and sets the GraphicsIndexSet that defines the indices within the GraphicsColorSet to use. |
| [ColorMapper](../TriangleFanGraphics/TriangleFanGraphics_ColorMapper.md) | Read-write property that gets and sets the GraphicsColorMapper object associated with the set. |
| [ColorSet](../TriangleFanGraphics/TriangleFanGraphics_ColorSet.md) | Gets and sets the GraphicsColorSet associated with the set. |
| [CoordinateIndexSet](../TriangleFanGraphics/TriangleFanGraphics_CoordinateIndexSet.md) | Get and sets the GraphicsIndexSet that defines the indices within the coordinate set to use for the triangles of the set. |
| [CoordinateSet](../TriangleFanGraphics/TriangleFanGraphics_CoordinateSet.md) | Gets and sets the GraphicsCoordinateSet associated with the set. |
| [DepthPriority](../TriangleFanGraphics/TriangleFanGraphics_DepthPriority.md) | Read-write property that allows you to specify a priority to a set. |
| [Id](../TriangleFanGraphics/TriangleFanGraphics_Id.md) | Read-only property that returns the Id of the object. |
| [NormalBinding](../TriangleFanGraphics/TriangleFanGraphics_NormalBinding.md) | Gets and sets how the normals are defined for the triangles. |
| [NormalIndexSet](../TriangleFanGraphics/TriangleFanGraphics_NormalIndexSet.md) | Gets and sets the GraphicsIndexSet that defines the indices within the normal set to use for the triangles of the set. |
| [NormalSet](../TriangleFanGraphics/TriangleFanGraphics_NormalSet.md) | Gets and sets the GraphicsNormalSet associated with the set. |
| [Parent](../TriangleFanGraphics/TriangleFanGraphics_Parent.md) | Property that returns the parent object from whom this object can logically be reached. |
| [RangeBox](../TriangleFanGraphics/TriangleFanGraphics_RangeBox.md) | Property that returns a Box object which contains the opposing points of a rectangular box that is guaranteed to enclose this object. |
| [TextureCoordinateIndexSet](../TriangleFanGraphics/TriangleFanGraphics_TextureCoordinateIndexSet.md) | Read-write property that gets and sets the GraphicsCoordinateIndexSet that defines the indices within the texture coordinate set to use for the triangles of the set. |
| [TextureCoordinateSet](../TriangleFanGraphics/TriangleFanGraphics_TextureCoordinateSet.md) | Read-write property that gets and sets the GraphicsCoordinateSet associated with the set. |
| [Type](../TriangleFanGraphics/TriangleFanGraphics_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[GraphicsNode.AddTriangleFanGraphics](../GraphicsNode/GraphicsNode_AddTriangleFanGraphics.md), [GraphicsNodeProxy.AddTriangleFanGraphics](../GraphicsNodeProxy/GraphicsNodeProxy_AddTriangleFanGraphics.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Client Graphics - Triangle](../../sample-programs/GraphicsNode_AddTriangleFanGraphics_Sample.md) | This sample demonstrates the creation of client graphics triangles using triange fans and strips. It does this by drawing a cylinder. The end caps are triangle fans and the cylinder is made from a triangle strip. |

## Version

Introduced in version 5

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
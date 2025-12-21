# TriangleGraphics Object

Derived from: [GraphicsPrimitive](../GraphicsPrimitive/GraphicsPrimitive.md) Object

## Description

The TriangleGraphics object defines a set of disconnected triangles. Each set of three coordinates defines a triangle.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../TriangleGraphics/TriangleGraphics_Delete.md) | Method that deletes the graphics primitive. |
| [GetCustomImage](../TriangleGraphics/TriangleGraphics_GetCustomImage.md) | Method that gets the image used for this TriangleGraphics object. |
| [GetTransformBehavior](../TriangleGraphics/TriangleGraphics_GetTransformBehavior.md) | Returns the current view transformation settings (e.g. pixel scaling and front facing). |
| [GetViewSpaceAnchor](../TriangleGraphics/TriangleGraphics_GetViewSpaceAnchor.md) | Method that gets the anchor information of the graphics object. This method returns an error if the 'Anchored' property returns False. |
| [RemoveViewSpaceAnchor](../TriangleGraphics/TriangleGraphics_RemoveViewSpaceAnchor.md) | The RemoveViewSpaceAnchor method removes the view space anchor from the object, and sets the Anchored property to false. |
| [SetCustomImage](../TriangleGraphics/TriangleGraphics_SetCustomImage.md) | Method that sets the custom image to use for this TriangleGraphics object. |
| [SetTransformBehavior](../TriangleGraphics/TriangleGraphics_SetTransformBehavior.md) | Sets the view transformation settings (e.g. pixel scaling and front facing). |
| [SetViewSpaceAnchor](../TriangleGraphics/TriangleGraphics_SetViewSpaceAnchor.md) | Method that anchors the graphics object at the specified point in view space. The Anchored property is set to True. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Anchored](../TriangleGraphics/TriangleGraphics_Anchored.md) | Property that indicates whether this graphics primitive is anchored in view space. This property can only be set to False. The Anchored property is automatically set to True by the SetViewSpaceAnchor method. |
| [Application](../TriangleGraphics/TriangleGraphics_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [BackFaceCulling](../TriangleGraphics/TriangleGraphics_BackFaceCulling.md) | Gets and sets how the back face culling are defined for the triangles. |
| [BurnThrough](../TriangleGraphics/TriangleGraphics_BurnThrough.md) | Read-write property that specifies whether or not graphics are always visible even if they are blocked by other object. |
| [ColorBinding](../TriangleGraphics/TriangleGraphics_ColorBinding.md) | Gets and sets how the colors are defined for the triangle. |
| [ColorIndexSet](../TriangleGraphics/TriangleGraphics_ColorIndexSet.md) | Gets and sets the GraphicsIndexSet that defines the indices within the GraphicsColorSet to use. |
| [ColorMapper](../TriangleGraphics/TriangleGraphics_ColorMapper.md) | Read-write property that gets and sets the GraphicsColorMapper object associated with the set. |
| [ColorSet](../TriangleGraphics/TriangleGraphics_ColorSet.md) | Gets and sets the GraphicsColorSet associated with the set. |
| [CoordinateIndexSet](../TriangleGraphics/TriangleGraphics_CoordinateIndexSet.md) | Get and sets the GraphicsIndexSet that defines the indices within the coordinate set to use for the triangles of the set. |
| [CoordinateSet](../TriangleGraphics/TriangleGraphics_CoordinateSet.md) | Gets and sets the GraphicsCoordinateSet associated with the set. |
| [DepthPriority](../TriangleGraphics/TriangleGraphics_DepthPriority.md) | Read-write property that allows you to specify a priority to a set. |
| [HasCustomImage](../TriangleGraphics/TriangleGraphics_HasCustomImage.md) | Read-write property that gets and sets whether a custom image is set for this TriangleGraphics object. |
| [Id](../TriangleGraphics/TriangleGraphics_Id.md) | Read-only property that returns the Id of the object. |
| [NormalBinding](../TriangleGraphics/TriangleGraphics_NormalBinding.md) | Gets and sets how the normals are defined for the triangles. |
| [NormalIndexSet](../TriangleGraphics/TriangleGraphics_NormalIndexSet.md) | Gets and sets the GraphicsIndexSet that defines the indices within the normal set to use for the triangles of the set. |
| [NormalSet](../TriangleGraphics/TriangleGraphics_NormalSet.md) | Gets and sets the GraphicsNormalSet associated with the set. |
| [Parent](../TriangleGraphics/TriangleGraphics_Parent.md) | Property that returns the parent object from whom this object can logically be reached. |
| [RangeBox](../TriangleGraphics/TriangleGraphics_RangeBox.md) | Property that returns a Box object which contains the opposing points of a rectangular box that is guaranteed to enclose this object. |
| [TextureCoordinateIndexSet](../TriangleGraphics/TriangleGraphics_TextureCoordinateIndexSet.md) | Read-write property that gets and sets the GraphicsCoordinateIndexSet that defines the indices within the texture coordinate set to use for the triangles of the set. |
| [TextureCoordinateSet](../TriangleGraphics/TriangleGraphics_TextureCoordinateSet.md) | Read-write property that gets and sets the GraphicsCoordinateSet associated with the set. |
| [Type](../TriangleGraphics/TriangleGraphics_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[GraphicsNode.AddTriangleGraphics](../GraphicsNode/GraphicsNode_AddTriangleGraphics.md), [GraphicsNodeProxy.AddTriangleGraphics](../GraphicsNodeProxy/GraphicsNodeProxy_AddTriangleGraphics.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Client graphics texture-based color mapping](../../sample-programs/GraphicsColorMapper_Sample.md) | This test applies texture coordinates expressing distance from the origin to 'the triangle mesh of whatever Part you have open. It then creates either a discrete-band or continuous color mapper and allows you to adjust the values of the mapper to change the range of values that map to various colors. |
| [Client Graphics - Vertex Color by Z Height](../../sample-programs/GraphicsDataSets_CreateColorSet_Sample.md) | This sample demonstrates using client graphics and some other functions that help to support display control. It uses the currently active part and replaces the part display with a display where the part's color varies from blue to red where blue is assigned to the lowest Z portion of the part and red is assigned to the highest Z portion of the part. Areas in between are represented by a smooth blend of color from blue to red. |

## Version

Introduced in version 5

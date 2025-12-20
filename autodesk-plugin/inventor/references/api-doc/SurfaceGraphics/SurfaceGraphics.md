# SurfaceGraphics Object

Derived from: [GraphicsPrimitive](../GraphicsPrimitive/GraphicsPrimitive.md) Object

## Description

The SurfaceGraphics object defines a graphics object created using a body.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../SurfaceGraphics/SurfaceGraphics_Delete.md) | Method that deletes the graphics primitive. |
| [GetCustomLineType](../SurfaceGraphics/SurfaceGraphics_GetCustomLineType.md) | Method that returns information regarding the custom line type in use. The method returns a failure if the return value of the LineType property is not kCustomLineType. |
| [GetTransformBehavior](../SurfaceGraphics/SurfaceGraphics_GetTransformBehavior.md) | Method that gets the current transform behavior of the graphic object. |
| [GetViewSpaceAnchor](../SurfaceGraphics/SurfaceGraphics_GetViewSpaceAnchor.md) | Method that gets the anchor information of the graphics object. This method returns an error if the 'Anchored' property returns False. |
| [RemoveViewSpaceAnchor](../SurfaceGraphics/SurfaceGraphics_RemoveViewSpaceAnchor.md) | The RemoveViewSpaceAnchor method removes the view space anchor from the object, and sets the Anchored property to false. |
| [SetCustomLineType](../SurfaceGraphics/SurfaceGraphics_SetCustomLineType.md) | Method that sets a custom line type to the curve from the specified .lin file. The method automatically changes the value of LineType property to kCustomLineType. |
| [SetTransformBehavior](../SurfaceGraphics/SurfaceGraphics_SetTransformBehavior.md) | Method that sets the transform behavior of the graphic object. |
| [SetViewSpaceAnchor](../SurfaceGraphics/SurfaceGraphics_SetViewSpaceAnchor.md) | Method that anchors the graphics object at the specified point in view space. The Anchored property is set to True. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Anchored](../SurfaceGraphics/SurfaceGraphics_Anchored.md) | Property that indicates whether this graphics primitive is anchored in view space. This property can only be set to False. The Anchored property is automatically set to True by the SetViewSpaceAnchor method. |
| [Application](../SurfaceGraphics/SurfaceGraphics_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Body](../SurfaceGraphics/SurfaceGraphics_Body.md) | Property that returns the SurfaceBody object associated with the SurfaceGraphics. |
| [BurnThrough](../SurfaceGraphics/SurfaceGraphics_BurnThrough.md) | Read-write property that specifies whether or not graphics are always visible even if they are blocked by other objects. |
| [ChildrenAreSelectable](../SurfaceGraphics/SurfaceGraphics_ChildrenAreSelectable.md) | Read-write property that gets and sets whether the children elements of the surface graphics are selectable. |
| [Color](../SurfaceGraphics/SurfaceGraphics_Color.md) | Gets and sets color associated with this primitive. |
| [DepthPriority](../SurfaceGraphics/SurfaceGraphics_DepthPriority.md) | Read-write property that allows you to specify a display priority to the surface graphics. |
| [DisplayedEdges](../SurfaceGraphics/SurfaceGraphics_DisplayedEdges.md) | Property that returns a SurfaceGraphicsEdgeList object. |
| [DisplayedFaces](../SurfaceGraphics/SurfaceGraphics_DisplayedFaces.md) | Property that returns a SurfaceGraphicsFaceList object. |
| [DisplayedVertices](../SurfaceGraphics/SurfaceGraphics_DisplayedVertices.md) | Read-only property that returns a SurfaceGraphicsVertexList object. This list provides access to all vertices that are currently displayed. Vertices can be added to or removed from the list. The vertices added to the list must be from the surface body associated with the SurfaceGraphics, else an error will occur. |
| [DisplaySilhouettes](../SurfaceGraphics/SurfaceGraphics_DisplaySilhouettes.md) | Read-write property that specifies whether or not to display the silhouette edges of the body. The property defaults to True when the SurfaceGraphics object is created. |
| [Id](../SurfaceGraphics/SurfaceGraphics_Id.md) | Read-only property that returns the Id of the object. |
| [LineDefinitionSpace](../SurfaceGraphics/SurfaceGraphics_LineDefinitionSpace.md) | Gets and sets the LineDefinitionSpace applied to this surface graphics. |
| [LineScale](../SurfaceGraphics/SurfaceGraphics_LineScale.md) | Gets and sets the LineScale applied to this surface graphics. |
| [LineType](../SurfaceGraphics/SurfaceGraphics_LineType.md) | Property that gets and sets the line type override. Setting the property to kDefaultLineType restores the default line type. If the property returns kCustomLineType, the GetCustomLineType method can be used to get further details about the line type. |
| [LineWeight](../SurfaceGraphics/SurfaceGraphics_LineWeight.md) | Gets and sets the LineWeight applied to this surface graphics. |
| [Parent](../SurfaceGraphics/SurfaceGraphics_Parent.md) | Property that returns the parent object from whom this object can logically be reached. |
| [RangeBox](../SurfaceGraphics/SurfaceGraphics_RangeBox.md) | Property that returns a Box object which contains the opposing points of a rectangular box that is guaranteed to enclose this object. |
| [Type](../SurfaceGraphics/SurfaceGraphics_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[GraphicsNode.AddSurfaceGraphics](../GraphicsNode/GraphicsNode_AddSurfaceGraphics.md), [GraphicsNodeProxy.AddSurfaceGraphics](../GraphicsNodeProxy/GraphicsNodeProxy_AddSurfaceGraphics.md), [SurfaceGraphicsEdge.Parent](../SurfaceGraphicsEdge/SurfaceGraphicsEdge_Parent.md), [SurfaceGraphicsFace.Parent](../SurfaceGraphicsFace/SurfaceGraphicsFace_Parent.md), [SurfaceGraphicsVertex.Parent](../SurfaceGraphicsVertex/SurfaceGraphicsVertex_Parent.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Selection of Surface Graphics Primitives](../../sample-programs/SelectSurfaceGraphicsPrimitives_Sample.md) | This demonstrates the ability to select client graphic primitives, by creating SurfaceGraphics and showing how you can select B-Rep entities within the graphics. You must have a part or assembly open and select a part of sat file which will be read in and displayed as client graphics. Depending on our responses to the program it will create the graphics so that only the node is selectable (which is all that was supported before), so that all of the primitives are selected, or so that only certain primitives are selectable (every other face in this case). |
| [Transient solid body creation](../../sample-programs/SurfaceBodyDefinition_CreateTransientSurfaceBody_Sample.md) | The following sample demonstrates the creation of a transient solid block body. The newly created body is then displayed using client graphics in a part. |
| [Client graphics creation of 3D primitives](../../sample-programs/TransientBRep_CreateSolidCylinderCone_Sample.md) | This sample demonstrates the creation of 3D primitives (cylinder, cone, etc.) using client graphics. |

## Version

Introduced in version 2009

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
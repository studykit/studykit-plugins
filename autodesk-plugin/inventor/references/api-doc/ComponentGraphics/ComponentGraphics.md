# ComponentGraphics Object

Derived from: [GraphicsPrimitive](../GraphicsPrimitive/GraphicsPrimitive.md) Object

## Description

ComponentGraphics Object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../ComponentGraphics/ComponentGraphics_Delete.md) | Method that deletes the graphics primitive. |
| [GetCustomLineType](../ComponentGraphics/ComponentGraphics_GetCustomLineType.md) | Method that returns information regarding the custom line type in use. The method returns a failure if the return value of the LineType property is not kCustomLineType. |
| [GetTransformBehavior](../ComponentGraphics/ComponentGraphics_GetTransformBehavior.md) | Method that gets the current transform behavior of the graphic object. Graphic objects have two special transform behaviors: front facing and pixel scaling. A front facing object does not rotate as the view is rotated but maintains the same orientation on the screen. It is positioned at a specified location within model and its position on the screen will change as the view is zoomed in and out and scrolled, but its orientation will not change.  A graphic object that has pixel scaling behavior maintains the same size relative to the screen. As the user zooms in and out the graphic objects visible size on the screen will remain the same.  By default an object has no transform behavior, which means its size, position, and orientation are relative to model space.  Text always has front facing behavior regardless of the behavior type returned through this method. |
| [GetViewSpaceAnchor](../ComponentGraphics/ComponentGraphics_GetViewSpaceAnchor.md) | Method that gets the anchor information of the graphics object. This method returns an error if the 'Anchored' property returns False. |
| [RemoveViewSpaceAnchor](../ComponentGraphics/ComponentGraphics_RemoveViewSpaceAnchor.md) | The RemoveViewSpaceAnchor method removes the view space anchor from the object, and sets the Anchored property to false. |
| [SetCustomLineType](../ComponentGraphics/ComponentGraphics_SetCustomLineType.md) | Method that sets a custom line type to the curve from the specified .lin file. The method automatically changes the value of LineType property to kCustomLineType. |
| [SetTransformBehavior](../ComponentGraphics/ComponentGraphics_SetTransformBehavior.md) | Method that sets the transform behavior of the graphic object. Graphic objects have two special transform behaviors: front facing and pixel scaling. A front facing object does not rotate as the view is rotated but maintains the same orientation on the screen. It is positioned at a specified location within model and its position on the screen will change as the view is zoomed in and out and scrolled, but its orientation will not change.  A graphic object that has pixel scaling behavior maintains the same size relative to the screen. As the user zooms in and out the graphic objects visible size on the screen will remain the same.  Any graphic object can have no transform behavior which means it’s size, position, and orientation are relative to model space, front facing behavior, pixel scaling behavior, or front facing and pixel scaling behavior. By default an object has not transform behavior, with the exception of text. Text always has front facing behavior regardless of the behavior type set through this method. |
| [SetViewSpaceAnchor](../ComponentGraphics/ComponentGraphics_SetViewSpaceAnchor.md) | Method that anchors the graphics object at the specified point in view space. The Anchored property is set to True. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Anchored](../ComponentGraphics/ComponentGraphics_Anchored.md) | Property that indicates whether this graphics primitive is anchored in view space. This property can only be set to False. The Anchored property is automatically set to True by the SetViewSpaceAnchor method. |
| [Application](../ComponentGraphics/ComponentGraphics_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Body](../ComponentGraphics/ComponentGraphics_Body.md) | Read-only property that returns the SurfaceBody object associated with the SurfaceGraphics. |
| [BurnThrough](../ComponentGraphics/ComponentGraphics_BurnThrough.md) | Read-write property that specifies whether or not graphics are always visible even if they are blocked by other objects. |
| [Color](../ComponentGraphics/ComponentGraphics_Color.md) | Read-write property that gets and sets the color associated with the primitive. |
| [DepthPriority](../ComponentGraphics/ComponentGraphics_DepthPriority.md) | Read-write property that allows you to specify a display priority to the graphics. This is used in the cases where entities are coincident. The entities with the higher priority will render on top of lower priority entities. |
| [DisplayedEdges](../ComponentGraphics/ComponentGraphics_DisplayedEdges.md) | Read-only property that returns a SurfaceGraphicsEdgeList object. This list provides access to all edges that are currently displayed. |
| [DisplayedFaces](../ComponentGraphics/ComponentGraphics_DisplayedFaces.md) | Read-only property that returns a SurfaceGraphicsFaceList object. This list provides access to all faces that are currently displayed. |
| [DisplaySilhouettes](../ComponentGraphics/ComponentGraphics_DisplaySilhouettes.md) | Read-write property that specifies whether or not to display the silhouette edges of bodies. The property defaults to True when the ComponentGraphics object is created. |
| [Id](../ComponentGraphics/ComponentGraphics_Id.md) | Read-only property that returns the Id of the object. |
| [LineDefinitionSpace](../ComponentGraphics/ComponentGraphics_LineDefinitionSpace.md) | Read-write property that gets and sets the line definition space for this primitive. This affects how the line weight and line scale are applied to the primitive. This defaults to kScreenSpace. |
| [LineScale](../ComponentGraphics/ComponentGraphics_LineScale.md) | Read-write property that gets and sets the line scale applied to this primitive. |
| [LineType](../ComponentGraphics/ComponentGraphics_LineType.md) | Read-write property that gets and sets the line type associated with the primitive. |
| [LineWeight](../ComponentGraphics/ComponentGraphics_LineWeight.md) | Read-write property that gets and sets the thickness of this primitive. If LineDefinitionSpace is set to kScreenSpace, this value is defined in pixels. If LineDefinitionSpace is set to kModelSpace, this value is defined in model units (centimeters). |
| [Parent](../ComponentGraphics/ComponentGraphics_Parent.md) | Property that returns the parent object from whom this object can logically be reached. |
| [RangeBox](../ComponentGraphics/ComponentGraphics_RangeBox.md) | Property that returns a Box object which contains the opposing points of a rectangular box that is guaranteed to enclose this object. |
| [Type](../ComponentGraphics/ComponentGraphics_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[GraphicsNode.AddComponentGraphics](../GraphicsNode/GraphicsNode_AddComponentGraphics.md), [GraphicsNodeProxy.AddComponentGraphics](../GraphicsNodeProxy/GraphicsNodeProxy_AddComponentGraphics.md)

## Version

Introduced in version 2011

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
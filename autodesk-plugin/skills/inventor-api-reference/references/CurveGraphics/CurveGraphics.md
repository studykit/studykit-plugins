# CurveGraphics Object

Derived from: [GraphicsPrimitive](../GraphicsPrimitive/GraphicsPrimitive.md) Object

## Description

The CurveGraphics object defines a graphics object created using a transient curve.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../CurveGraphics/CurveGraphics_Delete.md) | Method that deletes the graphics primitive. |
| [GetCustomLineType](../CurveGraphics/CurveGraphics_GetCustomLineType.md) | Method that returns information regarding the custom line type in use. The method returns a failure if the return value of the LineType property is not kCustomLineType. |
| [GetTransformBehavior](../CurveGraphics/CurveGraphics_GetTransformBehavior.md) | Method that gets the current transform behavior of the graphic object. |
| [GetViewSpaceAnchor](../CurveGraphics/CurveGraphics_GetViewSpaceAnchor.md) | Method that gets the anchor information of the graphics object. This method returns an error if the 'Anchored' property returns False. |
| [RemoveViewSpaceAnchor](../CurveGraphics/CurveGraphics_RemoveViewSpaceAnchor.md) | The RemoveViewSpaceAnchor method removes the view space anchor from the object, and sets the Anchored property to false. |
| [SetCustomLineType](../CurveGraphics/CurveGraphics_SetCustomLineType.md) | Method that sets a custom line type to the curve from the specified .lin file. The method automatically changes the value of LineType property to kCustomLineType. |
| [SetTransformBehavior](../CurveGraphics/CurveGraphics_SetTransformBehavior.md) | Method that sets the transform behavior of the graphic object. |
| [SetViewSpaceAnchor](../CurveGraphics/CurveGraphics_SetViewSpaceAnchor.md) | Method that anchors the graphics object at the specified point in view space. The Anchored property is set to True. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Anchored](../CurveGraphics/CurveGraphics_Anchored.md) | Property that indicates whether this graphics primitive is anchored in view space. This property can only be set to False. The Anchored property is automatically set to True by the SetViewSpaceAnchor method. |
| [Application](../CurveGraphics/CurveGraphics_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [BurnThrough](../CurveGraphics/CurveGraphics_BurnThrough.md) | Read-write property that specifies whether or not graphics are always visible even if they are blocked by other objects. |
| [Color](../CurveGraphics/CurveGraphics_Color.md) | Gets and sets color associated with this primitive. |
| [Curve](../CurveGraphics/CurveGraphics_Curve.md) | Gets and sets curve associated with this primitive. |
| [CurveType](../CurveGraphics/CurveGraphics_CurveType.md) | Property that returns the type of the underlying curve geometry that defines this curve. |
| [DepthPriority](../CurveGraphics/CurveGraphics_DepthPriority.md) | Read-write property that allows you to specify a display priority to the curve graphics. |
| [Id](../CurveGraphics/CurveGraphics_Id.md) | Read-only property that returns the Id of the object. |
| [LineDefinitionSpace](../CurveGraphics/CurveGraphics_LineDefinitionSpace.md) | Gets and sets the LineDefinitionSpace applied to this curve graphics. |
| [LineScale](../CurveGraphics/CurveGraphics_LineScale.md) | Gets and sets the LineScale applied to this curve graphics. |
| [LineType](../CurveGraphics/CurveGraphics_LineType.md) | Property that gets and sets the line type override. Setting the property to kDefaultLineType restores the default line type. If the property returns kCustomLineType, the GetCustomLineType method can be used to get further details about the line type. |
| [LineWeight](../CurveGraphics/CurveGraphics_LineWeight.md) | Gets and sets the LineWeight applied to this curve graphics. |
| [Parent](../CurveGraphics/CurveGraphics_Parent.md) | Property that returns the parent object from whom this object can logically be reached. |
| [RangeBox](../CurveGraphics/CurveGraphics_RangeBox.md) | Property that returns a Box object which contains the opposing points of a rectangular box that is guaranteed to enclose this object. |
| [Type](../CurveGraphics/CurveGraphics_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[GraphicsNode.AddCurveGraphics](../GraphicsNode/GraphicsNode_AddCurveGraphics.md), [GraphicsNodeProxy.AddCurveGraphics](../GraphicsNodeProxy/GraphicsNodeProxy_AddCurveGraphics.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [3D Curve from Parametric Curve](../../sample-programs/ParameterCurveTo3D_Sample.md) | Demonstrates the conversion of a 2d parameteric space curve into the equivalent 3d model space curve. To use this sample you must have a part open. You can select any face and 3D curves will be drawn on the face using client graphics. |
| [Create curve primitives](../../sample-programs/TransientGeometry_Sample.md) | This sample demonstrates the creation of curve primitives (lines, arcs, circles, etc.) using client graphics. |

## Version

Introduced in version 2008

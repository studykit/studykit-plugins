# LineGraphics Object

Derived from: [GraphicsPrimitive](../GraphicsPrimitive/GraphicsPrimitive.md) Object

## Description

The LineGraphics object defines one or more disconnected lines.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../LineGraphics/LineGraphics_Delete.md) | Method that deletes the graphics primitive. |
| [GetCustomLineType](../LineGraphics/LineGraphics_GetCustomLineType.md) | Method that returns information regarding the custom line type in use. The method returns a failure if the return value of the LineType property is not kCustomLineType. |
| [GetTransformBehavior](../LineGraphics/LineGraphics_GetTransformBehavior.md) | Returns the current view transformation settings (e.g. pixel scaling and front facing). |
| [GetViewSpaceAnchor](../LineGraphics/LineGraphics_GetViewSpaceAnchor.md) | Method that gets the anchor information of the graphics object. This method returns an error if the 'Anchored' property returns False. |
| [RemoveViewSpaceAnchor](../LineGraphics/LineGraphics_RemoveViewSpaceAnchor.md) | The RemoveViewSpaceAnchor method removes the view space anchor from the object, and sets the Anchored property to false. |
| [SetCustomLineType](../LineGraphics/LineGraphics_SetCustomLineType.md) | Method that sets a custom line type to the curve from the specified .lin file. The method automatically changes the value of LineType property to kCustomLineType. |
| [SetTransformBehavior](../LineGraphics/LineGraphics_SetTransformBehavior.md) | Sets the view transformation settings (e.g. pixel scaling and front facing). |
| [SetViewSpaceAnchor](../LineGraphics/LineGraphics_SetViewSpaceAnchor.md) | Method that anchors the graphics object at the specified point in view space. The Anchored property is set to True. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Anchored](../LineGraphics/LineGraphics_Anchored.md) | Property that indicates whether this graphics primitive is anchored in view space. This property can only be set to False. The Anchored property is automatically set to True by the SetViewSpaceAnchor method. |
| [Application](../LineGraphics/LineGraphics_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [BurnThrough](../LineGraphics/LineGraphics_BurnThrough.md) | Read-write property that specifies whether or not graphics are always visible even if they are blocked by other objects. |
| [ColorBinding](../LineGraphics/LineGraphics_ColorBinding.md) | Gets and sets how colors are defined for the line. |
| [ColorIndexSet](../LineGraphics/LineGraphics_ColorIndexSet.md) | Gets and sets the GraphicsIndexSet that defines the indices within the GraphicsColorSet to use. |
| [ColorSet](../LineGraphics/LineGraphics_ColorSet.md) | Gets and sets the GraphicsColorSet associated with the set. |
| [CoordinateIndexSet](../LineGraphics/LineGraphics_CoordinateIndexSet.md) | Gets and sets the GraphicsCoordinateIndexSet that defines the indices within the coordinate set to use for the lines of the set. |
| [CoordinateSet](../LineGraphics/LineGraphics_CoordinateSet.md) | Gets and sets the GraphicsCoordinateSet associated with the set. |
| [DepthPriority](../LineGraphics/LineGraphics_DepthPriority.md) | Read-write property that allows you to specify a display priority to the line graphics. |
| [Id](../LineGraphics/LineGraphics_Id.md) | Read-only property that returns the Id of the object. |
| [LineDefinitionSpace](../LineGraphics/LineGraphics_LineDefinitionSpace.md) | Gets and sets the LineDefinitionSpace applied to this line graphics. |
| [LineScale](../LineGraphics/LineGraphics_LineScale.md) | Gets and sets the LineScale applied to this line graphics. |
| [LineType](../LineGraphics/LineGraphics_LineType.md) | Property that gets and sets the line type override. Setting the property to kDefaultLineType restores the default line type. If the property returns kCustomLineType, the GetCustomLineType method can be used to get further details about the line type. |
| [LineWeight](../LineGraphics/LineGraphics_LineWeight.md) | Gets and sets the LineWeight applied to this line graphics. |
| [Parent](../LineGraphics/LineGraphics_Parent.md) | Property that returns the parent object from whom this object can logically be reached. |
| [RangeBox](../LineGraphics/LineGraphics_RangeBox.md) | Property that returns a Box object which contains the opposing points of a rectangular box that is guaranteed to enclose this object. |
| [Type](../LineGraphics/LineGraphics_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[GraphicsNode.AddLineGraphics](../GraphicsNode/GraphicsNode_AddLineGraphics.md), [GraphicsNodeProxy.AddLineGraphics](../GraphicsNodeProxy/GraphicsNodeProxy_AddLineGraphics.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Client Graphics - Draw Range Box](../../sample-programs/ClientGraphics_Sample.md) | This sample demonstrates the use of client graphics to draw the range box of selected entities. |
| [Client Graphics - Line](../../sample-programs/GraphicsNode_AddLineGraphics_Sample.md) | This sample demonstrates the creation of custom graphics using LineGraphics and LineStripGraphics. The same set of coordinate data is used for both types of graphics. Line graphics use two coordinates to define a line, and then the next two coordinates to define the next line, and so on through the defined coordinates. For the data provided, this results in gaps in the drawn curve. Line strips use the first two coordinates to define the first line and then the last point of the first line becomes the first point of the second line and the next coordinate is used as the end point of the second line. This results in the set of points being connected by a continuous set of lines, drawing a continuous curve. This sample also demonstrates two methods of defining the color for client graphics. In one case it uses an existing appearance asset, and in the other, it explicitly defines a color and assigns it. To use the sample you need to have an assembly or part document open. The program has two behaviors: the first time it is run it will draw the graphics. The second time it is run it deletes the previously drawn graphics. |

## Version

Introduced in version 5

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
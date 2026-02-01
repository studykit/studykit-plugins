# TextGraphics Object

Derived from: [GraphicsPrimitive](../GraphicsPrimitive/GraphicsPrimitive.md) Object

## Description

The TextGraphics object defines a set of text strings that are displayed within the model. Each coordinate provided defines a new TextGraphics object. For each coordinate you must also provide a text string.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../TextGraphics/TextGraphics_Delete.md) | Method that deletes the graphics primitive. |
| [GetTextColor](../TextGraphics/TextGraphics_GetTextColor.md) | Method that gets the color of the text. |
| [GetTransformBehavior](../TextGraphics/TextGraphics_GetTransformBehavior.md) | Returns the current view transformation settings (e.g. pixel scaling and front facing). |
| [GetViewSpaceAnchor](../TextGraphics/TextGraphics_GetViewSpaceAnchor.md) | Method that gets the anchor information of the graphics object. This method returns an error if the 'Anchored' property returns False. |
| [PutTextColor](../TextGraphics/TextGraphics_PutTextColor.md) | Method that sets the color of the text. |
| [RemoveViewSpaceAnchor](../TextGraphics/TextGraphics_RemoveViewSpaceAnchor.md) | The RemoveViewSpaceAnchor method removes the view space anchor from the object, and sets the Anchored property to false. |
| [SetTransformBehavior](../TextGraphics/TextGraphics_SetTransformBehavior.md) | Sets the view transformation settings (e.g. pixel scaling and front facing). |
| [SetViewSpaceAnchor](../TextGraphics/TextGraphics_SetViewSpaceAnchor.md) | Method that anchors the graphics object at the specified point in view space. The Anchored property is set to True. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Anchor](../TextGraphics/TextGraphics_Anchor.md) | Gets and sets the position of the text. |
| [Anchored](../TextGraphics/TextGraphics_Anchored.md) | Property that indicates whether this graphics primitive is anchored in view space. This property can only be set to False. The Anchored property is automatically set to True by the SetViewSpaceAnchor method. |
| [Application](../TextGraphics/TextGraphics_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Bold](../TextGraphics/TextGraphics_Bold.md) | Gets and sets whether the text has bold formatting or not. |
| [BurnThrough](../TextGraphics/TextGraphics_BurnThrough.md) | Read-write property that specifies whether or not graphics are always visible even if they are blocked by other objects. |
| [DepthPriority](../TextGraphics/TextGraphics_DepthPriority.md) | Read-write property that allows you to specify a priority for a set. |
| [Font](../TextGraphics/TextGraphics_Font.md) | Gets and sets the font used for the text. |
| [FontSize](../TextGraphics/TextGraphics_FontSize.md) | Gets/sets the font size. The font size is defined in pixels for non-scalable text graphics objects. It is defined in model space units for scalable text graphics objects. |
| [HorizontalAlignment](../TextGraphics/TextGraphics_HorizontalAlignment.md) | Read-write property that allows you to specify the horizontal justification of the text with respect to the coordinate point for the text. |
| [Id](../TextGraphics/TextGraphics_Id.md) | Read-only property that returns the Id of the object. |
| [Italic](../TextGraphics/TextGraphics_Italic.md) | Gets and sets whether the text has italic formatting or not. |
| [Parent](../TextGraphics/TextGraphics_Parent.md) | Property that returns the parent object from whom this object can logically be reached. |
| [RangeBox](../TextGraphics/TextGraphics_RangeBox.md) | Property that returns a Box object which contains the opposing points of a rectangular box that is guaranteed to enclose this object. |
| [Scalable](../TextGraphics/TextGraphics_Scalable.md) | Property that returns whether the TextGraphics object is scalable. If True, the FontSize property can be set a double value indicating its size in model space units. |
| [Text](../TextGraphics/TextGraphics_Text.md) | Gets and sets the text displayed for the TextGraphics object. |
| [Type](../TextGraphics/TextGraphics_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [VerticalAlignment](../TextGraphics/TextGraphics_VerticalAlignment.md) | Read-write property that allows you to specify the vertical justification of the text with respect to the coordinate point for the text. |

## Accessed From

[GraphicsNode.AddScalableTextGraphics](../GraphicsNode/GraphicsNode_AddScalableTextGraphics.md), [GraphicsNode.AddTextGraphics](../GraphicsNode/GraphicsNode_AddTextGraphics.md), [GraphicsNodeProxy.AddScalableTextGraphics](../GraphicsNodeProxy/GraphicsNodeProxy_AddScalableTextGraphics.md), [GraphicsNodeProxy.AddTextGraphics](../GraphicsNodeProxy/GraphicsNodeProxy_AddTextGraphics.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Text Using Client Graphics (Simple)](../../sample-programs/GraphicsNode_AddTextGraphics_Sample.md) | This sample demonstrates creating text using client graphics. It illustrates the simple case where the text is one font and is one line. |
| [Text Using Client Graphics (Multiple fonts and lines)](../../sample-programs/GraphicsNode_AddTextGraphics2_Sample.md) | This sample demonstrates creating text using client graphics. It illustrates the more complex case of changes in font and more than one line. |
| [Anchored Client Grahics](../../sample-programs/GraphicsPrimitive_SetViewSpaceAnchor_Sample.md) | This sample demonstrates the creation of client graphics that is fully anchored in a view. |

## Version

Introduced in version 5

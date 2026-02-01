# CurveGraphics.SetTransformBehavior Method

Parent Object: [CurveGraphics](../CurveGraphics/CurveGraphics.md)

## Description

Method that sets the transform behavior of the graphic object.

## Remarks

Graphic objects have two special transform behaviors: front facing and pixel scaling. A front facing object does not rotate as the view is rotated but maintains the same orientation on the screen. It is positioned at a specified location within model and its position on the screen will change as the view is zoomed in and out and scrolled, but its orientation will not change. A graphic object that has pixel scaling behavior maintains the same size relative to the screen. As the user zooms in and out the graphic objects visible size on the screen will remain the same. Any graphic object can have no transform behavior which means it's size, position, and orientation are relative to model space, front facing behavior, pixel scaling behavior, or front facing and pixel scaling behavior. By default an object has not transform behavior, with the exception of text. Text always has front facing behavior regardless of the behavior type set through this method.

## Syntax

CurveGraphics.**SetTransformBehavior**( ***Anchor*** As [Point](../Point/Point.md), ***BehaviorType*** As [DisplayTransformBehaviorEnum](../DisplayTransformBehaviorEnum.md), [***PixelScale***] As Double )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Anchor | [Point](../Point/Point.md) | Input Point object that specifies the anchor point of the graphic object in model space. The coordinates of this point are always defined in model space. The value of this argument is ignored when setting the behavior type to kNoTransformBehaviors. |
| BehaviorType | [DisplayTransformBehaviorEnum](../DisplayTransformBehaviorEnum.md) | Input value from DisplayTransformBehaviorEnum that specifies the type of transform behavior the text has. Valid values are kFrontFacing, kFrontFacingAndPixelScaling, kNoTransformBehaviors, and kPixelScaling. TextGraphics objects are always front facing regardless of the defined behavior type. |
| PixelScale | Double | Input Double that defines the scale factor to apply to all coordinates associated with this graphics object. This scale factor is only used when the behavior type is kFrontFacingAndPixelScaling or kPixelScaling. |

## Version

Introduced in version 2008

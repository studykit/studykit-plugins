# ComponentGraphics.GetTransformBehavior Method

Parent Object: [ComponentGraphics](../ComponentGraphics/ComponentGraphics.md)

## Description

Method that gets the current transform behavior of the graphic object. Graphic objects have two special transform behaviors: front facing and pixel scaling. A front facing object does not rotate as the view is rotated but maintains the same orientation on the screen. It is positioned at a specified location within model and its position on the screen will change as the view is zoomed in and out and scrolled, but its orientation will not change.

A graphic object that has pixel scaling behavior maintains the same size relative to the screen. As the user zooms in and out the graphic objects visible size on the screen will remain the same.

By default an object has no transform behavior, which means its size, position, and orientation are relative to model space.  Text always has front facing behavior regardless of the behavior type returned through this method.

## Syntax

ComponentGraphics.**GetTransformBehavior**( ***TextAnchor*** As [Point](../Point/Point.md), ***BehaviorType*** As [DisplayTransformBehaviorEnum](../DisplayTransformBehaviorEnum.md), ***PixelScale*** As Double )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| TextAnchor | [Point](../Point/Point.md) | Output Point object that returns the anchor point of the graphic object in model space. The coordinates of this point are always defined in model space. The value of this argument is irrelevant when the behavior type to kNoTransformBehaviors. |
| BehaviorType | [DisplayTransformBehaviorEnum](../DisplayTransformBehaviorEnum.md) | Output value from DisplayTransformBehaviorEnum that returns the type of transform behavior the text has. Valid values are kFrontFacing, kFrontFacingAndPixelScaling, kNoTransformBehaviors, and kPixelScaling. TextGraphics objects are always front facing regardless of the defined behavior type. |
| PixelScale | Double | Output Double that returns the scale factor to apply to all coordinates associated with this graphics object. The scale factor is only relevant when the object has pixel scaling behavior. |

## Version

Introduced in version 2011

# TextGraphics.SetTransformBehavior Method

Parent Object: [TextGraphics](../TextGraphics/TextGraphics.md)

## Description

Sets the view transformation settings (e.g. pixel scaling and front facing).

## Syntax

TextGraphics.**SetTransformBehavior**( ***Anchor*** As [Point](../Point/Point.md), ***BehaviorType*** As [DisplayTransformBehaviorEnum](../DisplayTransformBehaviorEnum.md), [***PixelScale***] As Double )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Anchor | [Point](../Point/Point.md) | Input that indicates which point is unaffected by the transform behavior. |
| BehaviorType | [DisplayTransformBehaviorEnum](../DisplayTransformBehaviorEnum.md) | Input DisplayTransformBehaviorEnum that specifies which transform behaviors are to be used. |
| PixelScale | Double | Input Double that indicates how many pixels should be used to draw one model unit when pixel scaling is used. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Text Using Client Graphics (Multiple fonts and lines)](../../sample-programs/GraphicsNode_AddTextGraphics2_Sample.md) | This sample demonstrates creating text using client graphics. It illustrates the more complex case of changes in font and more than one line. |

## Version

Introduced in version 6

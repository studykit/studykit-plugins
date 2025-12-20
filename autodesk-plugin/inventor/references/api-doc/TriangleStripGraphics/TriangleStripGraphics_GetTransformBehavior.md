# TriangleStripGraphics.GetTransformBehavior Method

Parent Object: [TriangleStripGraphics](../TriangleStripGraphics/TriangleStripGraphics.md)

## Description

Returns the current view transformation settings (e.g. pixel scaling and front facing).

## Syntax

TriangleStripGraphics.**GetTransformBehavior**( ***TextAnchor*** As [Point](../Point/Point.md), ***BehaviorType*** As [DisplayTransformBehaviorEnum](../DisplayTransformBehaviorEnum.md), ***PixelScale*** As Double )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| TextAnchor | [Point](../Point/Point.md) | Output Point that returns the point that is unaffected by the transform behavior. |
| BehaviorType | [DisplayTransformBehaviorEnum](../DisplayTransformBehaviorEnum.md) | Output DisplayTransformBehaviorEnum that returns the transform behaviors currently being used. |
| PixelScale | Double | Output Point that returns the number of pixels that are used to draw one model unit when pixel scaling is used. |

## Version

Introduced in version 5

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
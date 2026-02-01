# TriangleFanGraphics.SetViewSpaceAnchor Method

Parent Object: [TriangleFanGraphics](../TriangleFanGraphics/TriangleFanGraphics.md)

## Description

Method that anchors the graphics object at the specified point in view space. The Anchored property is set to True.

## Syntax

TriangleFanGraphics.**SetViewSpaceAnchor**( ***Origin*** As [Point](../Point/Point.md), ***Anchor*** As [Point2d](../Point2d/Point2d.md), ***AnchorRelativeTo*** As [ViewLayoutEnum](../ViewLayoutEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Origin | [Point](../Point/Point.md) | Input that specifies the origin of the coordinate system. |
| Anchor | [Point2d](../Point2d/Point2d.md) | Input that indicates which point is unaffected by the transform behavior. |
| AnchorRelativeTo | [ViewLayoutEnum](../ViewLayoutEnum.md) | Input constant indicating which corner of the view the anchor is relative to. |

## Version

Introduced in version 9

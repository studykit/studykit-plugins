# SurfaceGraphics.GetViewSpaceAnchor Method

Parent Object: [SurfaceGraphics](../SurfaceGraphics/SurfaceGraphics.md)

## Description

Method that gets the anchor information of the graphics object. This method returns an error if the 'Anchored' property returns False.

## Syntax

SurfaceGraphics.**GetViewSpaceAnchor**( ***Origin*** As [Point](../Point/Point.md), ***Anchor*** As [Point2d](../Point2d/Point2d.md), ***AnchorRelativeTo*** As [ViewLayoutEnum](../ViewLayoutEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Origin | [Point](../Point/Point.md) | Output that specifies the origin of the coordinate system. |
| Anchor | [Point2d](../Point2d/Point2d.md) | Output that indicates which point is unaffected by the transform behavior. |
| AnchorRelativeTo | [ViewLayoutEnum](../ViewLayoutEnum.md) | Output constant indicating which corner of the view the anchor is relative to. |

## Version

Introduced in version 2009

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
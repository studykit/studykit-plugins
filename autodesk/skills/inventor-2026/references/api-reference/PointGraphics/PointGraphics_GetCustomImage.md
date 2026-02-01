# PointGraphics.GetCustomImage Method

Parent Object: [PointGraphics](../PointGraphics/PointGraphics.md)

## Description

Method that gets the image used for this PointGraphics object. This is only valid in the case where the PointRenderStyle property returns kCustomImagePointStyle, otherwise this method will fail.

## Syntax

PointGraphics.**GetCustomImage**( ***GraphicsImageSet*** As [GraphicsImageSet](../GraphicsImageSet/GraphicsImageSet.md), ***GraphicsImageIndex*** As Long )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| GraphicsImageSet | [GraphicsImageSet](../GraphicsImageSet/GraphicsImageSet.md) | Output GraphicsImageSet that is currently assigned to this PointGraphics object. |
| GraphicsImageIndex | Long | Output Long that indicates which image in the GraphicsImageSet is currently being used by this PointGraphics object. |

## Version

Introduced in version 2011

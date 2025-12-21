# SectionDrawingView.AlignAuxiliary Method

Parent Object: [SectionDrawingView](../SectionDrawingView/SectionDrawingView.md)

## Description

Method that re-aligns an auxiliary view. The method fails if the view is not an auxiliary view.

## Syntax

SectionDrawingView.**AlignAuxiliary**( ***DrawingCurve*** As [DrawingCurve](../DrawingCurve/DrawingCurve.md), ***Position*** As [Point2d](../Point2d/Point2d.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| DrawingCurve | [DrawingCurve](../DrawingCurve/DrawingCurve.md) | Input DrawingCurve object that specifies the orientation edge for the auxiliary view. This must be from the parent view, else the method returns an error. |
| Position | [Point2d](../Point2d/Point2d.md) | Input Point2d object that specifies the new placement point for the auxiliary view on the sheet. |

## Version

Introduced in version 2010

# SectionDrawingView.SheetToModelSpace Method

Parent Object: [SectionDrawingView](../SectionDrawingView/SectionDrawingView.md)

## Description

Method that takes a 2d coordinate in sheet space, and returns a Line in model space. Since this method transforms from 2D space to 3D space, there is insufficient information to obtain a 3D model point. Hence, this method returns a Line in the view direction on which the point lies. You may then use the FindUsingRay method to find the point(s) of interest.

## Syntax

SectionDrawingView.**SheetToModelSpace**( ***SheetCoordinate*** As [Point2d](../Point2d/Point2d.md) ) As [Line](../Line/Line.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| SheetCoordinate | [Point2d](../Point2d/Point2d.md) | Input Point2d object of a point within sheet space. |

## Version

Introduced in version 9

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
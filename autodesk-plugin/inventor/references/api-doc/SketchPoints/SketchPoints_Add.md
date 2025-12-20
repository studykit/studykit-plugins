# SketchPoints.Add Method

Parent Object: [SketchPoints](../SketchPoints/SketchPoints.md)

## Description

Method that creates a new sketch point at the specified coordinate.

## Syntax

SketchPoints.**Add**( ***Point*** As [Point2d](../Point2d/Point2d.md), [***HoleCenter***] As Boolean ) As [SketchPoint](../SketchPoint/SketchPoint.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Point | [Point2d](../Point2d/Point2d.md) | Input that defines the position of the sketch point. |
| HoleCenter | Boolean | Optional input Boolean that specifies if the point is a hole center or not. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Hole Feature - Through holes (RegularAndTapped)](../../sample-programs/HoleFeature_Sample.md) | This sample demonstrates the creation of through holes, both regular and tapped. |
| [Add a punch tool feature](../../sample-programs/PunchToolFeatures_Add_Sample.md) | This program demonstrates the creation of a punch tool feature. It uses one of the punch features that's delivered with Inventor. It assumes you already have an existing sheet metal part and have selected a face to place the punch feature on. The selected face should be large so there is room for the punch features. |

## Version

Introduced in version 5

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
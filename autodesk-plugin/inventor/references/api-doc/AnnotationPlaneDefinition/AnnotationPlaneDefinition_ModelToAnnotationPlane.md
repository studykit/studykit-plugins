# AnnotationPlaneDefinition.ModelToAnnotationPlane Method

Parent Object: [AnnotationPlaneDefinition](../AnnotationPlaneDefinition/AnnotationPlaneDefinition.md)

## Description

Method that takes a 3d coordinate in model space, projects it onto the annotation plane along the normal of the plane and returns a Point2d object containing the resulting coordinate point in annotation plane space.

## Syntax

AnnotationPlaneDefinition.**ModelToAnnotationPlane**( ***ModelCoordinate*** As [Point](../Point/Point.md) ) As [Point2d](../Point2d/Point2d.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| ModelCoordinate | [Point](../Point/Point.md) | Input Point object defining the 3d coordinate in model space. |

## Version

Introduced in version 2018

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
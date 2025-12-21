# RadiusModelDimensions.CreateDefinition Method

Parent Object: [RadiusModelDimensions](../RadiusModelDimensions/RadiusModelDimensions.md)

## Description

Method that creates a radius dimension definition. This is a not a radius dimension but an object that encapsulates all of the information that defines a dimension. You use the methods an properties of this object to define the dimension you want to create and then provide it as input to the Add method.

## Syntax

RadiusModelDimensions.**CreateDefinition**( ***Intent*** As [GeometryIntent](../GeometryIntent/GeometryIntent.md), ***AnnotationPlaneDefinition*** As [AnnotationPlaneDefinition](../AnnotationPlaneDefinition/AnnotationPlaneDefinition.md), ***LandingPosition*** As [Point](../Point/Point.md) ) As [RadiusModelDimensionDefinition](../RadiusModelDimensionDefinition/RadiusModelDimensionDefinition.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Intent | [GeometryIntent](../GeometryIntent/GeometryIntent.md) | Input GeometryIntent object that defines the geometry to dimension to. For a radius dimension this can be a circular edge, cylindrical face, sketch arc, or sketch circle. |
| AnnotationPlaneDefinition | [AnnotationPlaneDefinition](../AnnotationPlaneDefinition/AnnotationPlaneDefinition.md) | Input AnnotationPlaneDefinition object that defines the annotation plane the annotation will be created on. An existing annotation plane can be specified by using the AnnotationPlaneDefinition object associated with the existing annotation plane. |
| LandingPosition | [Point](../Point/Point.md) | Input Point object that specifies the landing position of the dimension. The point will be projected onto the orientation plane. |

## Version

Introduced in version 2018

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
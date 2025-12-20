# ModelFeatureControlFrames.CreateDefinition Method

Parent Object: [ModelFeatureControlFrames](../ModelFeatureControlFrames/ModelFeatureControlFrames.md)

## Description

Method that creates a feature control frame definition.

## Syntax

ModelFeatureControlFrames.**CreateDefinition**( ***Intent*** As [GeometryIntent](../GeometryIntent/GeometryIntent.md), ***AnnotationPlaneDefinition*** As [AnnotationPlaneDefinition](../AnnotationPlaneDefinition/AnnotationPlaneDefinition.md), ***LandingPosition*** As [Point](../Point/Point.md) ) As [ModelFeatureControlFrameDefinition](../ModelFeatureControlFrameDefinition/ModelFeatureControlFrameDefinition.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Intent | [GeometryIntent](../GeometryIntent/GeometryIntent.md) | Input GeometryIntent object that defines the geometry to attach the symbol to. |
| AnnotationPlaneDefinition | [AnnotationPlaneDefinition](../AnnotationPlaneDefinition/AnnotationPlaneDefinition.md) | Input AnnotationPlaneDefinition object that defines the annotation plane the annotation will be created on. An existing annotation plane can be specified by using the AnnotationPlaneDefinition object associated with the existing annotation plane. |
| LandingPosition | [Point](../Point/Point.md) | Input Point object that specifies the landing position of the frame. The point will be projected onto the orientation plane. This can be Nothing in the case where the symbol is attached directly to the object without a leader. |

## Version

Introduced in version 2018

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
# ModelDatumIdentifiers.CreateDefinition Method

Parent Object: [ModelDatumIdentifiers](../ModelDatumIdentifiers/ModelDatumIdentifiers.md)

## Description

Method that creates a datum identifier definition.

## Syntax

ModelDatumIdentifiers.**CreateDefinition**( ***Intent*** As [GeometryIntent](../GeometryIntent/GeometryIntent.md), ***AnnotationPlaneDefinition*** As [AnnotationPlaneDefinition](../AnnotationPlaneDefinition/AnnotationPlaneDefinition.md), ***TextPosition*** As [Point](../Point/Point.md) ) As [ModelDatumIdentifierDefinition](../ModelDatumIdentifierDefinition/ModelDatumIdentifierDefinition.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Intent | [GeometryIntent](../GeometryIntent/GeometryIntent.md) | Input GeometryIntent object that defines the geometry to attach the symbol to. |
| AnnotationPlaneDefinition | [AnnotationPlaneDefinition](../AnnotationPlaneDefinition/AnnotationPlaneDefinition.md) | Input AnnotationPlaneDefinition object that defines the annotation plane the annotation will be created on. An existing annotation plane can be specified by using the AnnotationPlaneDefinition object associated with the existing annotation plane. |
| TextPosition | [Point](../Point/Point.md) |  |

## Version

Introduced in version 2018

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
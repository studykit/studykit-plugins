# ModelWeldingSymbols.CreateDefinitions Method

Parent Object: [ModelWeldingSymbols](../ModelWeldingSymbols/ModelWeldingSymbols.md)

## Description

Method that creates a model welding symbol definitions object.

## Syntax

ModelWeldingSymbols.**CreateDefinitions**( ***LeaderPoints*** As [ObjectCollection](../ObjectCollection/ObjectCollection.md), ***AnnotationPlaneDefinition*** As [AnnotationPlaneDefinition](../AnnotationPlaneDefinition/AnnotationPlaneDefinition.md) ) As [ModelWeldingSymbolDefinitions](../ModelWeldingSymbolDefinitions/ModelWeldingSymbolDefinitions.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| LeaderPoints | [ObjectCollection](../ObjectCollection/ObjectCollection.md) | ObjectCollection containing a series of Point objects representing the leader originating at the model welding symbol. The last item in the collection (even if it is the only item) can be a GeometryIntent object indicating the geometry to attach the leader to. The ObjectCollection must contain at least one item, else the method will fail. The points are projected onto the orientation plane. |
| AnnotationPlaneDefinition | [AnnotationPlaneDefinition](../AnnotationPlaneDefinition/AnnotationPlaneDefinition.md) | Input AnnotationPlaneDefinition object that defines the annotation plane the annotation will be created on. An existing annotation plane can be specified by using the AnnotationPlaneDefinition object associated with the existing annotation plane. |

## Version

Introduced in version 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
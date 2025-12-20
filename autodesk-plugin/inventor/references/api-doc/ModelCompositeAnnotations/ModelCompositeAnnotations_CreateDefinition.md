# ModelCompositeAnnotations.CreateDefinition Method

Parent Object: [ModelCompositeAnnotations](../ModelCompositeAnnotations/ModelCompositeAnnotations.md)

## Description

Creates a model composite annotation definition.

## Syntax

ModelCompositeAnnotations.**CreateDefinition**( ***BaseAnnotation*** As [ModelAnnotation](../ModelAnnotation/ModelAnnotation.md), [***AnnotationType***] As Variant ) As [ModelCompositeAnnotationDefinition](../ModelCompositeAnnotationDefinition/ModelCompositeAnnotationDefinition.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| BaseAnnotation | [ModelAnnotation](../ModelAnnotation/ModelAnnotation.md) | Input ModelAnnotation object that specifies the base annotation in the ModelCompositeAnnotation. Valid base annotation can be a ModelDimension, ModelFeatureControlFrame, ModelSurfaceTextureSymbol, ModelLeaderNote and ModelHoleThreadNote. |
| AnnotationType | Variant | Optional input String value that specifies the annotation type of the ModelCompositeAnnotation. |

## Version

Introduced in version 2018

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
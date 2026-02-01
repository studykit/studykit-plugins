# ModelAnnotations.CreateAnnotationPlaneDefinitionUsingIntents Method

Parent Object: [ModelAnnotations](../ModelAnnotations/ModelAnnotations.md)

## Description

Method that determines all of the valid annotation planes for the given input. The definitions for these annotation planes is returned as a collection, allowing you to select the desired annotation plane to use when creating annotation.

## Syntax

ModelAnnotations.**CreateAnnotationPlaneDefinitionUsingIntents**( ***AnnotationType*** As [ObjectTypeEnum](../ObjectTypeEnum.md), ***IntentOne*** As [GeometryIntent](../GeometryIntent/GeometryIntent.md), [***IntentTwo***] As Variant, [***IntentThree***] As Variant, [***XAxis***] As Variant ) As [AnnotationPlaneDefinitionsEnumerator](../AnnotationPlaneDefinitionsEnumerator/AnnotationPlaneDefinitionsEnumerator.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| AnnotationType | [ObjectTypeEnum](../ObjectTypeEnum.md) | Input AnnotationTypeEnum that defines the type of annotation you intend on using the annotation plane to create. |
| IntentOne | [GeometryIntent](../GeometryIntent/GeometryIntent.md) | Input GeometryIntent object that defines the first geometry that specifies the position of the annotation plane. |
| IntentTwo | Variant | Optional Input GeometryIntent object that defines the second geometry that specifies the position of the annotation plane. If there is only one geometry defininng the annotation plane, you can pass Nothing for this argument. |
| IntentThree | Variant | Optional Input GeometryIntent object that defines the third geometry that specifies the position of the annotation plane. If there is only one or two geometries defining the annotation plane, you can pass Nothing for this argument.   This is an optional argument whose default value is null. |
| XAxis | Variant | Input linear entity that defines the x-axis of the annotation plane. If not provided a default orientation is determined. A valid input object for the axis is a linear edge, work axis, 2D sketch line.   This is an optional argument whose default value is null. |

## Version

Introduced in version 2018

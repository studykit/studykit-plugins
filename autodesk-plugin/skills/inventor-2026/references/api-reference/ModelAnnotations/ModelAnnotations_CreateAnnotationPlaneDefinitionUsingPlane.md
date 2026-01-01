# ModelAnnotations.CreateAnnotationPlaneDefinitionUsingPlane Method

Parent Object: [ModelAnnotations](../ModelAnnotations/ModelAnnotations.md)

## Description

Method that returns an annotation plane definition for the given planar entity. The object returned is not an annotation plane, but is the information that defines a plane and can be used to create an annotation plane when an annotation is created.

## Syntax

ModelAnnotations.**CreateAnnotationPlaneDefinitionUsingPlane**( ***Plane*** As Object, [***XAxisDirection***] As Variant ) As [AnnotationPlaneDefinition](../AnnotationPlaneDefinition/AnnotationPlaneDefinition.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Plane | Object | Input planar entity that the annotation plane will lie on. The input object can be a planar face or work plane |
| XAxisDirection | Variant | Input linear entity that defines the x-axis of the annotation plane. If not provided a default orientation is determined. A valid input object for the axis is a linear edge, work axis, 2D sketch line. |

## Version

Introduced in version 2018

# ModelAnnotations.Item Property

Parent Object: [ModelAnnotations](../ModelAnnotations/ModelAnnotations.md)

## Description

Method that returns the specified model annotation object from the collection.

## Syntax

ModelAnnotations.**Item**( ***Index*** As Variant ) As [ModelAnnotation](../ModelAnnotation/ModelAnnotation.md)

## Property Value

This is a read only property whose value is a [ModelAnnotation](../ModelAnnotation/ModelAnnotation.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Input Variant value that specifies the object to return. This can be either a numeric value indicating the index of the item in the collection or it can be a string indicating the annotation name. If an out of range index or a name of a non-existent annotation is provided, an error occurs. |

## Version

Introduced in version 2018

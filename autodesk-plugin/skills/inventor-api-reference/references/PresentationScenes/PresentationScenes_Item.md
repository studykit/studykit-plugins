# PresentationScenes.Item Property

Parent Object: [PresentationScenes](../PresentationScenes/PresentationScenes.md)

## Description

Allows integer-indexed access to items in the collection.

## Syntax

PresentationScenes.**Item**( ***Index*** As Variant ) As [PresentationScene](../PresentationScene/PresentationScene.md)

## Property Value

This is a read only property whose value is a [PresentationScene](../PresentationScene/PresentationScene.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Specifies the index of the object to return. This can be either a numeric value indicating the index of the item in the collection or it can be a string indicating the PresentationScene name. If an out of range index or an name of a non-existent PresentationScene is provided, an error will occur . |

## Version

Introduced in version 2018

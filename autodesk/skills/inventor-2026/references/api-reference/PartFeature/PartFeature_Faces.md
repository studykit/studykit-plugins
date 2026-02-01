# PartFeature.Faces Property

Parent Object: [PartFeature](../PartFeature/PartFeature.md)

## Description

Property that returns a collection that provides access to all of the faces of the feature. The Faces collection object will return the faces that still currently exist in the part. For example, if a face has been consumed by additional modeling operations it will not be returned.

## Syntax

PartFeature.**Faces**() As [Faces](../Faces/Faces.md)

## Property Value

This is a read only property whose value is a [Faces](../Faces/Faces.md).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create sheet metal face and flange features](../../sample-programs/SheetMetalFeatures_FlangeFeatures_Sample.md) | This sample demonstrates the creation of sheet metal face and flange features. |

## Version

Introduced in version 5

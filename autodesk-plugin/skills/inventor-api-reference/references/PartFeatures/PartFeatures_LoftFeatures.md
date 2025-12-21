# PartFeatures.LoftFeatures Property

Parent Object: [PartFeatures](../PartFeatures/PartFeatures.md)

## Description

Property that returns the LoftFeatures collection object. This collection provides access to existing LoftFeature objects and provides functionality to create new LoftFeature objects.

## Syntax

PartFeatures.**LoftFeatures**() As [LoftFeatures](../LoftFeatures/LoftFeatures.md)

## Property Value

This is a read only property whose value is a [LoftFeatures](../LoftFeatures/LoftFeatures.md).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Loft Feature With Non-Planar Section](../../sample-programs/LoftFeature_Sample.md) | This sample demonstrates the creation of a loft feature. It uses two sections for the loft, one is from a 2d sketch and the other is a non-planar section from a 3d sketch. Because one of the sketches isn't planar, a surface is created instead of a solid. |

## Version

Introduced in version 5

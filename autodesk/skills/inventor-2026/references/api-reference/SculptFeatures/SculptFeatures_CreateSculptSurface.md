# SculptFeatures.CreateSculptSurface Method

Parent Object: [SculptFeatures](../SculptFeatures/SculptFeatures.md)

## Description

Method that creates a new SculptSurface object. The new SculptSurface is returned.

## Syntax

SculptFeatures.**CreateSculptSurface**( ***Surface*** As Object, [***Direction***] As [PartFeatureExtentDirectionEnum](../PartFeatureExtentDirectionEnum.md) ) As [SculptSurface](../SculptSurface/SculptSurface.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Surface | Object | Object that defines a boundary surface for the sculpt feature. Valid input objects for the surface are WorkSurface and WorkPlane. |
| Direction | [PartFeatureExtentDirectionEnum](../PartFeatureExtentDirectionEnum.md) | Optional input constant that specifies the sculpt direction for the surface specified by the Surface argument. The direction specifies the side of the surface that should be used when creating the sculpt feature. Valid input is kPositiveExtentDirection, kNegativeExtentDirection or kSymmetricExtentDirection. If no value is specified, then kPositiveExtentDirection will be assumed for the direction. |

## Version

Introduced in version 11

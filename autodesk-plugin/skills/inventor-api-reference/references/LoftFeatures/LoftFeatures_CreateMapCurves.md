# LoftFeatures.CreateMapCurves Method

Parent Object: [LoftFeatures](../LoftFeatures/LoftFeatures.md)

## Description

Method that creates a new MapPointCurves object. You then use functionality provided by the resulting MapPointCurves object to define the specific point mapping.

## Syntax

LoftFeatures.**CreateMapCurves**( ***Sections*** As [ObjectCollection](../ObjectCollection/ObjectCollection.md) ) As [MapPointCurves](../MapPointCurves/MapPointCurves.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Sections | [ObjectCollection](../ObjectCollection/ObjectCollection.md) | Input ObjectCollection that contains the sections for the loft. The sections provided for input must be the same sections that will be used as input for the LoftFeatures.Add method. |

## Version

Introduced in version 6

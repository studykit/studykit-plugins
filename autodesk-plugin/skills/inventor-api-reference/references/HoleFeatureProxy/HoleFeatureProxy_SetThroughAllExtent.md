# HoleFeatureProxy.SetThroughAllExtent Method

Parent Object: [HoleFeatureProxy](../HoleFeatureProxy/HoleFeatureProxy.md)

## Description

Method that specifies the termination type for the hole feature. Hole features can be specified to terminate at a particular distance or object, or can be specified as "through all," which means it extends through all faces of the feature. This method defines a through-all termination type.

## Syntax

HoleFeatureProxy.**SetThroughAllExtent**( ***ExtentDirection*** As [PartFeatureExtentDirectionEnum](../PartFeatureExtentDirectionEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| ExtentDirection | [PartFeatureExtentDirectionEnum](../PartFeatureExtentDirectionEnum.md) | Input argument identifying the direction in which to extend the hole feature. |

## Version

Introduced in version 9

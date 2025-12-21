# RevolveFeatureProxy.SetAngleExtent Method

Parent Object: [RevolveFeatureProxy](../RevolveFeatureProxy/RevolveFeatureProxy.md)

## Description

Method that changes the extents of the revolution to the given angle

## Syntax

RevolveFeatureProxy.**SetAngleExtent**( ***Angle*** As Variant, ***ExtentDirection*** As [PartFeatureExtentDirectionEnum](../PartFeatureExtentDirectionEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Angle | Variant | Defines the sweep angle of the revolution. This can be either a numeric value or a string. A parameter for this value will be created and the supplied string or value is assigned to the parameter. If a value is input, the units are radians. If a string is input, the units can be specified as part of the string or it will default to the current angle units of the document. |
| ExtentDirection | [PartFeatureExtentDirectionEnum](../PartFeatureExtentDirectionEnum.md) | constant that indicates the direction of the sweep. Valid input is kPositive, kNegative, or kSymmetric. The sweep direction is defined relative to the natural direction of the axis entity. kPositive defines the sweep to be in a positive direction using the right-hand rule about the axis. |

## Version

Introduced in version 11

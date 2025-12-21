# AssemblyJointDefinition.SetOriginOneAsOffset Method

Parent Object: [AssemblyJointDefinition](../AssemblyJointDefinition/AssemblyJointDefinition.md)

## Description

Method that sets assembly joint origin as offset origin for OriginOne.

## Syntax

AssemblyJointDefinition.**SetOriginOneAsOffset**( ***XOffset*** As Variant, ***YOffset*** As Variant )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| XOffset | Variant | Input Variant object to specify the offset value along the X-axis. A numeric or string value can be supplied for this argument and a parameter will be automatically created after the joint is created. If a numeric value is supplied, the value is in centimeters, and the parameter is set to the value specified. If a string value is supplied it will be used as the expression for the newly created parameter, if the value is supplied without a unit qualifier it will default to the current document length unit. The following is a valid entry for it, assuming the parameter d1 already exists and defines a length “d1+3 in”. If a geometry is provided, the offset value will be calculated with the OriginOne and the geometry. Valid geometries are Edge, Face, WorkPlane, WorkAxis and their proxies. |
| YOffset | Variant | Input Variant object to specify the offset value along the Y-axis. A numeric or string value can be supplied for this argument and a parameter will be automatically created after the joint is created. If a numeric value is supplied, the value is in centimeters, and the parameter is set to the value specified. If a string value is supplied it will be used as the expression for the newly created parameter, if the value is supplied without a unit qualifier it will default to the current document length unit. The following is a valid entry for it, assuming the parameter d1 already exists and defines a length “d1+3 in”. If a geometry is provided, the offset value will be calculated with the OriginOne and the geometry. Valid geometries are Edge, Face, WorkPlane, WorkAxis and their proxies. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create planar AssemblyJoint with offset to origins](../../sample-programs/AssemblyJointDefinition_SetOriginOneAsOffset_Sample.md) | This sample demonstrates how to create a planar AssemblyJoint with offset to the OriginOne and OriginTwo. |

## Version

Introduced in version 2016

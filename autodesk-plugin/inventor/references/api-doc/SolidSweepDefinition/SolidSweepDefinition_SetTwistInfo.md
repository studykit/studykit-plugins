# SolidSweepDefinition.SetTwistInfo Method

Parent Object: [SolidSweepDefinition](../SolidSweepDefinition/SolidSweepDefinition.md)

## Description

Method that sets the twist angle info.

## Syntax

SolidSweepDefinition.**SetTwistInfo**( ***TwistAngle*** As Variant, [***TwistAxis***] As Variant )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| TwistAngle | Variant | Input numeric or string value to set the twist angle, a parameter will be created for the twist angle when the sweep is created. If a numeric value is supplied, the value is in radian. If a string value is supplied it will be used as the expression for the newly created parameter, if the value is supplied without a unit qualifier it will default to the current document angle unit. The following is a valid entry for it, assuming the parameter d1 already exists and defines a angle “d1+3 deg”. |
| TwistAxis | Variant | Optional input object to specify the twist axis. This is required if the TwistAngle is specified with non-zero value. This can be a linear Edge, WorkAxis or Face which can infer an axis. When a Face object is specified it should be a cylindrical, conical, elliptical or toroidal surface where its axis is used. |

## Version

Introduced in version 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
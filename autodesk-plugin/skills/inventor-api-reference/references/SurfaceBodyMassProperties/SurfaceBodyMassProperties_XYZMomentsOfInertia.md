# SurfaceBodyMassProperties.XYZMomentsOfInertia Method

Parent Object: [SurfaceBodyMassProperties](../SurfaceBodyMassProperties/SurfaceBodyMassProperties.md)

## Description

Method that gets the moments of inertia about the reference axis with the center of gravity as origin.

## Syntax

SurfaceBodyMassProperties.**XYZMomentsOfInertia**( ***Ixx*** As Double, ***Iyy*** As Double, ***Izz*** As Double, ***Ixy*** As Double, ***Iyz*** As Double, ***Ixz*** As Double, [***OverriddenMass***] As Variant )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Ixx | Double | Output Double that returns the XX partial moment. |
| Iyy | Double | Output Double that returns the YY partial moment. |
| Izz | Double | Output Double that returns the ZZ partial moment. |
| Ixy | Double | Output Double that returns the XY partial moment. |
| Iyz | Double | Output Double that returns the YZ partial moment. |
| Ixz | Double | Output Double that returns the XZ partial moment. |
| OverriddenMass | Variant | Optional input Double that specifies the overridden mass in kilograms to calculate the moment of inertia. If this is not specified the calculated mass of the body will be used. |

## Version

Introduced in version 2023

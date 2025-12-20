# SurfaceBodyProxy.Volume Property

Parent Object: [SurfaceBodyProxy](../SurfaceBodyProxy/SurfaceBodyProxy.md)

## Description

Property that returns the volume of the component in database units.

## Syntax

SurfaceBodyProxy.**Volume**( ***PrecisionPercent*** As Double ) As Double

## Property Value

This is a read only property whose value is a Double.

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| PrecisionPercent | Double | Input Double that specifies the requested relative accuracy of the result as a percentage. For example, a value of 0.01 requests a maximum error of one percent. The application should find the mass properties for several requested accuracies and compare the results since there is a limitation to the current algorithm in that it does have a bound on how precisely the algorithm can calculate mass properties, due to hard coded convergence criteria in the functions. If you tighten the relative error value and the mass properties values don't change, that means it is as close as can be achieved. |

## Version

Introduced in version 4

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
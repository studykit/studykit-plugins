# BSplineCurveDefinition.AddPoint Method

Parent Object: [BSplineCurveDefinition](../BSplineCurveDefinition/BSplineCurveDefinition.md)

## Description

Method that adds point and its corresponding weight and tangent information to the definition.

## Syntax

BSplineCurveDefinition.**AddPoint**( ***Point*** As [Point](../Point/Point.md), [***Weight***] As Double, [***Tangent***] As Variant )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Point | [Point](../Point/Point.md) | Input object that specifies the point. |
| Weight | Double | Optional input double that specifies the weight for the input point. If not specified, a default value of 1 is used. |
| Tangent | Variant | Optional input UnitVector object that defines the tangent of the BSpline curve at this point.   This is an optional argument whose default value is null. |

## Version

Introduced in version 9

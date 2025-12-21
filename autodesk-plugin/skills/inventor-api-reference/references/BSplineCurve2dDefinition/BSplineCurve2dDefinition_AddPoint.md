# BSplineCurve2dDefinition.AddPoint Method

Parent Object: [BSplineCurve2dDefinition](../BSplineCurve2dDefinition/BSplineCurve2dDefinition.md)

## Description

Method that adds point and its corresponding weight and tangent information to the definition.

## Syntax

BSplineCurve2dDefinition.**AddPoint**( ***Point*** As [Point2d](../Point2d/Point2d.md), [***Weight***] As Double, [***Tangent***] As Variant )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Point | [Point2d](../Point2d/Point2d.md) | Input object that specifies the point. |
| Weight | Double | Optional input double that specifies the weight for the input point. If not specified, a default value of 1 is used. |
| Tangent | Variant | Optional input UnitVector2d object that defines the tangent of the BSpline curve at this point.   This is an optional argument whose default value is null. |

## Version

Introduced in version 9

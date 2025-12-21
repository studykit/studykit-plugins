# LoftedFlangeDefinition.SetOutputType Method

Parent Object: [LoftedFlangeDefinition](../LoftedFlangeDefinition/LoftedFlangeDefinition.md)

## Description

Method that sets the technique that will be used to calculate the lofted flange.

## Syntax

LoftedFlangeDefinition.**SetOutputType**( ***OutputType*** As [LoftedFlangeOutputTypeEnum](../LoftedFlangeOutputTypeEnum.md), [***FacetTolerance***] As Variant )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| OutputType | [LoftedFlangeOutputTypeEnum](../LoftedFlangeOutputTypeEnum.md) | Constant that defines the how the lofted flange will be calculated. Valid values are kDieFormedLoftedFlange, kPressBrakeChordToleranceLoftedFlange, kPressBrakeFacetAngleLoftedFlange, and kPressBrakeFacetDistanceLoftedFlange. |
| FacetTolerance | Variant | Optional Variant that defines the tolerance value used when calculating the lofted flange. This only applies to the press brake methods and is ignored if the OutputType argument is kDieFormedLoftedFlange.  This can be either a numeric value or a string. A parameter for this value will be created and the supplied string or value is assigned to the parameter. If a value is input and the output type is kPressBrakeChordToleranceLoftedFlange or kPressBrakeFacetDistanceLoftedFlange, the units are centimeters. If the output type is kPressBrakeFacetAngleLoftedFlange, the units are radians. If a string is input, the units can be specified as part of the string or it will default to the current length or angle units of the document. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create sheet metal lofted flange feature](../../sample-programs/LoftedFlangeFeatures_Add_Sample.md) | The following sample demonstrates the creation of a sheet metal lofted flange feature. |

## Version

Introduced in version 2011

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
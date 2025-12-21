# CutFeatures.Add Method

Parent Object: [CutFeatures](../CutFeatures/CutFeatures.md)

## Description

Method that creates a new cut feature.

## Remarks

The newly created CutFeature object is returned.

## Syntax

CutFeatures.**Add**( ***CutDefinition*** As [CutDefinition](../CutDefinition/CutDefinition.md) ) As [CutFeature](../CutFeature/CutFeature.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| CutDefinition | [CutDefinition](../CutDefinition/CutDefinition.md) | Input CutDefinition object that defines the face feature you want to create. A CutDefinition object can be created using the CutFeatures.CreateCutDefinition method. It can also be obtained from an existing CutFeature object. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create sheet metal face and cut features](../../sample-programs/SheetMetalFeatures_Sample.md) | This sample demonstrates the creation of sheet metal face and cut features. |

## Version

Introduced in version 2009

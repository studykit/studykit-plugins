# iMateResults.AddByTwoiMates Method

Parent Object: [iMateResults](../iMateResults/iMateResults.md)

## Description

Method that creates a new iMate result. The newly created iMateResult object is returned.

## Remarks

If the two inputs do not define a valid iMateResult the method will fail. The result of adding an iMate will create a single iMateResult and one or more assembly constraints. If a CompositeiMateDefinition is input, multiple constraints will result.

## Syntax

iMateResults.**AddByTwoiMates**( ***iMateDefinitionOne*** As [iMateDefinition](../iMateDefinition/iMateDefinition.md), ***iMateDefinitionTwo*** As [iMateDefinition](../iMateDefinition/iMateDefinition.md) ) As [iMateResult](../iMateResult/iMateResult.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| iMateDefinitionOne | [iMateDefinition](../iMateDefinition/iMateDefinition.md) | Input object that defines the first input iMate. |
| iMateDefinitionTwo | [iMateDefinition](../iMateDefinition/iMateDefinition.md) | Input object that defines the second input iMate. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [iMate Result Creation](../../sample-programs/iMateResult_Sample.md) | This sample demonstrates creating an iMate result using two existin iMate definitions. |

## Version

Introduced in version 6

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
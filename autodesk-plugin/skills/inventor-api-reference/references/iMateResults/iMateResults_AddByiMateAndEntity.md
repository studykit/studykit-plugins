# iMateResults.AddByiMateAndEntity Method

Parent Object: [iMateResults](../iMateResults/iMateResults.md)

## Description

Method that creates a new iMate result. The newly created iMateResult object is returned. If the two inputs do not define a valid iMateResult the method will fail.

## Syntax

iMateResults.**AddByiMateAndEntity**( ***iMateDefinition*** As [iMateDefinition](../iMateDefinition/iMateDefinition.md), ***Entity*** As Object, [***EntityBiasPoint***] As Variant, [***AngleEntityReversed***] As Variant ) As [iMateResult](../iMateResult/iMateResult.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| iMateDefinition | [iMateDefinition](../iMateDefinition/iMateDefinition.md) | Input object that defines the input iMate. |
| Entity | Object | Input object that defines the second entity. This object must be a valid geometric entity in the assembly, such as a , WorkAxis, SketchLine, etc. |
| EntityBiasPoint | Variant | Optional input object that is used to help in determining the initial position of the occurrence. The occurrences are repositioned in an attempt to make the bias point coincident with the iMate. This provides some general control over the position of the occurrence when it isn't being controlled by another constraint. An example of when the bias points are useful is the case when the first constraint on a part is a mate constraint. In the case where the mate is between two planes, the parts can be positioned anywhere along the infinite plane that defines their mating contact. Using the bias point you can define the position of the two occurrences, relative to each other. If a bias point is not given, one is calculated that is at the center of the parameter range of the input entity. |
| AngleEntityReversed | Variant | Optional input Boolean that is only used when creating an angle constraint. This argument specifies if the direction of the entity should be reversed or not. A value of True indicates it should be reversed. If this argument is not provided for an angle constraint it defaults to False. This argument is ignored for all other constraint types.   This is an optional argument whose default value is null. |

## Version

Introduced in version 6

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
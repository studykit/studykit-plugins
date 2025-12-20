# iMateDefinitions.AddMateiMateDefinition Method

Parent Object: [iMateDefinitions](../iMateDefinitions/iMateDefinitions.md)

## Description

Method that creates a new mate iMate definition.

## Syntax

iMateDefinitions.**AddMateiMateDefinition**( ***Entity*** As Object, ***Offset*** As Variant, [***EntityInferredType***] As [InferredTypeEnum](../InferredTypeEnum.md), [***BiasPoint***] As Variant, [***Name***] As String, [***MatchList***] As Variant ) As [MateiMateDefinition](../MateiMateDefinition/MateiMateDefinition.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Entity | Object | Defines the entity to mate. |
| Offset | Variant | Defines the offset value. This can be either a numeric value or a string. A parameter for this value is created and the supplied string or value is assigned to the parameter. If a value is input, the units are centimeters. If a string is input the units can be specified as part of the string or will default to the current length units of the document. |
| EntityInferredType | [InferredTypeEnum](../InferredTypeEnum.md) | Enum that specifies how the geometry of the entity is to be interpreted. Depending on the geometry of the entity, different options are possible. If the entity is a cylinder this can be either kNoInferrence or kInferredLine. For kNoInferrence to be valid for a cylinder, the matching iMate must also be on a cylinder and they must be the same radius. If the entity is a sphere this can be either kNoInferrence or kInferredPoint. For kNoInferrence to be valid for a sphere, the matching iMate must also be on a sphere and they must be the same radius. If the entity is a cone this can be either kNoInferrence or kInferredLine. For kNoInferrence to be valid for a cone, the matching iMate must also be on a cone and they must have the same taper angle. If the entity is a torus this can be either kInferredLine or kInferredPoint. For a plane, only kNoInferrence is valid. |
| BiasPoint | Variant | Point object that is used to help determine the initial position when this iMate definition is used. This provides some general control over the position of the occurrence when it isn't being controlled by another constraint. An example of when the bias points are useful is the case when the first constraint on a part is a mate constraint. In the case where the mate is between two planes, the parts can be positioned anywhere along the infinite plane that defines their mating contact. Using the bias points you can define the position of the two occurrences, relative to each other. If a bias point is not given, one is calculated that is at the center of the parameter range of the input entity.   This is an optional argument whose default value is null. |
| Name | String | Specifies the name of the iMate definition. If not specified, a name is automatically generated.   This is an optional argument whose default value is "". |
| MatchList | Variant | Array of Strings that specifies the priority order of the iMate definitions to match.   This is an optional argument whose default value is null. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Add iMate Definition](../../sample-programs/iMateDefinitions_AddMateiMateDefinition_Sample.md) | Add iMate definitions using AddMateiMateDefinition and AddInsertiMateDefinition. |

## Version

Introduced in version 11

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
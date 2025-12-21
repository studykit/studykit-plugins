# AssemblyConstraints.AddMateConstraint Method

Parent Object: [AssemblyConstraints](../AssemblyConstraints/AssemblyConstraints.md)

## Description

Method that creates a new mate assembly constraint. The two input entities can be a combination of planar faces, linear edges, vertices, cylindrical faces, conical faces, spherical faces, revolved faces, work planes, work axes, and work points. When a cylindrical, conical, or revolved face is input, the axis of the surface is used for the constraint. When a sphere is input, the center point of the sphere is used for the constraint. To use the surface of a cylindrical, conical, or spherical face use the EntityOneInferredType or EntityTwoInferredType arguments.

## Syntax

AssemblyConstraints.**AddMateConstraint**( ***EntityOne*** As Object, ***EntityTwo*** As Object, ***Offset*** As Variant, [***EntityOneInferredType***] As [InferredTypeEnum](../InferredTypeEnum.md), [***EntityTwoInferredType***] As [InferredTypeEnum](../InferredTypeEnum.md), [***BiasPointOne***] As Variant, [***BiasPointTwo***] As Variant ) As [MateConstraint](../MateConstraint/MateConstraint.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| EntityOne | Object | Input object that defines the first object. |
| EntityTwo | Object | Input object that defines the second object. |
| Offset | Variant | Input Variant that defines the offset between the two input entities. This can be either a numeric value or a string. A parameter for this value is created and the supplied string or value is assigned to the parameter. If a value is input, the units are centimeters. If a string is input the units can be specified as part of the string or will default to the current length units of the document. |
| EntityOneInferredType | [InferredTypeEnum](../InferredTypeEnum.md) | Optional input constant that specifies how the geometry of entity one is to be interpreted. Depending on the geometry of the entity one, different options are possible. If entity one is a cylinder this can be either kNoInference or kInferredLine. For kNoInference to be valid for a cylinder, entity two must also be a cylinder and they must be the same radius. If entity one is a sphere this can be either kNoInference or kInferredPoint. For kNoInference to be valid for a sphere, entity two must also be a sphere and they must be the same radius. If entity one is a cone this can be either kNoInference or kInferredLine. For kNoInference to be valid for a cone, entity two must also be a cone and they must have the same taper angle. If entity one is a torus this can be either kInferredLine or kInferredPoint. For a plane, only kNoInference is valid. |
| EntityTwoInferredType | [InferredTypeEnum](../InferredTypeEnum.md) | Input enum that specifies how the geometry of entity two is to be interpreted. Depending on the geometry of the entity two, different options are possible. If entity two is a cylinder this can be either kNoInference or kInferredLine. For kNoInference to be valid for a cylinder, entity one must also be a cylinder and they must be the same radius. If entity two is a sphere this can be either kNoInference or kInferredPoint. For kNoInference to be valid for a sphere, entity one must also be a sphere and they must be the same radius. If entity two is a cone this can be either kNoInference or kInferredLine. For kNoInference to be valid for a cone, entity one must also be a cone and they must have the same taper angle. If entity two is a torus this can be either kInferredLine or kInferredPoint. For a plane, only kNoInference is valid.     This is an optional argument whose default value is 24833. |
| BiasPointOne | Variant | Optional input object that is used help in determining the initial position of the occurrence. The occurrences are repositioned in an attempt to make the two bias points coincident. This provides some general control over the position of the occurrence when it isn't being controlled by another constraint. An example of when the bias points are useful is the case when the first constraint on a part is a mate constraint. In the case where the mate is between two planes, the parts can be positioned anywhere along the infinite plane that defines their mating contact. Using the bias points you can define the position of the two occurrences, relative to each other. If a bias point is not given, one is calculated that is at the center of the parameter range of the input entity.   This is an optional argument whose default value is null. |
| BiasPointTwo | Variant | Optional input object that is used help in determining the initial position of the occurrence. The occurrences are repositioned in an attempt to make the two bias points coincident. This provides some general control over the position of the occurrence when it isn't being controlled by another constraint. An example of when the bias points are useful is the case when the first constraint on a part is a mate constraint. In the case where the mate is between two planes, the parts can be positioned anywhere along the infinite plane that defines their mating contact. Using the bias points you can define the position of the two occurrences, relative to each other. If a bias point is not given, one is calculated that is at the center of the parameter range of the input entity.   This is an optional argument whose default value is null. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Add assembly mate constraint](../../sample-programs/AssemblyConstraints_AddMateConstraint_Sample.md) | This sample demonstrates the creation of an assembly mate constraint. |
| [Add mate constraint using work planes in parts](../../sample-programs/AssemblyConstraints_AddMateConstraint2_Sample.md) | This sample demonstrates creating a mate constraint between two occurrences using the work planes within those occurrences. |
| [Add mate constraint with limits](../../sample-programs/AssemblyConstraints_AddMateConstraint3_Sample.md) | This sample demonstrates the creation of an assembly mate constraint with maximum and minimum limits defined. |

## Version

Introduced in version 5

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
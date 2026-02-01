# AssemblyConstraints.AddInsertConstraint Method

Parent Object: [AssemblyConstraints](../AssemblyConstraints/AssemblyConstraints.md)

## Description

Method that creates a new insert assembly constraint.

## Syntax

AssemblyConstraints.**AddInsertConstraint**( ***EntityOne*** As Object, ***EntityTwo*** As Object, ***AxesOpposed*** As Boolean, ***Distance*** As Variant, [***BiasPointOne***] As Variant, [***BiasPointTwo***] As Variant ) As [InsertConstraint](../InsertConstraint/InsertConstraint.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| EntityOne | Object | Object that defines the first object. This object is a circular edge. |
| EntityTwo | Object | Object that defines the second object. This object is a circular edge. |
| AxesOpposed | Boolean | Input Boolean that specifies whether the direction of the axes of the input entities are in the same direction or opposed. A value of True indicates they are opposed. |
| Distance | Variant | Input Variant that defines the offset between the two input entities. This can be either a numeric value or a string. A parameter for this value is created and the supplied string or value is assigned to the parameter. If a value is input, the units are centimeters. If a string is input the units can be specified as part of the string or will default to the current length units of the document. |
| BiasPointOne | Variant | Optional input object that is used help in determining the initial position of the occurrence. The occurrences are repositioned in an attempt to make the two bias points coincident. This provides some general control over the position of the occurrence when it isn't being controlled by another constraint. An example of when the bias points are useful is the case when the first constraint on a part is a mate constraint. In the case where the mate is between two planes, the parts can be positioned anywhere along the infinite plane that defines their mating contact. Using the bias points you can define the position of the two occurrences, relative to each other. If a bias point is not given, one is calculated that is at the center of the parameter range of the input entity. |
| BiasPointTwo | Variant | Optional input object that is used help in determining the initial position of the occurrence. The occurrences are repositioned in an attempt to make the two bias points coincident. This provides some general control over the position of the occurrence when it isn't being controlled by another constraint. An example of when the bias points are useful is the case when the first constraint on a part is a mate constraint. In the case where the mate is between two planes, the parts can be positioned anywhere along the infinite plane that defines their mating contact. Using the bias points you can define the position of the two occurrences, relative to each other. If a bias point is not given, one is calculated that is at the center of the parameter range of the input entity.   This is an optional argument whose default value is null. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Add assembly insert constraint](../../sample-programs/AssemblyConstraints_AddInsertConstraint_Sample.md) | This sample demonstrates the creation of an assembly insert constraint. |

## Version

Introduced in version 5

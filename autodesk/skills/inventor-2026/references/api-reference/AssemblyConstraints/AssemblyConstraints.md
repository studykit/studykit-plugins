# AssemblyConstraints Object

## Description

Provides access to the collection in the top level of the assembly.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [AddAngleConstraint](../AssemblyConstraints/AssemblyConstraints_AddAngleConstraint.md) | Method that creates a new angle assembly constraint. |
| [AddFlushConstraint](../AssemblyConstraints/AssemblyConstraints_AddFlushConstraint.md) | Method that creates a new flush assembly constraint. |
| [AddInsertConstraint](../AssemblyConstraints/AssemblyConstraints_AddInsertConstraint.md) | Method that creates a new insert assembly constraint. |
| [AddInsertConstraint2](../AssemblyConstraints/AssemblyConstraints_AddInsertConstraint2.md) | Creates a new Insert assembly constraint. |
| [AddMateConstraint](../AssemblyConstraints/AssemblyConstraints_AddMateConstraint.md) | Method that creates a new mate assembly constraint. The two input entities can be a combination of planar faces, linear edges, vertices, cylindrical faces, conical faces, spherical faces, revolved faces, work planes, work axes, and work points. When a cylindrical, conical, or revolved face is input, the axis of the surface is used for the constraint. When a sphere is input, the center point of the sphere is used for the constraint. To use the surface of a cylindrical, conical, or spherical face use the EntityOneInferredType or EntityTwoInferredType arguments. |
| [AddMateConstraint2](../AssemblyConstraints/AssemblyConstraints_AddMateConstraint2.md) | Creates a new Mate assembly constraint. |
| [AddRotateRotateConstraint](../AssemblyConstraints/AssemblyConstraints_AddRotateRotateConstraint.md) | Method that creates a new rotation motion constraint. |
| [AddRotateTranslateConstraint](../AssemblyConstraints/AssemblyConstraints_AddRotateTranslateConstraint.md) | Method that creates a new rotate-translate motion constraint. |
| [AddSymmetryConstraint](../AssemblyConstraints/AssemblyConstraints_AddSymmetryConstraint.md) | Creates a new Symmetry assembly constraint. |
| [AddTangentConstraint](../AssemblyConstraints/AssemblyConstraints_AddTangentConstraint.md) | Method that creates a new tangent assembly constraint. |
| [AddTransitionalConstraint](../AssemblyConstraints/AssemblyConstraints_AddTransitionalConstraint.md) | Method that creates a new transitional constraint. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../AssemblyConstraints/AssemblyConstraints_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Count](../AssemblyConstraints/AssemblyConstraints_Count.md) | Property that returns the number of items in this collection. |
| [Item](../AssemblyConstraints/AssemblyConstraints_Item.md) | Returns the specified AssemblyConstraint object from the collection. This is the default property of the AssemblyConstraints collection object. |
| [Parent](../AssemblyConstraints/AssemblyConstraints_Parent.md) | Property that returns the parent of the object. |
| [Type](../AssemblyConstraints/AssemblyConstraints_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[AssemblyComponentDefinition.Constraints](../AssemblyComponentDefinition/AssemblyComponentDefinition_Constraints.md), [WeldmentComponentDefinition.Constraints](../WeldmentComponentDefinition/WeldmentComponentDefinition_Constraints.md)

## Version

Introduced in version 4

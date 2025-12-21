# AssemblyConstraints.AddSymmetryConstraint Method

Parent Object: [AssemblyConstraints](../AssemblyConstraints/AssemblyConstraints.md)

## Description

Creates a new Symmetry assembly constraint.

## Syntax

AssemblyConstraints.**AddSymmetryConstraint**( ***EntityOne*** As Object, ***EntityTwo*** As Object, ***SymmetryPlane*** As Object, [***EntityOneInferredType***] As [InferredTypeEnum](../InferredTypeEnum.md), [***EntityTwoInferredType***] As [InferredTypeEnum](../InferredTypeEnum.md), [***NormalsOpposed***] As Boolean ) As [AssemblySymmetryConstraint](../AssemblySymmetryConstraint/AssemblySymmetryConstraint.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| EntityOne | Object | Input entity that is to be symmetric. |
| EntityTwo | Object | Input entity that is to be symmetric. |
| SymmetryPlane | Object | Input planar entity that defines the symmetry plane. This can either be a planar face or a work plane. |
| EntityOneInferredType | [InferredTypeEnum](../InferredTypeEnum.md) | Optional input constant that specifies how the geometry of entity one is to be interpreted. Depending on the geometry of the entity one, different options are possible. If entity one is a linear entity this can be either kNoInference or kInferredPoint, for kInferredPoint the mid-point of the linear entity is used for the constraint. If entity one is a circular/elliptical sketch entity, this can be either kInferredPiont or kInferredLine. If entity one is a cylindrical, elliptic-cylindrical, conical face this can be kNoInference or kInferredLine. If entity one is a toroidal face this can be either kInferredLine or kInferredPoint. If entity one is a spherical face this can be kInferredPoint. For a plane, only kNoInference is valid. |
| EntityTwoInferredType | [InferredTypeEnum](../InferredTypeEnum.md) | Optional input enum that specifies how the geometry of entity two is to be interpreted. Depending on the geometry of the entity two, different options are possible. If entity two is a linear entity this can be either kNoInference or kInferredPoint, for kInferredPoint the mid-point of the linear entity is used for the constraint. If entity two is a circular/elliptical sketch entity, this can be either kInferredPiont or kInferredLine. If entity two is a cylindrical, elliptic-cylindrical, conical face this can be kNoInference or kInferredLine. If entity two is a toroidal face this can be either kInferredLine or kInferredPoint. If entity two is a spherical face this can be kInferredPoint. For a plane, only kNoInference is valid.   This is an optional argument whose default value is 24833. |
| NormalsOpposed | Boolean | This argument only applies when the two entities are planar (planar face or work plane) and defines if the normal of the planar entities are oriented so they are opposed or aligned. If the input entities are not planar, this argument is ignored. If they are planar and this argument is not specified they will defined to be opposed.   This is an optional argument whose default value is True. |

## Version

Introduced in version 2014

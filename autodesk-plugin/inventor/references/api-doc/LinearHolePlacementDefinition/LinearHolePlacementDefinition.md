# LinearHolePlacementDefinition Object

Derived from: [HolePlacementDefinition](../HolePlacementDefinition/HolePlacementDefinition.md) Object

## Description

The LinearHolePlacementDefinition object defines the placement of a hole feature with respect to two linear entities.

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../LinearHolePlacementDefinition/LinearHolePlacementDefinition_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [DirectionOneReversed](../LinearHolePlacementDefinition/LinearHolePlacementDefinition_DirectionOneReversed.md) | Gets and sets whether the direction of the hole placement with respect to the first reference entity is reversed. |
| [DirectionTwoReversed](../LinearHolePlacementDefinition/LinearHolePlacementDefinition_DirectionTwoReversed.md) | Gets and sets whether the direction of the hole placement with respect to the second reference entity is reversed. |
| [DistanceOne](../LinearHolePlacementDefinition/LinearHolePlacementDefinition_DistanceOne.md) | Property that returns the parameter controlling the distance of the hole center from the first reference entity. |
| [DistanceTwo](../LinearHolePlacementDefinition/LinearHolePlacementDefinition_DistanceTwo.md) | Property that returns the parameter controlling the distance of the hole center from the second reference entity. |
| [Parent](../LinearHolePlacementDefinition/LinearHolePlacementDefinition_Parent.md) | Property that returns the parent PartFeature of the definition. This property returns Nothing in the case where the definition object is created using one of the Create methods on the HoleFeatures object. |
| [Plane](../LinearHolePlacementDefinition/LinearHolePlacementDefinition_Plane.md) | Property that indicates the plane on which the hole feature is placed. This can be a planar Face object or a WorkPlane object. |
| [ReferenceEntityOne](../LinearHolePlacementDefinition/LinearHolePlacementDefinition_ReferenceEntityOne.md) | Property that indicates the first entity referenced for dimensioning the placement of the hole. This can only be a linear Edge. |
| [ReferenceEntityTwo](../LinearHolePlacementDefinition/LinearHolePlacementDefinition_ReferenceEntityTwo.md) | Property that indicates the second entity referenced for dimensioning the placement of the hole. This can only be a linear Edge. |
| [Type](../LinearHolePlacementDefinition/LinearHolePlacementDefinition_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Hole feature linear placement](../../sample-programs/HoleFeatures_CreateLinearPlacementDefinition_Sample.md) | This sample demonstrates the creation of a hole feature using the linear placement type. |

## Version

Introduced in version 10

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |
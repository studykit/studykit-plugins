# DSValue Object

## Description

The DSValue object represents a value where the value can be either a constant value or be a variable value defined by a graph.

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../DSValue/DSValue_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [ConstantValue](../DSValue/DSValue_ConstantValue.md) | Get and set the value. This property is writable when the DSValue object is associated with a transient object. |
| [Graph](../DSValue/DSValue_Graph.md) | Gets the graph that controls this value. You can access and edit the graph using the properties on the returned DSValueGraph object. This property returns Nothing in the case where the value is defined by a constant value . You can determine this using the IsConstantValue property. |
| [IsConstantValue](../DSValue/DSValue_IsConstantValue.md) | Indicates if this value is defined by a constant value or a graph. |
| [Type](../DSValue/DSValue_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[DSDegreeOfFreedom.ImposedMotionValue](../DSDegreeOfFreedom/DSDegreeOfFreedom_ImposedMotionValue.md), [DSDegreeOfFreedom.LoadDamping](../DSDegreeOfFreedom/DSDegreeOfFreedom_LoadDamping.md), [DSDegreeOfFreedom.LoadDryFrictionCoefficient](../DSDegreeOfFreedom/DSDegreeOfFreedom_LoadDryFrictionCoefficient.md), [DSDegreeOfFreedom.LoadDryFrictionRadius](../DSDegreeOfFreedom/DSDegreeOfFreedom_LoadDryFrictionRadius.md), [DSDegreeOfFreedom.LoadForce](../DSDegreeOfFreedom/DSDegreeOfFreedom_LoadForce.md), [DSDegreeOfFreedom.LoadSpringElasticStiffness](../DSDegreeOfFreedom/DSDegreeOfFreedom_LoadSpringElasticStiffness.md), [DSDegreeOfFreedom.LoadSpringFreePosition](../DSDegreeOfFreedom/DSDegreeOfFreedom_LoadSpringFreePosition.md), [DSDegreeOfFreedom.MaxBoundsDamping](../DSDegreeOfFreedom/DSDegreeOfFreedom_MaxBoundsDamping.md), [DSDegreeOfFreedom.MaxBoundsStiffness](../DSDegreeOfFreedom/DSDegreeOfFreedom_MaxBoundsStiffness.md), [DSDegreeOfFreedom.MaxBoundsValue](../DSDegreeOfFreedom/DSDegreeOfFreedom_MaxBoundsValue.md), [DSDegreeOfFreedom.MinBoundsDamping](../DSDegreeOfFreedom/DSDegreeOfFreedom_MinBoundsDamping.md), [DSDegreeOfFreedom.MinBoundsStiffness](../DSDegreeOfFreedom/DSDegreeOfFreedom_MinBoundsStiffness.md), [DSDegreeOfFreedom.MinBoundsValue](../DSDegreeOfFreedom/DSDegreeOfFreedom_MinBoundsValue.md), [DSLoadDefinition.Magnitude](../DSLoadDefinition/DSLoadDefinition_Magnitude.md), [DSLoadDefinition.VectorXComponent](../DSLoadDefinition/DSLoadDefinition_VectorXComponent.md), [DSLoadDefinition.VectorYComponent](../DSLoadDefinition/DSLoadDefinition_VectorYComponent.md), [DSLoadDefinition.VectorZComponent](../DSLoadDefinition/DSLoadDefinition_VectorZComponent.md)

## Version

Introduced in version 2013

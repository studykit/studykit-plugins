# DSDegreeOfFreedom Object

## Description

The DSDegreeOfFreedom object represents a degree of freedom associated with a joint.

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../DSDegreeOfFreedom/DSDegreeOfFreedom_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [DegreeOfFreedomType](../DSDegreeOfFreedom/DSDegreeOfFreedom_DegreeOfFreedomType.md) | Read-only property that indicates if this degree of freedom is for a rotation or translation. |
| [ImposedMotionType](../DSDegreeOfFreedom/DSDegreeOfFreedom_ImposedMotionType.md) | Gets and sets the type of imposed motion defined on a degree of freedom. |
| [ImposedMotionValue](../DSDegreeOfFreedom/DSDegreeOfFreedom_ImposedMotionValue.md) | Read-only property returning a DSValue object that you can use to get and set the imposed motion. This property returns nothing in the case where the ImposedMotionType property is set to kNoImposedMotion. |
| [InitialPosition](../DSDegreeOfFreedom/DSDegreeOfFreedom_InitialPosition.md) | Gets and sets the initial position. This property is writable when the DSDegreeOfFreedom object is transient and not associated with an existing joint. |
| [InitialVelocity](../DSDegreeOfFreedom/DSDegreeOfFreedom_InitialVelocity.md) | Gets and sets the initial position. This property is writable when the DSDegreeOfFreedom object is transient and not associated with an existing joint. |
| [IsLoadEnabled](../DSDegreeOfFreedom/DSDegreeOfFreedom_IsLoadEnabled.md) | Gets and sets if the load settings for this joint are enabled. |
| [IsMaxBoundsEnabled](../DSDegreeOfFreedom/DSDegreeOfFreedom_IsMaxBoundsEnabled.md) | Gets and sets if the maximum bounds of the joint are defined. |
| [IsMinBoundsEnabled](../DSDegreeOfFreedom/DSDegreeOfFreedom_IsMinBoundsEnabled.md) | Gets and sets if the minimum bounds of the joint are defined. |
| [IsPositionLocked](../DSDegreeOfFreedom/DSDegreeOfFreedom_IsPositionLocked.md) | Gets and sets if the position of this joint is locked. |
| [IsVelocityComputed](../DSDegreeOfFreedom/DSDegreeOfFreedom_IsVelocityComputed.md) | Gets and sets if the velocity is computed. |
| [LoadDamping](../DSDegreeOfFreedom/DSDegreeOfFreedom_LoadDamping.md) | Gets a DSValue object that you can use to get and set the load damping. This property returns Nothing in the case where IsLoadEnabled is False. |
| [LoadDryFrictionCoefficient](../DSDegreeOfFreedom/DSDegreeOfFreedom_LoadDryFrictionCoefficient.md) | Gets a DSValue object that you can use to get and set the load dry friction coefficient. This property returns Nothing in the case where IsLoadEnabled is False. |
| [LoadDryFrictionRadius](../DSDegreeOfFreedom/DSDegreeOfFreedom_LoadDryFrictionRadius.md) | Gets a DSValue object that you can use to get and set the load dry friction radius. This property returns Nothing in the case where IsLoadEnabled is False. |
| [LoadForce](../DSDegreeOfFreedom/DSDegreeOfFreedom_LoadForce.md) | Gets a DSValue object that you can use to get and set the load force. This property returns Nothing in the case where IsLoadEnabled is False. |
| [LoadSpringElasticStiffness](../DSDegreeOfFreedom/DSDegreeOfFreedom_LoadSpringElasticStiffness.md) | Gets a DSValue object that you can use to get and set the load spring free position. This property returns Nothing in the case where IsLoadEnabled is False. |
| [LoadSpringFreePosition](../DSDegreeOfFreedom/DSDegreeOfFreedom_LoadSpringFreePosition.md) | Gets a DSValue object that you can use to get and set the load spring free position. This property returns Nothing in the case where IsLoadEnabled is False. |
| [MaxBoundsDamping](../DSDegreeOfFreedom/DSDegreeOfFreedom_MaxBoundsDamping.md) | Gets the maximum damping value. The value is in database units, where lengths are is always expressed in centimeters, angles in radians, and time in seconds. |
| [MaxBoundsStiffness](../DSDegreeOfFreedom/DSDegreeOfFreedom_MaxBoundsStiffness.md) | Gets the maximum stiffness value. The value is in database units, where lengths are is always expressed in centimeters, angles in radians, and time in seconds. |
| [MaxBoundsValue](../DSDegreeOfFreedom/DSDegreeOfFreedom_MaxBoundsValue.md) | Gets the maximum value of the joint. The value is in database units, which for linear bounds is centimeters and radial bounds is radians. |
| [MinBoundsDamping](../DSDegreeOfFreedom/DSDegreeOfFreedom_MinBoundsDamping.md) | Gets the minimuim damping value. The value is in database units, which for linear bounds is centimeters and radial bounds is radians. |
| [MinBoundsStiffness](../DSDegreeOfFreedom/DSDegreeOfFreedom_MinBoundsStiffness.md) | Gets the minimum stiffness value. |
| [MinBoundsValue](../DSDegreeOfFreedom/DSDegreeOfFreedom_MinBoundsValue.md) | Gets the minimum value of the joint. |
| [Parent](../DSDegreeOfFreedom/DSDegreeOfFreedom_Parent.md) | Returns the DSJointDefinition object this degree of freedom is associated with. |
| [Results](../DSDegreeOfFreedom/DSDegreeOfFreedom_Results.md) | Gets the DSResults object that provides access to the simulation results associated with this degree of freedom. |
| [Type](../DSDegreeOfFreedom/DSDegreeOfFreedom_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[DSDegreesOfFreedom.Item](../DSDegreesOfFreedom/DSDegreesOfFreedom_Item.md), [DSResult.Parent](../DSResult/DSResult_Parent.md)

## Version

Introduced in version 2013

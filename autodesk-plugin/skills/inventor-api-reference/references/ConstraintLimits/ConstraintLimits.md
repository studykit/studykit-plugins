# ConstraintLimits Object

## Description

The ConstraintLimits object provides access to various limits related settings for assembly constraints and iMate definitions.

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../ConstraintLimits/ConstraintLimits_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Maximum](../ConstraintLimits/ConstraintLimits_Maximum.md) | Property that returns the Parameter object that controls the maximum limit value. This property returns Nothing if the maximum limit has never been enabled for this constraint or the parameter associated with the maximum value was deleted. Set the MaximumEnabled property to True to make this parameter available. |
| [MaximumEnabled](../ConstraintLimits/ConstraintLimits_MaximumEnabled.md) | Read-write property that gets and sets whether the maximum limit value should be enabled. Once enabled, the parameter returned in the Maximum property can be used to control the value of this limit. |
| [Minimum](../ConstraintLimits/ConstraintLimits_Minimum.md) | Property that returns the Parameter object that controls the minimum limit value. This property returns Nothing if the minimum limit has never been enabled for this constraint or the parameter associated with the minimum value was deleted. Set the MinimumEnabled property to True to make this parameter available. |
| [MinimumEnabled](../ConstraintLimits/ConstraintLimits_MinimumEnabled.md) | Read-write property that gets and sets whether the minimum limit value should be enabled. Once enabled, the parameter returned in the Minimum property can be used to control the value of this limit. |
| [Parent](../ConstraintLimits/ConstraintLimits_Parent.md) | Property that returns the parent object. This can be one of the strongly typed assembly constraint objects (such as MateConstraint) or one of the strongly typed iMate definition objects (such as MateiMateDefinition). |
| [RestingPositionEnabled](../ConstraintLimits/ConstraintLimits_RestingPositionEnabled.md) | Read-write property that gets and sets whether the resting position value should be enabled. If enabled, the constraint snaps back to the nominal value after a drag or a solve. |
| [Type](../ConstraintLimits/ConstraintLimits_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[AngleConstraint.ConstraintLimits](../AngleConstraint/AngleConstraint_ConstraintLimits.md), [AngleConstraintProxy.ConstraintLimits](../AngleConstraintProxy/AngleConstraintProxy_ConstraintLimits.md), [FlushConstraint.ConstraintLimits](../FlushConstraint/FlushConstraint_ConstraintLimits.md), [FlushConstraintProxy.ConstraintLimits](../FlushConstraintProxy/FlushConstraintProxy_ConstraintLimits.md), [FlushiMateDefinition.ConstraintLimits](../FlushiMateDefinition/FlushiMateDefinition_ConstraintLimits.md), [FlushiMateDefinitionProxy.ConstraintLimits](../FlushiMateDefinitionProxy/FlushiMateDefinitionProxy_ConstraintLimits.md), [InsertConstraint.ConstraintLimits](../InsertConstraint/InsertConstraint_ConstraintLimits.md), [InsertConstraintProxy.ConstraintLimits](../InsertConstraintProxy/InsertConstraintProxy_ConstraintLimits.md), [InsertiMateDefinition.ConstraintLimits](../InsertiMateDefinition/InsertiMateDefinition_ConstraintLimits.md), [InsertiMateDefinitionProxy.ConstraintLimits](../InsertiMateDefinitionProxy/InsertiMateDefinitionProxy_ConstraintLimits.md), [MateConstraint.ConstraintLimits](../MateConstraint/MateConstraint_ConstraintLimits.md), [MateConstraintProxy.ConstraintLimits](../MateConstraintProxy/MateConstraintProxy_ConstraintLimits.md), [MateiMateDefinition.ConstraintLimits](../MateiMateDefinition/MateiMateDefinition_ConstraintLimits.md), [MateiMateDefinitionProxy.ConstraintLimits](../MateiMateDefinitionProxy/MateiMateDefinitionProxy_ConstraintLimits.md), [TangentConstraint.ConstraintLimits](../TangentConstraint/TangentConstraint_ConstraintLimits.md), [TangentConstraintProxy.ConstraintLimits](../TangentConstraintProxy/TangentConstraintProxy_ConstraintLimits.md), [TangentiMateDefinition.ConstraintLimits](../TangentiMateDefinition/TangentiMateDefinition_ConstraintLimits.md), [TangentiMateDefinitionProxy.ConstraintLimits](../TangentiMateDefinitionProxy/TangentiMateDefinitionProxy_ConstraintLimits.md)

## Version

Introduced in version 2011
